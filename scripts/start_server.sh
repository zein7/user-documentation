export aristotlemdr__BASE_DIR=/tmp/aristotle_docs
tox -e server runserver 127.0.0.1:8080 > server.log 2>&1 &
printf 'Waiting for webserver '
until $(curl --output /dev/null --silent --head --fail 127.0.0.1:8080); do
    printf '.'
    sleep 2
done
printf ' up!\n'