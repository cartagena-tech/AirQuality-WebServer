# base image
FROM postgres:11.1-alpine

COPY /maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance


# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
