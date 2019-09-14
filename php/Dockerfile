FROM debian:10

RUN apt-get update && \
	apt-get install -y php7.3 php7.3-curl php7.3-pgsql php7.3-fpm && \
	rm -rf /var/lib/apt/lists/*

RUN useradd php

RUN sed -i~ -e "s/short_open_tag = Off/short_open_tag = On/" \
        -e "s/display_errors = Off/display_errors = On/" \
        -e "s/display_startup_errors = Off/display_startup_errors = On/" \
        /etc/php/7.3/fpm/php.ini

RUN sed -i~ -e "s#listen = /run/php/php7.3-fpm.sock#listen = 0.0.0.0:9000#" \
        -e "s/user = www-data/user = php/" \
        /etc/php/7.3/fpm/pool.d/www.conf

RUN mkdir -p /run/php && \
	chown php /run/php

CMD ["/usr/sbin/php-fpm7.3", "--nodaemonize", "--fpm-config", "/etc/php/7.3/fpm/php-fpm.conf"]