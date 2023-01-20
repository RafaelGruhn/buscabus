#!/bin/bash

set -e

pip install --upgrade pip
pip install -r /temp/requirements/main.txt

if [ "$MODE" = "production" ]; then
  pip install -r /temp/requirements/production.txt
fi

exit 0
