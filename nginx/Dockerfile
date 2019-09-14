FROM debian:10

RUN apt-get update && \
	apt-get install -y nginx && \
	rm -rf /var/lib/apt/lists/*

RUN rm -f /etc/nginx/conf.d/default.conf && \
	rm -f /etc/nginx/sites-enabled/default

COPY lhs.conf /etc/nginx/conf.d/lhs-www-test.conf

CMD ["nginx", "-g", "daemon off; master_process on;"]