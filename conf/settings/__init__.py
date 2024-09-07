from split_settings.tools import include

settings = [
    "django.py",  # standard django settings
    "database.py",  # postgres
    "rest_framework.py",  # rest-framework settings
    "admin_reorder.py",  # admin_reorder settings
]

# Include settings:
include(*settings)
