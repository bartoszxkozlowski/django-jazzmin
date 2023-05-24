import django

version = "2.6.2-bxk-custom"

if django.VERSION < (3, 2):
    default_app_config = "jazzmin.apps.JazzminConfig"
