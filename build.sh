#!/bin/bash

docker build -t lhs-website-php php
docker build -t lhs-website-nginx nginx
docker build -t lhs-website-django django
docker build -t lhs-website-db db