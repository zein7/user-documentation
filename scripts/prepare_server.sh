# Put in any argument to skip rebuilding the pipenv virtualenv

mkdir /tmp/aristotle_docs -p
export DATABASE_PATH=aristotle.db
cd ./python/server
cp server.env .env

if [[ $# -eq 0 ]]; then
    pipenv install --three --dev --skip-lock
fi
pipenv run django-admin createcachetable
pipenv run django-admin migrate --noinput
pipenv run django-admin migrate --run-syncdb  --noinput
pipenv run django-admin compilestatic -v0
pipenv run django-admin collectstatic --noinput -v0
pipenv run django-admin loaddata --app docs_server users.yaml
pipenv run django-admin loaddata --app docs_server iso_metadata.json
pipenv run django-admin loaddata --app docs_server test_metadata.yaml
# pipenv run django-admin loaddata --app docs_server extra_metadata.yaml
pipenv run django-admin rebuild_index --noinput
rm .env
cd -
