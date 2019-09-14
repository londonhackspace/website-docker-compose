Quick Start:
```
git submodule update --init --recursive
mkdir -p hackspace-foundation-sites/var/session
chmod 777 hackspace-foundation-sites/var/ -R
cp config-files/config.php hackspace-foundation-sites/etc/
cp config-files/production_settings.py hackspace-foundation-sites/lhs/
docker-compose up
```