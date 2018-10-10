from datetime import timedelta

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from AspiraUser.models import UserProfile
from SocialNetworkHarvester.jsonResponses import *
from SocialNetworkHarvester.loggers.viewsLogger import logError
from SocialNetworkHarvester.settings import DEBUG
from SocialNetworkHarvester.views.messages import add_info_message, add_error_message, add_error_messages
from Youtube.models import *
from .pages import userSettings, lastUrlOrHome


def userLogin(request):
    username = request.POST['username']
    pw = request.POST['password']
    user = authenticate(username=username, password=pw)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            add_error_message(
                'Ce nom d\'utilisateur existe, mais le compte est '
                'présentement inactif. Est-ce que le webmaster vous '
                'a contacté?'
            )
    else:
        add_error_message(request, 'Invalid login information')

    return lastUrlOrHome(request)


@login_required()
def userLogout(request):
    for select in request.user.tableRowsSelections.all():
        select.delete()
    logout(request)
    return lastUrlOrHome(request)


# @viewsLogger.debug()
@login_required()
def editUserSettings(request):
    user = request.user
    # pretty(request.POST)
    for atr in request.POST:
        if atr not in [
            'u_first_name',
            'u_last_name',
            'u_email',
            'p_twitterApp_consumerKey',
            'p_twitterApp_consumer_secret',
            'p_twitterApp_access_token_key',
            'p_twitterApp_access_token_secret',
            'p_youtubeApp_dev_key'
        ] and not atr == 'csrfmiddlewaretoken':
            add_error_message('Une erreur est survenue. Veuillez contacter l\'administrateur.')
            return redirect('/settings')
        if atr[0] == 'u':
            setattr(user, atr[2:], request.POST[atr])
        elif atr[0] == 'p':
            setattr(user.userProfile, atr[2:], request.POST[atr])
    user.save()
    user.userProfile.twitterApp_parameters_error = False
    user.userProfile.facebookApp_parameters_error = False
    user.userProfile.youtubeApp_parameters_error = False
    user.userProfile.save()
    add_info_message(request, 'Vos paramètres ont été mis à jour. Merci!')
    return redirect('/settings')


def userRegister(request):
    data = request.POST
    errors = []
    masterAddrs = [user.email for user in User.objects.filter(is_superuser=True, email__isnull=False) if
                   user.email != '']
    required_fields = {'username': 'Username',
                       'email': 'Email address',
                       'pw': 'Password'}
    context = {
        'user': request.user,
        'navigator': [
            ('Enregistrement', '#')
        ]
    }

    for field in required_fields.keys():
        if field not in data or data[field] == '':
            errors.append('Le champ "%s" est vide! Veuillez y insérer une valeur.' % required_fields[field])

    if not errors and data['pw'] != data['pw_confirm']:
        errors.append('Les mots de passe ne coincident pas!')

    if not errors and len(data['pw']) < 6:
        errors.append('Votre mot de passe doit avoir au moins 6 caractères.')

    if not errors and User.objects.filter(email=data['email']).exists():
        errors.append('Un compte avec cette adresse email existe déjà!')

    if not errors and User.objects.filter(username=data['username']).exists():
        errors.append('Un compte avec ce nom d\'utilisateur existe déjà!')

    if not errors and not validate_userName(data['username']):
        errors.append('Le nom d\'utilisateur ne peut contenir que des caractères alphanumériques.')

    if not errors:
        try:
            validate_email(data['email'])
        except ValidationError:
            errors.append('L\'adresse email fournie ne semble pas valide. Veuillez vérifier qu\'il '
                                'ne s\'agit pas d\'une erreur.')

    if not errors:
        message = render_to_string('AspiraUser/emails/newAccountInstructions.html', {
            'username': data['username'],
            'fname': data['fname'],
            'lname': data['lname'],
            'org': data['org'],
            'webmasters': masterAddrs,
        })
        send_mail('SNH - Account creation instructions', 'message',
                  'doNotReplyMail', [data['email']], html_message=message)

    if not errors:
        try:
            newUser = User.objects.create_user(data['username'], data['email'], data['pw'],
                                               first_name=data['fname'],
                                               last_name=data['lname'],
                                               is_active=False
                                               )
            newProfile = UserProfile.objects.create(user=newUser)
        except:
            logError('An error occured while creating a new AspiraUser!')
            errors.append('An error occured! Please contact the webmaster directly to create your account.')

    if not errors:
        message = render_to_string('AspiraUser/emails/validateNewAccount.html', {
            'email': data['email'],
            'username': data['username'],
            'fname': data['fname'],
            'lname': data['lname'],
            'org': data['org'],
            'usageText': data['usageText'],
            'adminAuth': "https://%s/adminauth/user/%s/change/" % (request.get_host(), newUser.pk)
        })

        try:
            send_mail('SNH - New account creation request', 'message',
                      'doNotReplyMail', masterAddrs, html_message=message)
        except:
            logError('An error occured while sending an email to %s' % masterAddrs)

    if errors:
        add_error_messages(request, errors)
        fieldKeeper = {}
        for field in ['fname', 'username', 'org', 'email', 'lname', 'usageText']:
            if field in data:
                fieldKeeper[field] = data[field]
        context['fieldKeeper'] = fieldKeeper
        template = 'AspiraUser/login_page.html'
    else:
        add_info_message(request, "Merci! Vous reçevrez un courriel aussitôt que \
        votre compte est approuvé par le webmaster.")
        template = 'AspiraUser/register_successful.html'
    return render(request, template, context)


def validate_userName(userName):
    return re.match(r'^[_a-zA-Z0-9]+$', userName)


def confAgreement(request):
    return render(request, 'AspiraUser/confidentPol.html', {})


def browserList(request):
    return render(request, "AspiraUser/browserList.html", {})


@login_required()
def updatePW(request):
    user = request.user
    if not all(
            ['pass0' in request.POST, 'pass1' in request.POST, 'pass2' in request.POST]):
        return jResponse({'status': 'error',
                          'errors': ['Requête invalide']})

    if not user.check_password(request.POST['pass0']):
        return jsonErrors('Mauvais mot de passe actuel')

    if user.check_password(request.POST['pass1']):
        return jsonErrors('Le nouveau mot de passe doit être différent du mot de passe actuel')

    if len(request.POST['pass1']) < 6:
        return jsonErrors('Le mot de passe doit contenir au moins 6 caractères.')

    if request.POST['pass1'] != request.POST['pass2']:
        return jsonErrors('Les mots de passe de concordent pas.')

    try:
        user.set_password(request.POST['pass1'])
        user.save()
        update_session_auth_hash(request, user)
    except Exception as e:
        return jResponse({'status': 'error',
                          'errors': [str(e)]})

    return jResponse({'status': 'ok'})


def requestResetPW(request):
    if request.user.is_authenticated:
        return jsonErrors('Vous devez être déconnecté pour réinitialiser votre mot de passe')
    if 'email' not in request.POST:
        return missingParam('email')

    aspiraUser = User.objects.filter(email=request.POST['email']).first()
    if not aspiraUser:
        return jsonErrors("L'adresse email '%s' n'existe pas." % request.POST['email'])

    aspiraUser.userProfile.passwordResetToken = UserProfile.getUniquePasswordResetToken()
    aspiraUser.userProfile.passwordResetDateLimit = datetime.utcnow() \
                                                        .replace(second=0, microsecond=0, tzinfo=utc) + timedelta(
        days=1)
    aspiraUser.userProfile.save()

    if DEBUG:
        url = "http://localhost/user/forms/resetPW/"
    else:
        url = "https://aspira.ulaval.ca/user/forms/resetPW/"

    message = render_to_string('AspiraUser/emails/resetPassword.html', {
        'aspiraUser': aspiraUser,
        'link': url + aspiraUser.userProfile.passwordResetToken,
        'webmasters': [user.email for user in User.objects.filter(is_superuser=True, email__isnull=False) if
                       user.email != ''],
    })
    send_mail('SNH - Réinitialisation du mot de passe', 'message',
              'doNotReplyMail', [request.POST['email']], html_message=message)

    return jResponse({'status': 'ok'})
