# Updated ALLOWED_HOSTS and DEBUG settings based on the environment

import os

# Set DEBUG based on the environment variable
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Define ALLOWED_HOSTS
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',') if os.getenv('ALLOWED_HOSTS') else []
