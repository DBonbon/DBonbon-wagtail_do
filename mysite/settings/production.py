from .base import *

DEBUG = int(os.environ.get("DEBUG", default=1))
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq

# Recapcha settings
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

try:
    from .local import *
except ImportError:
    pass
