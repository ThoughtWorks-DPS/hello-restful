#!/usr/bin/env bash
set -eo pipefail

export env=$1
export tag=$2

echo "deploy hello-restful:$tag to demo-$env"
helm upgrade hello-restful charts/hello-restful \
      --install --atomic --timeout 60s \
      --namespace "demo-$env" \
      --values "charts/hello-restful/values.yaml" \
      --values "charts/hello-restful/values-$env.yaml" \
      --set image.tag="$tag"
