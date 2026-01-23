# Changelog

This project uses [Semantic Versioning 2.0.0](http://semver.org/), the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## 7.0.0 - 2026-01-23

### Removed

- REMOVED: Removed deprecated `get_domain_premium_price`. Use `get_domain_prices` instead. (dnsimple/dnsimple-developer#916)
- Removed deprecated `get_whois_privacy` (dnsimple/dnsimple-developer#919)
- Removed deprecated `renew_whois_privacy` (dnsimple/dnsimple-developer#919)

## 6.1.0 - 2025-09-26

### Added

- Added `Zones.batch_change_records` to make changes to zone records in a batch. (dnsimple/dnsimple-python#477)

## 6.0.0 - 2025-08-20

### Removed

- Removed `email_from` and `email_to` fields in `EmailForward`. Please use `alias_email` and `destination_email` instead.

### Added

- Added `active` to `EmailForward`

### Fixed

- ZoneRecordInput omits empty name when serialized to json (dnsimple/dnsimple-python#451)

## 5.0.0 - 2025-05-14

### Changed

- Dependency updates

### Removed

- `DomainCollaborators` have been removed. Please use our Domain Access Control feature.

## 4.0.0 - 2024-12-12

### Added

- Added `alias_email` and `destination_email` to `EmailForward`
- Add support for python 3.13

### Changed

- Aligned `EmailForwardInput` constructor param names with current endpoint definition

### Deprecated

- Deprecated `email_from` and `email_to` fields in `EmailForward`
- `DomainCollaborators` have been deprecated and will be removed in the next major version. Please use our Domain Access Control feature.

## 3.0.0 - 2024-03-12

### Changed

- Drop support for Python < 3.12
- Add support for Python 3.12

## 2.15.0 - 2024-02-27

### Added

- Added `get_domain_restore`, `restore_domain` APIs to restore domains. (dnsimple/dnsimple-python#447)

## 2.14.0 - 2024-02-06

### Added

- Added `DnsAnalytics.query` to query and pull data from the DNS Analytics API endpoint (dnsimple/dnsimple-python#445)

## 2.13.0 - 2023-12-13

### Added

- Added `secondary`, `last_transferred_at`, `active` to `Zone` (dnsimple/dnsimple-python#441)

## 2.12.0 - 2023-11-03

### Added

- Added `billing.list_charges` to list charges for the account [learn more](https://developer.dnsimple.com/v2/billing-charges/). (dnsimple/dnsimple-python#437)

## 2.11.0 - 2023-09-06

### Added

- Added `get_domain_transfer_lock`, `enable_domain_transfer_lock`, and `disable_domain_transfer_lock` APIs to manage domain transfer locks. (dnsimple/dnsimple-python#435)
- Added `list_registrant_changes`, `create_registrant_change`, `check_registrant_change`, `get_registrant_change`, and `delete_registrant_change` APIs to manage registrant changes. (dnsimple/dnsimple-python#433)

## 2.10.1 - 2023-08-10

### Added

- Added `Zones.activate_dns` to activate DNS services (resolution) for a zone. (dnsimple/dnsimple-python#432)
- Added `Zones.deactivate_dns` to deactivate DNS services (resolution) for a zone. (dnsimple/dnsimple-python#432)

## 2.10.0 - 2023-03-03

### Added

- Added support for `get_domain_registration` and `get_domain_renewal` Registrar APIs.

## 2.9.0 - 2023-03-01

### Added

- Added support for `signature_algorithm` in Let's Encrypt APIs

### Changed

- Dependency updates

## 2.8.0 - 2022-11-22

### Changed

- Drop py as a dependency ([dnsimple/dnsimple-python#388](https://github.com/dnsimple/dnsimple-python/pull/388))
- Dependency updates

## 2.7.0 - 2022-09-20

### Changed

- Deprecate exceptions `errors` attr and move to `attribute_errors`
- Added `reason`, `status` and `response` fields to exceptions
- Updates the exception string serialization format

## 2.6.0 - 2022-08-17

### Changed

- Exceptions error messages are displayed correctly ([dnsimple/dnsimple-python#340](https://github.com/dnsimple/dnsimple-python/pull/340))
- Dependency updates

## 2.5.0 - 2022-07-20

### Changed

- Dependency updates

### Deprecated

- Deprecated Certificate's `contact_id` (dnsimple/dnsimple-python#314)

## 2.4.0 - 2022-02-16

### Changed

- Dropped support of Python 3.6
- Dependency updates

## 2.3.1 - 2022-02-10

### Changed

- Dependency updates

## 2.3.0 - 2021-10-29

### Added

- Added support for DS key-data interface (dnsimple/dnsimple-python#210).

### Changed

- Dependency updates

### Removed

- Developer warning in README.md

## 2.2.1 - 2021-07-01

### Changed

- Dependency updates

## 2.2.0 - 2021-05-19

### Added

- Added `registrar.get_domain_prices` to retrieve whether a domain is premium and the prices to register, transfer, and renew. (dnsimple/dnsimple-python#174)

### Changed

- Dependency updates

### Deprecated

- Deprecated `get_domain_premium_price`, use `get_domain_prices` instead.

## 2.1.2 - 2021-05-10

### Security

- Dependencies updates with a security update for urllib3

## 2.1.1 - 2021-02-24

### Changed

- Dependencies update

### Fixed

- Fixed #98

## 2.1.0 - 2020-12-31

### Changed

- Dependencies update

## 2.0.1 - 2020-11-12

### Changed

- Dependencies update

## 2.0.0 - 2020-09-28

Adopted public release.
