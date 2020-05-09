#!/usr/bin/env python3
import sys
import csv
from urllib.parse import urlparse

from tqdm import tqdm
import psycopg2
import click

def parse_db_uri(uri):
    result = urlparse(uri)
    return "dbname='%s' user='%s' host='%s' password='%s'" % (
        result.path[1:],
        result.username,
        result.hostname,
        result.password
    )

@click.command()
@click.option('--csv', 'csv_filename', help='csv filename')
@click.option('--db', default='postgresql://postgres:password@127.0.0.1/postgres', help='db uri')
@click.option('--ape-filter', default='62.01Z', help='API code filter')
def import_csv_to_postgres(csv_filename, db, ape_filter):
    try:
        conn = psycopg2.connect(parse_db_uri(db))
    except:
        print("I am unable to connect to the database")
        sys.exit(1)

    cur = conn.cursor()
    with open(csv_filename, 'r') as input_csvfile:
        reader = csv.DictReader(input_csvfile)

        for row in tqdm(reader, ncols=10, unit='rows'):
            if (
                (row['etatAdministratifUniteLegale'] == 'A') and
                (row['activitePrincipaleUniteLegale'] == ape_filter)
            ):
                # Convert empty string to none
                for k, v in row.items():
                    if v == '':
                        row[k] = None


                cur.execute("""
                    INSERT INTO
                        public.stock_unite_legale
                    (
                        activite_principale_unite_legale,
                        annee_categorie_entreprise,
                        annee_effectifs_unite_legale,
                        caractere_employeur_unite_legale,
                        categorie_entreprise,
                        categorie_juridique_unite_legale,
                        date_creation_unite_legale,
                        date_debut,
                        date_dernier_traitement_unite_legale,
                        denomination_unite_legale,
                        denomination_usuelle1_unite_legale,
                        denomination_usuelle2_unite_legale,
                        denomination_usuelle3_unite_legale,
                        economie_sociale_solidaire_unite_legale,
                        etat_administratif_unite_legale,
                        identifiant_association_unite_legale,
                        nic_siege_unite_legale,
                        nombre_periodes_unite_legale,
                        nomenclature_activite_principale_unite_legale,
                        nom_unite_legale,
                        nom_usage_unite_legale,
                        prenom1_unite_legale,
                        prenom2_unite_legale,
                        prenom3_unite_legale,
                        prenom4_unite_legale,
                        prenom_usuel_unite_legale,
                        pseudonyme_unite_legale,
                        sexe_unite_legale,
                        sigle_unite_legale,
                        siren,
                        statut_diffusion_unite_legale,
                        tranche_effectifs_unite_legale,
                        unite_purgee_unite_legale
                    )
                    VALUES (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                    """,
                    (
                        row['activitePrincipaleUniteLegale'],
                        row['anneeCategorieEntreprise'],
                        row['anneeEffectifsUniteLegale'],
                        row['caractereEmployeurUniteLegale'],
                        row['categorieEntreprise'],
                        row['categorieJuridiqueUniteLegale'],
                        row['dateCreationUniteLegale'],
                        row['dateDebut'],
                        row['dateDernierTraitementUniteLegale'],
                        row['denominationUniteLegale'],
                        row['denominationUsuelle1UniteLegale'],
                        row['denominationUsuelle2UniteLegale'],
                        row['denominationUsuelle3UniteLegale'],
                        row['economieSocialeSolidaireUniteLegale'],
                        row['etatAdministratifUniteLegale'],
                        row['identifiantAssociationUniteLegale'],
                        row['nicSiegeUniteLegale'],
                        row['nombrePeriodesUniteLegale'],
                        row['nomenclatureActivitePrincipaleUniteLegale'],
                        row['nomUniteLegale'],
                        row['nomUsageUniteLegale'],
                        row['prenom1UniteLegale'],
                        row['prenom2UniteLegale'],
                        row['prenom3UniteLegale'],
                        row['prenom4UniteLegale'],
                        row['prenomUsuelUniteLegale'],
                        row['pseudonymeUniteLegale'],
                        row['sexeUniteLegale'],
                        row['sigleUniteLegale'],
                        row['siren'],
                        row['statutDiffusionUniteLegale'],
                        row['trancheEffectifsUniteLegale'],
                        row['unitePurgeeUniteLegale']
                    )
                )
                conn.commit()

if __name__ == '__main__':
    import_csv_to_postgres()