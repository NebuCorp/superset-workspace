#!/bin/bash

# Upgrading Superset metastore must be done before user creation
superset db upgrade

# create Admin user, you can read these values from env or anywhere else possible
superset fab create-admin \
    --username "$ADMIN_USERNAME" \
    --firstname Superset \
    --lastname Admin \
    --email "$ADMIN_EMAIL" \
    --password "$ADMIN_PASSWORD"

# Finally initialize roles and permissions
superset init

# Load some examples to play with
superset load_examples

# Set the database URI
superset set-database-uri \
    --database-name "PostgreSQL" \
    --uri "${DATABASE_DIALECT}://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${DATABASE_PORT}/${DATABASE_DB}"

# Initialize the superset app
/bin/sh -c /usr/bin/run-server.sh