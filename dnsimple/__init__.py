# Make DNSimple available directly from module for backwards-compatibility
try:
    from dnsimple import DNSimple, DNSimpleException, DNSimpleAuthException
except ImportError:
    from dnsimple.dnsimple import DNSimple, DNSimpleException, DNSimpleAuthException
