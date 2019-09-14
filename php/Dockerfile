FROM debian:8

RUN apt-get update && \
	apt-get install -y php5 php5-curl php-apc php5-pgsql php5-fpm && \
	rm -rf /var/lib/apt/lists/*

RUN useradd php

RUN sed -i~ -e "s/short_open_tag = Off/short_open_tag = On/" \
        -e "s/display_errors = Off/display_errors = On/" \
        -e "s/display_startup_errors = Off/display_startup_errors = On/" \
        /etc/php5/fpm/php.ini

RUN sed -i~ -e "s#listen = /var/run/php5-fpm.sock#listen = 0.0.0.0:9000#" \
        -e "s/user = www-data/user = php/" \
        /etc/php5/fpm/pool.d/www.conf

CMD ["/usr/sbin/php5-fpm", "--nodaemonize", "--fpm-config", "/etc/php5/fpm/php-fpm.conf"]