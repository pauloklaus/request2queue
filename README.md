# Request To Queue

Receive a payload from http request, validate and publish in a queue.

## Process

1. POST in */vulnerabilities* via API Gateway: *vuln-api-[env])*
2. Start Lambda function to data validation: *vuln-api-entry-[env]*
3. Publish in SNS: *vuln-[env]*

Valid values to [env]: staging, production

## Test

```sh
make test
```

## Build container image

```sh
make build
```

## Run locally inside a container

```sh
make run
```
