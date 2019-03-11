# Backend for CAAS project's README

## Getting Dependencies
```
pip install -t lib -r requirements.txt
```


## OpenApi Specification

#### Generating OpenApi config file to ReferralApi
```
python lib/endpoints/endpointscfg.py get_openapi_spec api.ReferralApi api.InstitutionApi --hostname caas-prototype.appspot.com
```

** Output:** *Caasv1openapi.json*

#### Implanting OpenApi file to Google Cloud Endpoints

```
gcloud endpoints services deploy caasv1openapi.json
```

## Deployment

#### Deploying endpoints to Google App Engine
```
gcloud app deploy
```

#### Deploying endpoints to localhost
```
dev_appserver.py ./app.yaml
```

#### Updating indexes on datastore
```
gcloud app deploy index.yaml --version=1 
or 
gcloud datastore indexes create
```