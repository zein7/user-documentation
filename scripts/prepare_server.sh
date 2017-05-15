mkdir /tmp/aristotle_docs -p
export aristotlemdr__BASE_DIR=/tmp/aristotle_docs
tox -e server migrate -- --run-syncdb  --noinput
tox -e server collectstatic -- --noinput -v0
tox -e server compilestatic -v0
tox -e server loaddata ./server/fixtures/iso_metadata.json
tox -e server loaddata ./server/fixtures/test_metadata.json
tox -e server rebuild_index --noinput