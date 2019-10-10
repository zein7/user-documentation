# Put in any argument to skip rebuilding the pipenv virtualenv

mkdir /tmp/aristotle_docs -p
cd ./python/server
cp server.env .env
pipenv install pip==18.0

if [[ $# -eq 0 ]]; then
    echo "INSTALLING";
    pipenv install --three --dev --skip-lock
    pipenv graph
else
    echo "NOT INSTALLING!!";
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
