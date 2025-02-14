#!/usr/bin/env bash
set -eo pipefail

environment= "$1"
tag="$2"

            url="https://twdps.io/v1/hello/healthz"
            if [[ "<< parameters.namespace >>" != "prod" ]];  then
              url="https://<< parameters.namespace >>.twdps.io/v1/hello/healthz"
            fi
            echo "test $url for version=<< parameters.tag >>"
            reponse=$(curl "$url")
            version=$(echo $reponse | jq -r .version)
            echo "version $version"
            if [[ "$version" != "<< parameters.tag >>" ]]; then
                echo "error: healthz not ok"
                exit 1
            fi