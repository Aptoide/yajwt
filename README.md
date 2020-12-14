# yajwt
**yajwt** is Yet Another [JWT wrapper](https://pyjwt.readthedocs.io/en/stable/) for Python.

## Public/private keys
yajwt supports public/private keys management. To accomplish that, one should create a
.JSON file with the following schema:
```json
{
  "team": "testing-user",
  "key": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5T8bGxmc/Wk4p2kC2IOU\nzpLHSQ28bkpP26x9PiQDQsPZMf1bBgZM213bGi0j34jcx6gp/rAFoLmhaFY3PThr\nVgZKBE3elvCxZwAoTrkR+Vpwe6cWF3dEiakiWkiu8blRuZjFEqQJyQLy/ycTA+x7\nRDc1oqKUl7dvsN/AKHTRNmCW7X1fuEHrvqi/4RXBUzmC2HVD3+pXBQH0uJeOqLtQ\nQMf9mZtBM10LwKa9ise/k+Uv0I5X3IUshHGG2WbWEwtvlHCHV/3pF4DuEONqySqN\ni9iAyN1JABtQVt8y5jcDkQv7oeQa9Rwb9wxufAjKcQA4o4Syhe8dAnWHZ/c++zPJ\n5QIDAQAB\n-----END PUBLIC KEY-----\n",
  "payload": {
    "iss": "testing-user",
    "version": "1"
  },
  "algorithm": "RS256",
  "key_type": "public"
}
```

`team` is used to identify .JSON file.

`payload` can be changed according to your specifications, however `iss` is needed to
verify incoming tokens.

`algorithm` can also be changed according to your specifications.

`key_type` can be `public` or `private`.

## Examples

### How to make a request?
```python
keys_path = os.path.join(os.getcwd(), "examples", "keys")
jwt_keys_manager = JwtKeysManager(keys_path)
jwt_requests = JwtRequestsWrapper(jwt_keys_manager, JwtResponseMapper(), TOKEN_TTL)

response = jwt_requests.get("https://example.com", "testing-user")
if response.status == HTTPStatus.OK:
    print(response)
```

### How to validate a request?
```python
keys_path = os.path.join(os.getcwd(), "examples", "keys")
jwt_keys_manager = JwtKeysManager(keys_path)
jwt_validator = JwtRequestsValidator(jwt_keys_manager)

token = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJ0ZXN0aW5nLXVzZXIiLCJ2"
    "ZXJzaW9uIjoiMSIsImV4cCI6MTYwNzU5NDU5OX0.s_fuw0ut1bOOLwKgbPWDtubqO7X6c"
    "te52jtSalHrzoiMYWeWflHXbCFel9VVeLFt6oDN_Yf2xgMx3bx71W3yUQ21jjqwSCYVR5"
    "B6dw-mM15U7v-KJKbjVpBU_KOkkNyqINJAJaB6imB6zz2UG4Du68NKzlPHbCHt4VGVNIQ"
    "-4cz5kbLMkXoZmX0sO3kTqSXpW4KkB9_8IxPNGYwdaqgsVn22Hlkf9-ER8QDsn-e69Bwx"
    "fGnqf-i5J0s3uWmSvboCciE6TIYkiutH8S93rooHLJb96mglmqLu2rcH3fqr9u1hg28jG"
    "er5LRZCK1N2HsnqSGnjc1MOhnKgX5OlrHIbAg"
)
jwt_token = jwt_validator.validate(token)
if jwt_token.valid:
    print(jwt_token.payload)
print(jwt_token)

```
