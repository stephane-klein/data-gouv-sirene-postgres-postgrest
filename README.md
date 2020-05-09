# Import data.gouv.fr Sirene in PostgreSQL with API REST

Status: Work in Progress, see [issues](https://github.com/stephane-klein/poc-data-gouv-siren-postgres/issues)

Import [Sirene](https://files.data.gouv.fr/insee-sirene/) data from [data.gouv.fr](https://www.data.gouv.fr) website to [PostgreSQL](postgresql.org/).

[PostgREST](http://postgrest.org) service is used to provide Sirene [API REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

## Importation notes

Considering that the file `StockUniteLegale_utf8.csv` is very big `2.6G` then some filters are applied before importation:

- drop `Cessée` [`etatAdministratifUniteLegale`](https://www.sirene.fr/sirene/public/variable/etatAdministratifUniteLegale)
- use `--ape-filter` to apply a filter on [`APE` code](https://www.sirene.fr/sirene/public/variable/activitePrincipaleUniteLegale)

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python3](https://www.python.org/)

[Homebrew](https://brew.sh/index_fr) instructions:

```sh
$ brew cask install docker
$ brew install python3 curl
```

## Getting started

Download data from https://files.data.gouv.fr/insee-sirene/:

```
$ ./scripts/download-data.sh
```

Start and initialize PostgreSQL database:

```
$ ./scripts/up.sh
```

Setup Python environment:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Import `StockUniteLegale_utf8.csv` file to PostgreSQL database:

```
$ ./import-csv-to-postgres.py --csv datas/StockUniteLegale_utf8.csv --db postgresql://postgres:password@127.0.0.1/postgres --ape-filter 62.01Z
```

Start REST API server (based on [PostgREST](http://postgrest.org)):

```
$ docker-compose up -d
```

Urls:

- REST API: http://127.0.0.1:3000/
- Swagger doc: http://127.0.0.1:8080/