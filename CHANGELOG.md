# Changelog

This project uses [Semantic Versioning 2.0.0](http://semver.org/).

## main

- CHANGED:
  - Rename exceptions `errors` field to `attribute_errors`
  - Added `reason`, `status` and `response` fields to exceptions
  - Updates the exception string serialization format

## 2.6.0

- CHANGED:
  - Exceptions error messages are displayed correctly ([dnsimple/dnsimple-python#340](https://github.com/dnsimple/dnsimple-python/pull/340))
  - Dependency updates

## 2.5.0

- CHANGED:
  - Deprecate Certificate's `contact_id` (dnsimple/dnsimple-python#314)
  - Dependency updates

## 2.4.0

- CHANGED:
  - Dropped support of Python 3.6
  - Dependency updates

## 2.3.1

- CHANGED:
  - Dependency updates

## 2.3.0

- CHANGED:
  - Dependency updates
  - Added support for DS key-data interface (dnsimple/dnsimple-python#210).

- REMOVED:
  - Developer warning in README.md

## 2.2.1

- CHANGED:
  Dependency updates

## 2.2.0

- CHANGED:
  - Feature: Added `registrar.get_domain_prices` to retrieve whether a domain is premium and the prices to register, transfer, and renew. (dnsimple/dnsimple-python#174)
  - Deprecated: get_domain_premium_price, use get_domain_prices instead.
  - Dependency updates

## 2.1.2

- CHANGED:
  Dependencies updates with a security update for urllib3

## 2.1.1

- CHANGED:
  Dependencies update
  Fixed #98

## 2.1.0

- CHANGED: Dependencies update

## 2.0.1

- CHANGED: Dependencies update

## 2.0.0

Adopted public release.
