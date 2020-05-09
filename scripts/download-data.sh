#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

mkdir -p datas/

curl https://files.data.gouv.fr/insee-sirene/2020-04-01-StockUniteLegale_utf8.zip -o datas/2020-04-01-StockUniteLegale_utf8.zip
(
    cd datas
    unzip *.zip
    rm *.zip
)