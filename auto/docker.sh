#!/usr/bin/env bash
target=dev
service=proj
env_src=(.env)

SERVICE=${service^^}
TARGET=${target^^}
env $(cat "${env_src[@]}" | grep -v '#' | xargs) bash -c '\
    tag=bazawinner/'$target'-$BW_PROJ_NAME-'$service':$BW_'$TARGET'_'$SERVICE'_VERSION 
    docker run -p 8888:8888 -v "'$PWD'/data":/home/jovyan/work $tag
'
# env $(cat "${env_src[@]}" | grep -v '#' | xargs) bash -c '\
#     tag=bazawinner/'$target'-$BW_PROJ_NAME-'$service':$BW_'$TARGET'_'$SERVICE'_VERSION
#     docker run -p $BW_'$TARGET'_'$SERVICE'_VERSION:8888 -v "$PWD/data":/home/jovyan/work $tag
# '
