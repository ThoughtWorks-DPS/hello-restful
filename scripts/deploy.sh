#!/usr/bin/env bash
set -eo pipefail

environment="$1"
tag="$2"

echo "deploy hello-restful:$tag to demo-$environment"
helm upgrade hello-restful charts/hello-restful \
      --install --atomic --timeout 60s \
      --namespace "demo-$environment" \
      --values "charts/hello-restful/values.yaml" \
      --values "charts/hello-restful/values-$environment.yaml" \
      --set image.tag="$tag"
