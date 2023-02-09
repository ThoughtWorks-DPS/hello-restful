FROM python:3.9-alpine as builder

LABEL maintainer=<nchenewe@thoughtworks.com>
LABEL org.opencontainers.image.source https://github.com/ThoughtWorks-DPS/hello-restful

ENV MUSL_LOCPATH=/usr/share/i18n/locales/musl \
    LANG="C.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1

# hadolint ignore=DL3003
RUN apk add --no-cache \
        libintl==0.21.1-r1 && \
    apk --no-cache add --virtual build-dependencies \
        cmake==3.24.3-r0 \
        make==4.3-r1 \
        musl==1.2.3-r4 \
        musl-dev==1.2.3-r4 \
        musl-utils==1.2.3-r4 \
        gcc==12.2.1_git20220924-r4 \
        gettext-dev==0.21.1-r1 && \
    wget -q https://gitlab.com/rilian-la-te/musl-locales/-/archive/master/musl-locales-master.zip && \
    unzip musl-locales-master.zip && cd musl-locales-master && \
    cmake -DLOCALE_PROFILE=OFF -D CMAKE_INSTALL_PREFIX:PATH=/usr . && \
    make && make install && \
    cd .. && rm -r musl-locales-master && \
    adduser -D hello && \
    apk del build-dependencies

USER hello
WORKDIR /home/hello

COPY --chown=hello:hello /api ./api
COPY --chown=hello:hello Pipfile Pipfile
ENV PATH="/home/hello/.local/bin:/home/hello/.venv/bin:${PATH}"

RUN pip install --user --no-cache-dir pipenv==2022.4.21 && \
    PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

# the below does not work. Nothing copied is actually visible within the runtime,
# though this is still a widely documented method.
#
# FROM gcr.io/distroless/python3:debug-amd64

# ENV MUSL_LOCPATH=/usr/share/i18n/locales/musl \
#     LANG="C.UTF-8" \
#     LANGUAGE="en_US.UTF-8" \
#     LC_ALL="en_US.UTF-8" \
#     PATH="/home/nonroot/.local/bin:/home/nonroot/.venv/bin:${PATH}"

# COPY --chown=nonroot:nonroot --from=builder /home/hello/.venv /home/nonroot/.venv
# COPY --chown=nonroot:nonroot /api /home/nonroot/api
# WORKDIR /home/nonroot

CMD [".venv/bin/uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
