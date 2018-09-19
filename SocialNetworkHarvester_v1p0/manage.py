#!/usr/bin/env python
import os
import sys

import pymysql
pymysql.install_as_MySQLdb()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SocialNetworkHarvester_v1p0.settings")

    from django.core.management import execute_from_command_line
    import SocialNetworkHarvester_v1p0.settings
    execute_from_command_line(sys.argv)

