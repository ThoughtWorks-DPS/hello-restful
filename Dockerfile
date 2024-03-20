FROM python:3.11-alpine

LABEL org.opencontainers.image.title="hello-restful" \
      org.opencontainers.image.description="Lightweight API providing request and response endpoints" \
      org.opencontainers.image.documentation="https://github.com/ThoughtWorks-DPS/hello-restful" \
      org.opencontainers.image.source="https://github.com/ThoughtWorks-DPS/hello-restful" \
      org.opencontainers.image.url="https://github.com/ThoughtWorks-DPS/hello-restful" \
      org.opencontainers.image.vendor="ThoughtWorks, Inc." \
      org.opencontainers.image.licenses="MIT"

ENV MUSL_LOCPATH=/usr/share/i18n/locales/musl \
    LANG="C.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8" \
    PATH="/home/hello/.local/bin:${PATH}"

# hadolint ignore=DL3003
RUN apk add --no-cache \
        libintl==0.22.3-r0 && \
    apk --no-cache add --virtual build-dependencies \
        cmake==3.27.8-r0 \
        make==4.4.1-r2 \
        musl==1.2.4_git20230717-r4 \
        musl-dev==1.2.4_git20230717-r4 \
        musl-utils==1.2.4_git20230717-r4 \
        gcc==13.2.1_git20231014-r0 \
        gettext-dev==0.22.3-r0 && \
    wget -q https://gitlab.com/rilian-la-te/musl-locales/-/archive/master/musl-locales-master.zip && \
    unzip musl-locales-master.zip && cd musl-locales-master && \
    cmake -DLOCALE_PROFILE=OFF -D CMAKE_INSTALL_PREFIX:PATH=/usr . && \
    make && make install && \
    cd .. && rm -r musl-locales-master && \
    adduser -D hello && \
    apk del build-dependencies

USER hello
WORKDIR /home/hello
ENV PATH="/home/hello/.local/bin:${PATH}"

COPY --chown=hello:hello api/ api/
COPY --chown=hello:hello requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
