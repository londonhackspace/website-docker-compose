FROM debian:10

RUN apt-get update && \
	apt-get install -y python3-virtualenv virtualenv python3-dev libpq-dev build-essential postgresql-client && \
	rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash django

COPY run.sh /run.sh
RUN chmod a+x /run.sh

USER django

CMD ["/run.sh"]