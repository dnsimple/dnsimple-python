# Change Log

## [1.1.0](https://github.com/onlyhavecans/dnsimple-python/tree/1.1.0) (2018-06-07)
[Full Changelog](https://github.com/onlyhavecans/dnsimple-python/compare/1.0.2...1.1.0)

**Closed issues:**

- update\_record in APIv2 should use PATCH, not PUT [\#34](https://github.com/onlyhavecans/dnsimple-python/issues/34)
- 1.0.1 pip install failing [\#32](https://github.com/onlyhavecans/dnsimple-python/issues/32)

**Merged pull requests:**

- Add methods corresponding to certificates endpoints [\#40](https://github.com/onlyhavecans/dnsimple-python/pull/40) ([DeviateFish](https://github.com/DeviateFish))
- Minor Code Cleanup [\#38](https://github.com/onlyhavecans/dnsimple-python/pull/38) ([onlyhavecans](https://github.com/onlyhavecans))
- fix version import [\#37](https://github.com/onlyhavecans/dnsimple-python/pull/37) ([onlyhavecans](https://github.com/onlyhavecans))
- Move to using tox for local tests [\#36](https://github.com/onlyhavecans/dnsimple-python/pull/36) ([onlyhavecans](https://github.com/onlyhavecans))
- use HTTP PATCH for updating records [\#35](https://github.com/onlyhavecans/dnsimple-python/pull/35) ([dcrosta](https://github.com/dcrosta))

## [1.0.2](https://github.com/onlyhavecans/dnsimple-python/tree/1.0.2) (2018-02-27)
[Full Changelog](https://github.com/onlyhavecans/dnsimple-python/compare/1.0.1...1.0.2)

## [1.0.1](https://github.com/onlyhavecans/dnsimple-python/tree/1.0.1) (2018-02-22)
[Full Changelog](https://github.com/onlyhavecans/dnsimple-python/compare/1.0.0...1.0.1)

**Merged pull requests:**

- Refactor auth to fix basic auth & v2 auth documentation [\#30](https://github.com/onlyhavecans/dnsimple-python/pull/30) ([onlyhavecans](https://github.com/onlyhavecans))

## [1.0.0](https://github.com/onlyhavecans/dnsimple-python/tree/1.0.0) (2018-02-22)
[Full Changelog](https://github.com/onlyhavecans/dnsimple-python/compare/0.3.6...1.0.0)

**Closed issues:**

- Support API v2 [\#26](https://github.com/onlyhavecans/dnsimple-python/issues/26)
- Dosn't work?  [\#25](https://github.com/onlyhavecans/dnsimple-python/issues/25)
- Add to PyPi [\#9](https://github.com/onlyhavecans/dnsimple-python/issues/9)
- dns.check sometimes fail on some domain name [\#5](https://github.com/onlyhavecans/dnsimple-python/issues/5)

**Merged pull requests:**

- Pre-1.0 release tweaks [\#29](https://github.com/onlyhavecans/dnsimple-python/pull/29) ([onlyhavecans](https://github.com/onlyhavecans))
- Support APIv2 [\#27](https://github.com/onlyhavecans/dnsimple-python/pull/27) ([lcd1232](https://github.com/lcd1232))
- Regression tests and fixes for domain token-based authentication [\#24](https://github.com/onlyhavecans/dnsimple-python/pull/24) ([reagent](https://github.com/reagent))
- Fix existing integration tests to prevent regressions [\#23](https://github.com/onlyhavecans/dnsimple-python/pull/23) ([reagent](https://github.com/reagent))
- Remove unnecessary print statement [\#18](https://github.com/onlyhavecans/dnsimple-python/pull/18) ([mdippery](https://github.com/mdippery))

## [0.3.6](https://github.com/onlyhavecans/dnsimple-python/tree/0.3.6) (2016-01-05)
**Closed issues:**

- Failed to reach a server: Unprocessable Entity \(Is this module still functionable?\) [\#12](https://github.com/onlyhavecans/dnsimple-python/issues/12)

**Merged pull requests:**

- Adds shell environment string interpolation to .dnsimple config [\#21](https://github.com/onlyhavecans/dnsimple-python/pull/21) ([pztrick](https://github.com/pztrick))
- fix print function [\#20](https://github.com/onlyhavecans/dnsimple-python/pull/20) ([kevchentw](https://github.com/kevchentw))
- Adds support for Domain Tokens [\#19](https://github.com/onlyhavecans/dnsimple-python/pull/19) ([mjacksonw](https://github.com/mjacksonw))
- Read global configuration file [\#17](https://github.com/onlyhavecans/dnsimple-python/pull/17) ([mdippery](https://github.com/mdippery))
- Fix for issues installing via pip or install.py [\#16](https://github.com/onlyhavecans/dnsimple-python/pull/16) ([drpotato](https://github.com/drpotato))
- fixed typo in `update\_record` [\#15](https://github.com/onlyhavecans/dnsimple-python/pull/15) ([pkaeding](https://github.com/pkaeding))
- Hotfix for failing on username/password auth. [\#14](https://github.com/onlyhavecans/dnsimple-python/pull/14) ([drpotato](https://github.com/drpotato))
- Added support for Python 3, moved to using the 'requests' module for handling RESTful calls, redid string formatting, added unit tests and updated to use DNSimple API v1. [\#13](https://github.com/onlyhavecans/dnsimple-python/pull/13) ([drpotato](https://github.com/drpotato))
- A few changes that enabled pip releases [\#10](https://github.com/onlyhavecans/dnsimple-python/pull/10) ([drcapulet](https://github.com/drcapulet))
- Partial support for the contacts API. [\#8](https://github.com/onlyhavecans/dnsimple-python/pull/8) ([pwnall](https://github.com/pwnall))
- Don't raise from check\(\) under normal operation. [\#7](https://github.com/onlyhavecans/dnsimple-python/pull/7) ([pwnall](https://github.com/pwnall))
- Support using the API sandbox. [\#6](https://github.com/onlyhavecans/dnsimple-python/pull/6) ([pwnall](https://github.com/pwnall))
- Improvements [\#3](https://github.com/onlyhavecans/dnsimple-python/pull/3) ([jmurty](https://github.com/jmurty))
- new methods added [\#2](https://github.com/onlyhavecans/dnsimple-python/pull/2) ([philhagen](https://github.com/philhagen))



\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*