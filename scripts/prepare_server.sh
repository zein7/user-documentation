# pip install -r ./server/requirements.txt

tox -e server migrate
tox -e server collectstatic -- --noinput
tox -e server compilestatic -- --noinput
tox -e server loaddata ./fixtures/iso_metadata.json
tox -e server loaddata ./fixtures/test_metadata.json
