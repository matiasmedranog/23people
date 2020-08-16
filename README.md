# 23People API

## Apigee
Currently the app uses Apigee as a proxy to handle metrics and security, to access the API prefer the command:

```curl
curl http://matiasmedrano94-eval-prod.apigee.net/23people
```

## Kubernetes
Use [cmake](https://cmake.org/install/) to run the following commands:

**NOTE**: *It requires Kubernetes credentials previusly setted to use [Helm](https://helm.sh/docs/intro/install/)*
```make
make install
```

Build local image
```make
make build
```

Push (updates) to Dockerhub
```make
make tag && make push 
```

## Local Installation

Use [docker-comppose](https://docs.docker.com/compose/install/) to install and run locally.

```bash
docker-compose up
```

## API Usage

User creation:
```curl
curl -X POST -H "Content-Type: application/json" 0.0.0.0:5000/api/v1/people -d '{"name":"Matias", "last_name":"Medrano", "age":26, "picture_url":"htttp://example.com/matias"}'
```
Get all users:
```curl
curl -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people
```
Get one users:
```curl
curl -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id}
```
Update user:
```curl
curl -X PUT -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id} -d '{"name":"Ignacio", "last_name":"Medrano", "age":22, "picture_url":"htttp://example.com/ignacio"}'
```
Delete user:
```curl
curl -X DELETE -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id}
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
