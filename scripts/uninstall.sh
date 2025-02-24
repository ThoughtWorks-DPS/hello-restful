#!/usr/bin/env bash
set -eo pipefail

env=$1
tag=$2

echo "uninstall hello-restful:$tag from demo-$env"
helm uninstall hello-restful --namespace "demo-$env"
