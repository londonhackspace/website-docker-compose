#!/bin/bash

set -e

cd /var/www/hackspace-foundation-sites
virtualenv -p python3 ~/venv
~/venv/bin/pip install -r requirements.txt

export PGDATABASE=hackspace
export PGHOST=db
export PGUSER=hackspace

echo "db:*:hackspace:hackspace:hackspace" > ~/.pgpass
chmod 600 ~/.pgpass

if [ ! -f /data/scratch/init ]; then
	~/venv/bin/python manage.py migrate sites
	~/venv/bin/python manage.py migrate
	~/venv/bin/python manage.py loaddata main/fixtures/*

	psql < /var/www/hackspace-foundation-sites/etc/create-flourish-tables.sql
	psql < /var/www/hackspace-foundation-sites/etc/restore-column-defaults.sql
	psql < /var/www/hackspace-foundation-sites/etc/restore-multicolumn-pks.sql

	touch /data/scratch/init
fi

~/venv/bin/python manage.py runserver 0.0.0.0:9001