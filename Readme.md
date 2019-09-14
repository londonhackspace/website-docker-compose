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