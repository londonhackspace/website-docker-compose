FROM postgres:11-alpine

# minor tweak to the container: create a scratch space for the django
# container to keep initialisation state in

RUN mkdir -p /data/scratch && \
	chmod 777 /data/scratch

VOLUME /data/scratch