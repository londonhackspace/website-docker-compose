Quick Start:
```
git submodule update --init --recursive
mkdir -p hackspace-foundation-sites/var/session
chmod 777 hackspace-foundation-sites/var/ -R
cp config-files/config.php hackspace-foundation-sites/etc/
cp config-files/production_settings.py hackspace-foundation-sites/lhs/
docker-compose up
```

One slightly quirky thing about this container stack is that the django container, which does the db initialisation, has a shared directory with the database container. This is done so that when the database container is recreated, the initialisation is redone.

Note that because this uses git submodules, you'll probably want to do a pull before doing any development
```
cd hackspace-foundation-sites
git pull
cd ..
```

also, if you want to be able to push your changes, you'll want to set the remote url to something more writable

```
cd hackspace-foundation-sites
git remote set-url origin git@github.com:londonhackspace/hackspace-foundation-sites.git
```

You'll also want to set the Django loopback URLs to suit the containers in your production_settings.py file:
```
FLOURISH_LOOPBACK_URLS = {
    'authenticate': 'http://nginx:8080/session.php',
    'destroy': 'http://nginx:8080/session.php?destroy',
}
```

The database config in production_settings.py should look like this:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'db',
        'NAME': 'hackspace',
        'USER': 'hackspace',
        'PASSWORD': 'hackspace',
    }
}
```