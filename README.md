# 23People API

## Installation

Use [docker-comppose](https://docs.docker.com/compose/install/) to install and run locally.

```bash
docker-compose up
```

## Usage

User creation:
```bash
curl -X POST -H "Content-Type: application/json" 0.0.0.0:5000/api/v1/people -d '{"name":"Matias", "last_name":"Medrano", "age":26, "picture_url":"htttp://example.com/matias"}'
```
Get all users:
```bash
curl -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people
```
Get one users:
```bash
curl -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id}
```
Update user:
```bash
curl -X PUT -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id} -d '{"name":"Ignacio", "last_name":"Medrano", "age":22, "picture_url":"htttp://example.com/ignacio"}'
```
Delete user:
```bash
curl -X DELETE -H "Content-Type: application/json"   0.0.0.0:5000/api/v1/people/{id}
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
