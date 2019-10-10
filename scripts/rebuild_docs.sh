django-admin migrate -- --run-syncdb  --noinput
django-admin compilestatic -v0
django-admin collectstatic -- --noinput -v0
django-admin loaddata --app docs_server iso_metadata.json
django-admin loaddata --app docs_server test_metadata.json
django-admin loaddata --app docs_server extra_metadata.yaml
django-admin rebuild_index -- --noinput