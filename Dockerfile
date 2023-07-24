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
        libintl==0.21.1-r7 && \
    apk --no-cache add --virtual build-dependencies \
        cmake==3.26.5-r0 \
        make==4.4.1-r1 \
        musl==1.2.4-r0 \
        musl-dev==1.2.4-r0 \
        musl-utils==1.2.4-r0 \
        gcc==12.2.1_git20220924-r10 \
        gettext-dev==0.21.1-r7 && \
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
