# -*- coding: utf-8 -*-

import os
from django.contrib.auth.hashers import make_password

os.environ.setdefault("DJANGO_SETTING_MODULE", "settings")

p = input("please pass to encode:")

p_encode = make_password(p, None, 'pbkdf2_sha256')

print('pass encoded:', p_encode)
