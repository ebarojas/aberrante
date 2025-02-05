#!/bin/sh
# Use this when promoting requires a migrations
# Deploy script when promoting needs migrations ==== Only works in production

heroku maintenance:on --app aberrante
# heroku scale worker=0 --app aberrante
heroku run python ./aberrante/manage.py migrate --app aberrante
# heroku scale worker=1 --app aberrante
heroku maintenance:off --app aberrante
