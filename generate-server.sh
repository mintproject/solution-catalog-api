#!/usr/bin/env bash
dir=${PWD}
SERVER_DIR=server
docker run -ti --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v4.1.2 \
     generate  \
     -i /local/openapi.yaml\
     -g python-flask  \
     -o /local/$SERVER_DIR/ \
     --git-repo-id viz-ingestion \
     --git-user-id mintproject \
     --ignore-file-override /local/.openapi-generator-ignore
