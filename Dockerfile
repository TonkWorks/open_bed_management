FROM python:3.6.1-alpine
MAINTAINER Kevin Dagostino <kevin@tonkworks.com>

# Copy in your requirements file
ADD /app/requirements.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step. Correct the path to your production requirements file, if needed.
RUN set -ex \
    && apk add --no-cache --virtual .build-deps \
        autoconf \
        automake \
        freetype-dev \
        g++ \
        gcc \
        jpeg-dev \
        lcms2-dev \
        libffi-dev \
        libpng-dev \
        libwebp-dev \
        linux-headers \
        make \
        openjpeg-dev \
        openssl-dev \
    && pyvenv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
    && runDeps="$( \
            scanelf --needed --nobanner --recursive /venv \
                    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                    | sort -u \
                    | xargs -r apk info --installed \
                    | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps

# Install nginx and supervisor
RUN set -ex && apk add --no-cache --virtual .build-deps nginx supervisor
RUN mkdir /etc/nginx/sites-enabled
RUN rm /etc/nginx/nginx.conf
RUN rm /etc/supervisord.conf
RUN mkdir /run/nginx


# Copy your application code to the container (make sure you create a .dockerignore file if any large files or directories should be excluded)
ENV APP_PRODUCTION=1

RUN mkdir /code
RUN mkdir /code/app
WORKDIR /code/app/
ADD . /code/

# Run Development Mode
#EXPOSE 8000
#CMD ["/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

# Run just uwsgi
#EXPOSE 8000
#ENV UWSGI_VIRTUALENV=/venv UWSGI_WSGI_FILE=/code/app/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000
#CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]


# Run uwsgi and nginx
RUN ln -s /code/nginx/nginx.conf /etc/nginx/ && \
    ln -s /code/nginx/nginx-app.conf /etc/nginx/sites-enabled/  && \
    ln -s /code/supervisord/supervisord.conf /etc/

CMD ["supervisord", "-n"]