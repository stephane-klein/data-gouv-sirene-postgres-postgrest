SET client_min_messages = error;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;

DROP TABLE IF EXISTS public.stock_unite_legale CASCADE;



CREATE TABLE public.stock_unite_legale (
    id                                             UUID PRIMARY KEY DEFAULT uuid_generate_v4() NOT NULL,
    activite_principale_unite_legale               VARCHAR,
    annee_categorie_entreprise                     INTEGER,
    annee_effectifs_unite_legale                   INTEGER,
    caractere_employeur_unite_legale               VARCHAR,
    categorie_entreprise                           VARCHAR,
    categorie_juridique_unite_legale               VARCHAR,
    date_creation_unite_legale                     DATE,
    date_debut                                     DATE,
    date_dernier_traitement_unite_legale           DATE,
    denomination_unite_legale                      VARCHAR,
    denomination_usuelle1_unite_legale             VARCHAR,
    denomination_usuelle2_unite_legale             VARCHAR,
    denomination_usuelle3_unite_legale             VARCHAR,
    economie_sociale_solidaire_unite_legale        VARCHAR,
    etat_administratif_unite_legale                VARCHAR,
    identifiant_association_unite_legale           VARCHAR,
    nic_siege_unite_legale                         VARCHAR,
    nombre_periodes_unite_legale                   INTEGER,
    nomenclature_activite_principale_unite_legale  VARCHAR,
    nom_unite_legale                               VARCHAR,
    nom_usage_unite_legale                         VARCHAR,
    prenom1_unite_legale                           VARCHAR,
    prenom2_unite_legale                           VARCHAR,
    prenom3_unite_legale                           VARCHAR,
    prenom4_unite_legale                           VARCHAR,
    prenom_usuel_unite_legale                      VARCHAR,
    pseudonyme_unite_legale                        VARCHAR,
    sexe_unite_legale                              VARCHAR,
    sigle_unite_legale                             VARCHAR,
    siren                                          VARCHAR,
    statut_diffusion_unite_legale                  VARCHAR,
    tranche_effectifs_unite_legale                 VARCHAR,
    unite_purgee_unite_legale                      VARCHAR
);

SET client_min_messages = INFO;
