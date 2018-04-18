cd ./python/server
cp server.env .env
pipenv run honcho start # > server.log 2>&1 &
printf 'Waiting for webserver '
until $(curl --output /dev/null --silent --head --fail $IP:$PORT); do
    printf '.'
    sleep 2
done
printf ' up!\n'
rm .env
cd -