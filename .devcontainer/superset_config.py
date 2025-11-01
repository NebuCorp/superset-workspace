#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath_dev/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#
# superset_config.py

import os

# ---------------------------------------------------------
# Superset specific config
# ---------------------------------------------------------

# The base URL for your local Superset instance
SUPERSET_WEBSERVER_PORT = 8088  # Change if you use a different port

# Enable or disable debug mode
DEBUG = True

# The secret key for signing session cookies
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "your_secret_key")

APP_NAME = "Superset"


# ---------------------------------------------------------
# Database connection config
# ---------------------------------------------------------

# Needed for Mapbox GL JS to render maps
# Replace with your actual Mapbox API key
MAPBOX_API_KEY=os.getenv("MAPBOX_API_KEY")
# Needed To pass data from superset to front end
ENABLE_JAVASCRIPT_CONTROLS  = True
# Example connection to a local PostgreSQL database
THUMBNAILS_ENABLED = False
DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

print(f"DATABASE_DIALECT: {DATABASE_DIALECT}")
print(f"DATABASE_HOST: {DATABASE_HOST}")
print(f"DATABASE_PORT: {DATABASE_PORT}")
print(f"DATABASE_DB: {DATABASE_DB}")
# Add this after your DATABASE_* variables
SQLALCHEMY_DATABASE_URI = f"{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
print(f"SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")

# Cache configuration for development (simple in-memory cache)
CACHE_CONFIG = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

# WEBDRIVER_BASEURL_USER_FRIENDLY = f"http://localhost:8888/{os.environ.get('SUPERSET_APP_ROOT', '/')}/"
# WEBDRIVER_BASEURL = f"http://superset_app{os.environ.get('SUPERSET_APP_ROOT', '/')}/"

# ---------------------------------------------------------
# Flask App Builder specific config
# ---------------------------------------------------------

# The default language to use for your app
BABEL_DEFAULT_LOCALE = "en"

# The default timezone to use
BABEL_DEFAULT_TIMEZONE = "UTC"

# ---------------------------------------------------------
# Feature Flags
# ---------------------------------------------------------

# Enable or disable specific Superset features
FEATURE_FLAGS = {
    "THUMBNAILS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ENABLE_JAVASCRIPT_CONTROLS":True , # Enable JavaScript controls for embedding
    "EMBEDDABLE_CHARTS": True,  # Enable embeddable charts
    "EMBEDDED_SUPERSET": True,  # Enable iframe for embedding
    "ENABLE_TEMPLATE_PROCESSING": True,  # This is generally a good idea, especially if you plan to use any dynamic content within your embedded dashboards (e.g., passing parameters through the iframe URL). It allows Superset to process Jinja templates.
}

# ---------------------------------------------------------
# Logging
# ---------------------------------------------------------

# Example logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {"format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "sqlalchemy.engine": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
}

# ---------------------------------------------------------
# Development Convenience
# ---------------------------------------------------------

# Allows importing charts and dashboards for testing
ENABLE_REACT_CRUD_VIEWS = True

# Automatically load examples for local testing
SUPERSET_LOAD_EXAMPLES = False


# ---------------------------------------------------------
# Superset Ifram config

# Enable CORS (replace with your SvelteKit domain for production)
ENABLE_CORS = True


CORS_OPTIONS = {
    "supports_credentials": True,
    "allow_headers": ["*"],
    "resources": ["*"],
    "origins": ["*"],  # In production, replace with your actual domain
}


# # Configure CSP (important for security)
CONTENT_SECURITY_POLICY = {
    "default-src": ["'self'"],
    "frame-src": [
        "'self'",
        "*",
    ],  # Allow all frame sources or specify your domain for production
    "style-src": ["'self'", "'unsafe-inline'"],  # Important for Superset styles
    "img-src": ["'self'", "data:"],  # For images and data URIs
}

GUEST_ROLE_NAME = "Gamma"  # The role for guest users, typically "Public" or "Gamma"
GUEST_TOKEN_JWT_SECRET = "test"  # Replace with a secure secret
GUEST_TOKEN_JWT_ALGO = "HS256"

# Important: Allow javascript controls for embedding
ENABLE_JAVASCRIPT_CONTROLS = True

# For public role access (ONLY for non-sensitive data!) https://superset.apache.org/docs/security/#public
PUBLIC_ROLE_LIKE = "Gamma"
# Disable CSRF protection for development
WTF_CSRF_ENABLED = False
# Disable SameSite cookie policy for development
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
# Set the application root for Superset - needed for embedding

# Disable X-Frame-Options to allow iframe embedding
TALISMAN_ENABLED = False
# Or if you want to keep Talisman but configure it:
# TALISMAN_CONFIG = {
#     'force_https': False,
#     'frame_options': 'ALLOWALL'
# }
