django-admin migrate -- --run-syncdb  --noinput
django-admin compilestatic -v0
django-admin collectstatic -- --noinput -v0
django-admin loaddata ./server/fixtures/iso_metadata.json
django-admin loaddata ./server/fixtures/test_metadata.json
django-admin rebuild_index -- --noinput