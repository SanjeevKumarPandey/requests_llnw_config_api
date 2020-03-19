# Config HTTP API

## Installation
```
pip install -i https://test.pypi.org/simple/ requests-ll-config-api==1.0.0
```

## Initiation
```
api = HttpStreamingApi('http-api-fqdn', 'api-username', 'api-key')
```

## Usage
```
api.<api-endpoint>(<params1>,<params2>...)
```