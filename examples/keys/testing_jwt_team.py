from yajwt.entities.jwt_key import JwtKey, JwtKeyType
from yajwt.entities.jwt_team import JwtTeam

TESTING_KEYS = {"testing-user": JwtTeam(
    private_key=JwtKey("testing-user",
                      "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA5T8bGxmc/Wk4p2kC2IOUzpLHSQ28bkpP26x9PiQDQsPZMf1b\nBgZM213bGi0j34jcx6gp/rAFoLmhaFY3PThrVgZKBE3elvCxZwAoTrkR+Vpwe6cW\nF3dEiakiWkiu8blRuZjFEqQJyQLy/ycTA+x7RDc1oqKUl7dvsN/AKHTRNmCW7X1f\nuEHrvqi/4RXBUzmC2HVD3+pXBQH0uJeOqLtQQMf9mZtBM10LwKa9ise/k+Uv0I5X\n3IUshHGG2WbWEwtvlHCHV/3pF4DuEONqySqNi9iAyN1JABtQVt8y5jcDkQv7oeQa\n9Rwb9wxufAjKcQA4o4Syhe8dAnWHZ/c++zPJ5QIDAQABAoIBAC2IeEDMuJLYyGjw\nAaGxmOfi3XRUJx4c4nm2a/Xgv0kOj2BPeznaHH/hx3gOiTaH/5oke5rbqXKADGAl\n57jgMOmYPDFYqiJ+0i2sKVVhiwFlBjx5NnkYtmNFVc5q61yVu3bKsjH+pPbpAAzP\n3QYFfYJSGPQhqLPtumB+QLOIaFmNO5AVUbUriF0d/PpurCdnxtDNyqE1c1M6YSTr\nSZj3mvJee68nY/nsQUUr/bHl0uzaz8rPotdef9j8G/PXK1q13rbhkuOoVCF6q+Gp\nxe82wmSZYLrQbj4cZm5EyxMU5xMsK6ga441VDJamGRST6UHVw3SYPOmVkT+01rtU\nMdAPrmECgYEA9FEMITDFsuGMd/h/Q6bKDQeUabGd0djvGnevQaryQl2gtmTI7JnN\nfyIbl63ppknnW6F8XSA3JniKQLIZHCmb0Q6aaovd9IQACXtL8hKGToi+HEN8hZhh\nOFnskSZoS0ciYgxYbcMYIncUqyPJSdo9GD8GentgP2HtxzWziaOMKOkCgYEA8DWR\nmZNwE8yQXvMTt1qpv2Wa1KePv/E3pDQxvswBV3ruhPJn84n/+rliIEKNpXCA/gWp\n5BlmU8ds2cqm5AU4cjL+un/LZKjsnpCQVymZTLFpn3U/i5m07i70nIU4nxMd1nds\n4qobiWgAG2X+w1yqrN0sW0mKbKMa2SZjJwepO50CgYAouj4IZmX+jOTqtu0YLPyv\nsVzHRcmmSsCJK/x2OPYLpCn/Xcu0zWrZT6lD3sT9aIJ93uypZY5sBlodsNLIxBLq\nhcGuE0Tb1wlei0Q8xWPIQblXYtSmPKGwUCVEiR+HtQMBT0eKfKRQUoOKh/utKQlY\nOmFtF5YS2tNVixkzz6S0yQKBgFjYd3IGRn4MO5ni7nfy4LYaLppZH6Iu5hWl+IBJ\nlHV20qH5xtkdQcDKsLCd7SYz5oIONjhX7LEwIeKsQe40wBv9IJp6ihBBKsO7VKfo\nivsC475G76oCwBkY5QC/haHQwEiDA5MSt/yqqt93ajN4IuitJareGIT2DwgiWqok\n+0NBAoGBANb4aAJnpoDRvb4l8DEGHzS7PykxgUB0TdPXp1JChh5EFOotX7CrlwAK\na633jJTEKGjj78aEyW0HUPvOI/UgAS26GuJurdOlSvy8IVszEPT4qioV4amtr94+\nEUvnkI9sz7EBWO+Nsy3iFoWFaOjWcvqpE3rraj0umZViPOJnf6hW\n-----END RSA PRIVATE KEY-----\n",
                      {"iss": "testing-user", "version": "1"},
                      "RS256",
                      JwtKeyType.PRIVATE_KEY),
    public_key=JwtKey("testing-user",
                       "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5T8bGxmc/Wk4p2kC2IOU\nzpLHSQ28bkpP26x9PiQDQsPZMf1bBgZM213bGi0j34jcx6gp/rAFoLmhaFY3PThr\nVgZKBE3elvCxZwAoTrkR+Vpwe6cWF3dEiakiWkiu8blRuZjFEqQJyQLy/ycTA+x7\nRDc1oqKUl7dvsN/AKHTRNmCW7X1fuEHrvqi/4RXBUzmC2HVD3+pXBQH0uJeOqLtQ\nQMf9mZtBM10LwKa9ise/k+Uv0I5X3IUshHGG2WbWEwtvlHCHV/3pF4DuEONqySqN\ni9iAyN1JABtQVt8y5jcDkQv7oeQa9Rwb9wxufAjKcQA4o4Syhe8dAnWHZ/c++zPJ\n5QIDAQAB\n-----END PUBLIC KEY-----\n",
                       {"iss": "testing-user", "version": "1"},
                       "RS256",
                       JwtKeyType.PUBLIC_KEY))}
