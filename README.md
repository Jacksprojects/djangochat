# README

This is an example instant messaging project using Django, websockets and redis.

## Requirements

This app uses `channels` and `redis` to function correctly. If you don't have a redis server set up you can get one working quickly with docker by using this command in a terminal:
`sudo docker run -p 6379:6379 -d redis:5`

Additionally, the default database is not included, so you will need to run `makemigrations` before running the app.