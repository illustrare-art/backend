#!/usr/bin/env bash
docker build -t api-server .
docker tag api-server eu.gcr.io/illustrare-53f71/api-server
docker push eu.gcr.io/illustrare-53f71/api-server
gcloud builds submit --tag eu.gcr.io/illustrare-53f71/api-server
gcloud run deploy api-server --image eu.gcr.io/illustrare-53f71/api-server --region=europe-central2 --port=8000 --allow-unauthenticated --min-instances=1 --max-instances=5