from pathlib import Path

SECRETS_DIR = Path("{{ helpdesk_secrets_dir }}")

#########################
#                       #
#   Required settings   #
#                       #
#########################

# Allow all hostnames - this validation is done by nginx instead.
ALLOWED_HOSTS = ["*"]

# Database configuration. See the Django documentation for a complete list of available parameters:
#   https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASE = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "db.sqlite",
    "CONN_MAX_AGE": 300,  # Max database connection age
}

# This key is used for secure generation of random numbers and strings. It must never be exposed outside of this file.
# For optimal security, SECRET_KEY should be at least 50 characters in length and contain a mix of letters, numbers, and
# symbols. Helpdesk will not run without this defined. For more information, see
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = SECRETS_DIR.joinpath("secret-key.txt").read_text()

#########################
#                       #
#   Optional settings   #
#                       #
#########################

BASE_PATH = "helpdesk/"

# Set to True to enable server debugging. WARNING: Debugging introduces a substantial performance penalty and may reveal
# sensitive information about your installation. Only enable debugging while performing testing. Never enable debugging
# on a production system.
DEBUG = False

EMAIL = {
  'BACKEND': 'django.core.mail.backends.console.EmailBackend'
}

# Title of the System
SYSTEM_TITLE = "Helpdesk"

# Time zone (default: UTC)
TIME_ZONE = "Europe/London"

VOLUNTEER_SIGNUP_CODE = SECRETS_DIR.joinpath("volunteer-signup-code.txt").read_text()
