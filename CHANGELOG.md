# Changelog

This project uses [Semantic Versioning 2.0.0](http://semver.org/).

## main

## 2.13.0

ENHANCEMENTS:

- NEW: Added `secondary`, `last_transferred_at`, `active` to `Zone` (dnsimple/dnsimple-python#441)

## 2.12.0

FEATURES:

- NEW: Added `billing.list_charges` to list charges for the account [learn more](https://developer.dnsimple.com/v2/billing-charges/). (dnsimple/dnsimple-python#437)

## 2.11.0

FEATURES:

- NEW: Added `get_domain_transfer_lock`, `enable_domain_transfer_lock`, and `disable_domain_transfer_lock` APIs to manage domain transfer locks. (dnsimple/dnsimple-python#435)
- NEW: Added `list_registrant_changes`, `create_registrant_change`, `check_registrant_change`, `get_registrant_change`, and `delete_registrant_change` APIs to manage registrant changes. (dnsimple/dnsimple-python#433)

## 2.10.1

FEATURES:

- NEW: Added `Zones.activate_dns` to activate DNS services (resolution) for a zone. (dnsimple/dnsimple-python#432)
- NEW: Added `Zones.deactivate_dns` to deactivate DNS services (resolution) for a zone. (dnsimple/dnsimple-python#432)

## 2.10.0

- NEW:
  - Added support for get_domain_registration and get_domain_renewal Registrar APIs.

## 2.9.0

- NEW:
  - Added support for `signature_algorithm` in Let's Encrypt APIs
- CHANGED:
  - Dependency updates

## 2.8.0

- CHANGED:
  - Drop py as a dependency ([dnsimple/dnsimple-python#388](https://github.com/dnsimple/dnsimple-python/pull/388))
  - Dependency updates

## 2.7.0

- CHANGED:
  - Deprecate exceptions `errors` attr and move to `attribute_errors`
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
