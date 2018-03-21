# Make DNSimple available directly from module for backwards-compatibility
try:
    from dnsimple import DNSimple, DNSimpleException, DNSimpleAuthException
except ImportError:
    from dnsimple.dnsimple import DNSimple, DNSimpleException, DNSimpleAuthException

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
