# sales-service

[![CircleCI](https://circleci.com/gh/guimunarolo/sales-service.svg?style=shield)](https://circleci.com/gh/guimunarolo/sales-service)
[![codecov](https://codecov.io/gh/guimunarolo/sales-service/branch/master/graph/badge.svg)](https://codecov.io/gh/guimunarolo/sales-service)

Simple service using [Fast API](https://github.com/tiangolo/fastapi) to control sales with cashback.


## How to install

With `pipenv` already installed just run:

```bash
$ pipenv install --dev
$ cp local.env .env
```


## How to run

Set the API Token and run it with:

```bash
$ EXTERNAL_API_TOKEN={token} make run
```

> You can also use the .env to set the Token

Now it's running at [http://localhost:8000](http://localhost:8000)


## Documentation

With the service running you can access the documentation at [http://localhost:8000/docs](http://localhost:8000/docs)


## Running tests

```bash
$ make test
```
