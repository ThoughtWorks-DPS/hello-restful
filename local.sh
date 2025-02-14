#!/usr/bin/env bash
set -eo pipefail

export ENV="$1"
export MODE="$2"

case $MODE in

  "d")
    helm upgrade --install hello-restful charts/hello-restful \
      --namespace "demo-$ENV" \
      --values charts/hello-restful/values.yaml \
      --values "charts/hello-restful/values-$ENV.yaml" \
      --set image.tag=dev.d36e474
    ;;

  "t")
    helm template hello-restful charts/hello-restful \
      --namespace "demo-$ENV" \
      --values charts/hello-restful/values.yaml \
      --values "charts/hello-restful/values-$ENV.yaml" \
      --set image.tag=dev.ed5d3e7
    ;;

  *)
    echo "no or unsupported mode flag"
    ;;
esac

# --atomic --timeout 30s 