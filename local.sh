export ENV=$1
export MODE=$2  

case $MODE in

  "d")
    helm upgrade --install --atomic --timeout 20s hello-restful charts/hello-restful \
      --namespace demo-$ENV \
      --values charts/hello-restful/values.yaml \
      --values charts/hello-restful/values-$ENV.yaml \
      --set image.tag=dev.aa7da86
    ;;

  "t")
    helm template hello-restful charts/hello-restful \
      --namespace demo-$ENV \
      --values charts/hello-restful/values.yaml \
      --values charts/hello-restful/values-$ENV.yaml \
      --set image.tag=dev.aa7da86
    ;;

  *)
    echo "no or unsupported mode flag"
    ;;
esac