# Backend for HR project's README

## Getting Dependencies
```
pip install -t lib -r requirements.txt
```


## OpenApi Specification

#### Generating OpenApi config file to UserApi
```
python lib/endpoints/endpointscfg.py get_openapi_spec api.[UserApi] --hostname hrdashmanagement.appspot.com
```

** Output:** *hrdashboardv1openapi.json*

#### Implanting OpenApi file to Google Cloud Endpoints

```
gcloud endpoints services deploy hrdashboardv1openapi.json
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
