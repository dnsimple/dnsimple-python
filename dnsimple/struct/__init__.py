from dataclasses import dataclass
from dataclasses import field
from dataclasses_json import config
from dataclasses_json import dataclass_json
from typing import Any
from typing import Dict
from typing import List
from typing import Literal
from typing import Union

Date = str


DateTime = str


NullableDate = str


NullableDateTime = str


@dataclass_json
@dataclass
class Error:
    message: str


@dataclass_json
@dataclass
class Pagination:
    current_page: int
    per_page: int
    total_entries: int
    total_pages: int


@dataclass_json
@dataclass
class Account:
    id: int
    email: str
    plan_identifier: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class WebhookAccount:
    id: int
    display: str
    identifier: str


@dataclass_json
@dataclass
class AccountInvitation:
    id: int
    account_id: int
    email: str
    token: str
    invitation_sent_at: "DateTime"
    invitation_accepted_at: "NullableDateTime"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Actor:
    id: int
    identifier: str
    pretty: str


@dataclass_json
@dataclass
class BillingSettings:
    ...


@dataclass_json
@dataclass
class Certificate:
    id: int
    domain_id: int
    contact_id: int
    name: str
    common_name: str
    years: int
    csr: str
    state: Literal[
        "new",
        "purchased",
        "configured",
        "submitted",
        "issued",
        "rejected",
        "refunded",
        "cancelled",
        "requesting",
        "failed",
    ]
    auto_renew: bool
    alternate_names: List[str]
    authority_identifier: Literal["comodo", "rapidssl", "letsencrypt"]
    created_at: "DateTime"
    updated_at: "DateTime"
    expires_at: "DateTime"
    expires_on: "Date"


@dataclass_json
@dataclass
class CertificateDownload:
    server: str
    root: str
    chain: List[str]


@dataclass_json
@dataclass
class CertificatePrivateKey:
    private_key: str


@dataclass_json
@dataclass
class Collaborator:
    id: int
    domain_id: int
    domain_name: str
    user_id: int
    user_email: str
    invitation: bool
    created_at: "DateTime"
    updated_at: "DateTime"
    accepted_at: "DateTime"


@dataclass_json
@dataclass
class Contact:
    id: int
    account_id: int
    label: str
    first_name: str
    last_name: str
    organization_name: str
    job_title: str
    address1: str
    address2: str
    city: str
    state_province: str
    postal_code: str
    country: str
    phone: str
    fax: str
    email: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class DelegationSigner:
    id: int
    domain_id: int
    algorithm: str
    digest: str
    digest_type: str
    keytag: str
    public_key: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Domain:
    id: int
    account_id: int
    registrant_id: int
    name: str
    unicode_name: str
    state: Literal["hosted", "registered", "expired"]
    auto_renew: bool
    private_whois: bool
    expires_at: "NullableDateTime"
    expires_on: "Date"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class DomainCheckResult:
    domain: str
    available: bool
    premium: bool


DomainNameServer = str


@dataclass_json
@dataclass
class DomainPremiumPrice:
    premium_price: str
    action: str


@dataclass_json
@dataclass
class DomainPrices:
    domain: str
    premium: bool
    registration_price: float
    renewal_price: float
    transfer_price: float


@dataclass_json
@dataclass
class DomainRegistration:
    id: int
    domain_id: int
    registrant_id: int
    period: int
    state: Literal["cancelled", "new", "registering", "registered", "failed"]
    auto_renew: bool
    whois_privacy: bool
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class DomainRenewal:
    id: int
    domain_id: int
    period: int
    state: Literal["cancelled", "new", "renewing", "renewed", "failed"]
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class DomainTransfer:
    id: int
    domain_id: int
    registrant_id: int
    state: Literal["cancelled", "new", "transferring", "transferred", "failed"]
    auto_renew: bool
    whois_privacy: bool
    status_description: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class DNSSEC:
    enabled: bool
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class EmailForward:
    id: int
    domain_id: int
    alias_email: str
    destination_email: str
    from_: str = field(metadata=config(field_name="from"))
    to: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class EventAccountAddUser:
    account: "Account"
    user: "User"


@dataclass_json
@dataclass
class EventAccountBillingSettingsUpdate:
    account: "Account"
    billing_settings: "BillingSettings"


@dataclass_json
@dataclass
class EventAccountPaymentDetailsUpdate:
    account: "Account"


@dataclass_json
@dataclass
class EventAccountRemoveUser:
    account: "Account"
    user: "User"


@dataclass_json
@dataclass
class EventAccountUpdate:
    account: "Account"


@dataclass_json
@dataclass
class EventAccountInvitationAccept:
    account: "Account"
    account_invitation: "AccountInvitation"


@dataclass_json
@dataclass
class EventAccountInvitationCreate:
    account: "Account"
    account_invitation: "AccountInvitation"


@dataclass_json
@dataclass
class EventAccountInvitationRemove:
    account: "Account"
    account_invitation: "AccountInvitation"


@dataclass_json
@dataclass
class EventAccountInvitationResend:
    account: "Account"
    account_invitation: "AccountInvitation"


@dataclass_json
@dataclass
class EventCertificateAutoRenewalDisable:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventCertificateAutoRenewalEnable:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventCertificateAutoRenewalFailed:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventCertificateIssue:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventCertificateReissue:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventCertificateRemovePrivateKey:
    certificate: "Certificate"


@dataclass_json
@dataclass
class EventContactCreate:
    contact: "Contact"


@dataclass_json
@dataclass
class EventContactDelete:
    contact: "Contact"


@dataclass_json
@dataclass
class EventContactUpdate:
    contact: "Contact"


@dataclass_json
@dataclass
class EventDNSSECCreate:
    dnssec: "DNSSEC"


@dataclass_json
@dataclass
class EventDNSSECDelete:
    dnssec: "DNSSEC"


@dataclass_json
@dataclass
class EventDNSSECRotationStart:
    delegation_signer_record: "DelegationSigner"
    dnssec: "DNSSEC"


@dataclass_json
@dataclass
class EventDNSSECRotationComplete:
    delegation_signer_record: "DelegationSigner"
    dnssec: "DNSSEC"


@dataclass_json
@dataclass
class EventDomainAutoRenewalDisable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainAutoRenewalEnable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainCreate:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainDelete:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRegisterStarted:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRegister:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRegisterCancelled:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRenewStarted:
    auto: bool
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRenew:
    auto: bool
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainRenewCancelled:
    auto: bool
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainDelegationChange:
    domain: "Domain"
    name_servers: List["NameServer"]


@dataclass_json
@dataclass
class EventDomainRegistrantChangeStarted:
    domain: "Domain"
    registrant: "Contact"


@dataclass_json
@dataclass
class EventDomainRegistrantChange:
    domain: "Domain"
    registrant: "Contact"


@dataclass_json
@dataclass
class EventDomainRegistrantChangeCancelled:
    domain: "Domain"
    registrant: "Contact"


@dataclass_json
@dataclass
class EventDomainResolutionDisable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainResolutionEnable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainTransferStarted:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainTransfer:
    domain: "Domain"


@dataclass_json
@dataclass
class EventDomainTransferCancelled:
    domain: "Domain"


@dataclass_json
@dataclass
class EventEmailForwardCreate:
    email_forward: "EmailForward"


@dataclass_json
@dataclass
class EventEmailForwardDelete:
    email_forward: "EmailForward"


@dataclass_json
@dataclass
class EventEmailForwardUpdate:
    email_forward: "EmailForward"


@dataclass_json
@dataclass
class EventInvoiceCollect:
    invoice: "Invoice"


@dataclass_json
@dataclass
class EventNameServerDeregister:
    name_server: "EventNameServerDeregisterNameServer"


@dataclass_json
@dataclass
class EventNameServerRegister:
    name_server: "EventNameServerRegisterNameServer"


@dataclass_json
@dataclass
class EventOauthApplicationCreate:
    oauth_application: "OauthApplication"


@dataclass_json
@dataclass
class EventOauthApplicationDelete:
    oauth_application: "OauthApplication"


@dataclass_json
@dataclass
class EventOauthApplicationResetClientSecret:
    oauth_application: "OauthApplication"


@dataclass_json
@dataclass
class EventOauthApplicationRevokeAccessTokens:
    oauth_application: "OauthApplication"


@dataclass_json
@dataclass
class EventOauthApplicationUpdate:
    oauth_application: "OauthApplication"


@dataclass_json
@dataclass
class EventPushAccept:
    push: "Push"


@dataclass_json
@dataclass
class EventPushInitiate:
    push: "Push"


@dataclass_json
@dataclass
class EventPushReject:
    push: "Push"


@dataclass_json
@dataclass
class EventRecordCreate:
    zone_record: "ZoneRecord"


@dataclass_json
@dataclass
class EventRecordDelete:
    zone_record: "ZoneRecord"


@dataclass_json
@dataclass
class EventRecordUpdate:
    zone_record: "ZoneRecord"


@dataclass_json
@dataclass
class EventSecondaryDNSCreate:
    configuration: "SecondaryDNS"


@dataclass_json
@dataclass
class EventSecondaryDNSDelete:
    configuration: "SecondaryDNS"


@dataclass_json
@dataclass
class EventSecondaryDNSUpdate:
    configuration: "SecondaryDNS"


@dataclass_json
@dataclass
class EventSubscriptionMigrate:
    subscription: "Subscription"


@dataclass_json
@dataclass
class EventSubscriptionRenew:
    subscription: "Subscription"


@dataclass_json
@dataclass
class EventSubscriptionSubscribe:
    subscription: "Subscription"


@dataclass_json
@dataclass
class EventSubscriptionUnsubscribe:
    subscription: "Subscription"


@dataclass_json
@dataclass
class EventTemplateApply:
    template: "Template"
    zone: "Zone"


@dataclass_json
@dataclass
class EventTemplateCreate:
    template: "Template"


@dataclass_json
@dataclass
class EventTemplateDelete:
    template: "Template"


@dataclass_json
@dataclass
class EventTemplateUpdate:
    template: "Template"


@dataclass_json
@dataclass
class EventTemplateRecordCreate:
    template_record: "TemplateRecord"


@dataclass_json
@dataclass
class EventTemplateRecordDelete:
    template_record: "TemplateRecord"


@dataclass_json
@dataclass
class EventVanityDisable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventVanityEnable:
    domain: "Domain"


@dataclass_json
@dataclass
class EventWebhookCreate:
    webhook: "Webhook"


@dataclass_json
@dataclass
class EventWebhookDelete:
    webhook: "Webhook"


@dataclass_json
@dataclass
class EventWhoisPrivacyDisable:
    domain: "Domain"
    whois_privacy: "WhoisPrivacy"


@dataclass_json
@dataclass
class EventWhoisPrivacyEnable:
    domain: "Domain"
    whois_privacy: "WhoisPrivacy"


@dataclass_json
@dataclass
class EventWhoisPrivacyPurchase:
    domain: "Domain"
    whois_privacy: "WhoisPrivacy"


@dataclass_json
@dataclass
class EventWhoisPrivacyRenew:
    domain: "Domain"
    whois_privacy: "WhoisPrivacy"


@dataclass_json
@dataclass
class EventZoneCreate:
    zone: "Zone"


@dataclass_json
@dataclass
class EventZoneDelete:
    zone: "Zone"


@dataclass_json
@dataclass
class ExtendedAttribute:
    name: str
    description: str
    required: bool
    options: List["ExtendedAttributeOption"]


TradeExtendedAttributes = Dict[str, str]


@dataclass_json
@dataclass
class ExtendedAttributeOption:
    title: str
    value: str
    description: str


@dataclass_json
@dataclass
class Invoice:
    id: int
    invoice_number: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class LetsencryptCertificatePurchase:
    id: int
    certificate_id: int
    state: Literal[
        "new",
        "purchased",
        "configured",
        "submitted",
        "issued",
        "rejected",
        "refunded",
        "cancelled",
        "requesting",
        "failed",
    ]
    auto_renew: bool
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class LetsencryptCertificateRenewal:
    id: int
    old_certificate_id: int
    new_certificate_id: int
    state: Literal["cancelled", "new", "renewing", "renewed", "failed"]
    auto_renew: bool
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class NameServer:
    id: int
    name: str
    ipv4: str
    ipv6: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class OauthApplication:
    id: int
    name: str
    description: str
    homepage_url: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class PrimaryServer:
    id: int
    account_id: int
    name: str
    ip: str
    port: int
    linked_secondary_zones: List[str]
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Push:
    id: int
    domain_id: int
    contact_id: int
    account_id: int
    created_at: "DateTime"
    updated_at: "DateTime"
    accepted_at: "NullableDateTime"


@dataclass_json
@dataclass
class RegistrantChange:
    id: int
    account_id: int
    contact_id: int
    domain_id: int
    state: Literal["new", "pending", "cancelling", "cancelled", "completed"]
    extended_attributes: "TradeExtendedAttributes"
    registry_owner_change: bool
    irt_lock_lifted_by: "Date"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class RegistrantChangeCheck:
    contact_id: int
    domain_id: int
    extended_attributes: List["ExtendedAttribute"]
    registry_owner_change: bool


@dataclass_json
@dataclass
class SecondaryDNS:
    id: int
    zone_id: str
    name_servers: List[str]
    whitelisted_ips: List[str]
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Service:
    id: int
    name: str
    sid: str
    description: str
    setup_description: str
    requires_setup: bool
    default_subdomain: str
    created_at: "DateTime"
    updated_at: "DateTime"
    settings: List["ServiceSetting"]


@dataclass_json
@dataclass
class ServiceSetting:
    name: str
    label: str
    append: str
    description: str
    example: str
    password: bool


@dataclass_json
@dataclass
class Subscription:
    id: int
    plan_name: Literal[
        "Silver",
        "Gold",
        "Silver v1 Yearly",
        "Bronze Yearly",
        "Gold v1 Yearly",
        "No DNS",
        "Professional Yearly",
        "Platinum Yearly",
        "Personal Yearly",
        "Silver Yearly",
        "Business",
        "Bronze Yearly v1",
        "Bronze",
        "Business Yearly",
        "Personal",
        "Basic Reseller Yearly",
        "Expert Reseller",
        "Expert Reseller Yearly",
        "Silver v1",
        "Master Reseller Yearly",
        "Basic Reseller",
        "Gold Yearly",
        "Bronze v1",
        "Professional",
        "Master Reseller",
        "Gold v1",
        "Platinum",
    ]
    state: Literal["new", "subscribing", "subscribed", "unsubscribed", "not_subscribed"]
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Template:
    id: int
    account_id: int
    name: str
    sid: str
    description: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class TemplateRecord:
    id: int
    template_id: int
    name: str
    content: str
    ttl: "TTL"
    priority: int
    type: "TemplateRecordType"
    created_at: "DateTime"
    updated_at: "DateTime"


TemplateRecordType = Literal[
    "A",
    "AAAA",
    "ALIAS",
    "CAA",
    "CNAME",
    "DNSKEY",
    "DS",
    "HINFO",
    "MX",
    "NAPTR",
    "NS",
    "POOL",
    "PTR",
    "SOA",
    "SPF",
    "SRV",
    "SSHFP",
    "TXT",
    "URL",
]


@dataclass_json
@dataclass
class TLD:
    tld: str
    tld_type: "TLDType"
    whois_privacy: bool
    auto_renew_only: bool
    idn: bool
    minimum_registration: int
    registration_enabled: bool
    renewal_enabled: bool
    transfer_enabled: bool
    dnssec_interface_type: Literal["ds", "key"]


TLDType = Literal[1, 2, 3]


TTL = int


@dataclass_json
@dataclass
class User:
    id: int
    email: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class VanityNameServer:
    id: int
    name: str
    ipv4: str
    ipv6: str
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Webhook:
    id: int
    url: str
    suppressed_at: "DateTime"


@dataclass_json
@dataclass
class WebhookPayload:
    name: Literal[
        "account.add_user",
        "account.billing_settings_update",
        "account.payment_details_update",
        "account.remove_user",
        "account.update",
        "account_invitation.accept",
        "account_invitation.create",
        "account_invitation.remove",
        "account_invitation.resend",
        "certificate.auto_renewal_disable",
        "certificate.auto_renewal_enable",
        "certificate.auto_renewal_failed",
        "certificate.issue",
        "certificate.reissue",
        "certificate.remove_private_key",
        "contact.create",
        "contact.update",
        "contact.delete",
        "dnssec.create",
        "dnssec.delete",
        "dnssec.rotation_start",
        "dnssec.rotation_complete",
        "domain.auto_renewal_disable",
        "domain.auto_renewal_enable",
        "domain.create",
        "domain.delete",
        "domain.register:started",
        "domain.register",
        "domain.register:cancelled",
        "domain.renew:started",
        "domain.renew",
        "domain.renew:cancelled",
        "domain.delegation_change",
        "domain.registrant_change:started",
        "domain.registrant_change",
        "domain.registrant_change:cancelled",
        "domain.resolution_disable",
        "domain.resolution_enable",
        "domain.transfer:started",
        "domain.transfer",
        "domain.transfer:cancelled",
        "email_forward.create",
        "email_forward.update",
        "email_forward.delete",
        "name_server.deregister",
        "name_server.register",
        "oauth_application.create",
        "oauth_application.delete",
        "oauth_application.reset_client_secret",
        "oauth_application.revoke_access_tokens",
        "push.accept",
        "push.initiate",
        "push.reject",
        "secondary_dns.create",
        "secondary_dns.delete",
        "secondary_dns.update",
        "subscription.migrate",
        "subscription.subscribe",
        "subscription.unsubscribe",
        "template.create",
        "template.delete",
        "template.update",
        "template_record.create",
        "template_record.delete",
        "vanity.disable",
        "vanity.enable",
        "webhook.create",
        "webhook.delete",
        "whois_privacy.disable",
        "whois_privacy.enable",
        "whois_privacy.purchase",
        "whois_privacy.renew",
        "zone.create",
        "zone.delete",
        "zone_record.create",
        "zone_record.delete",
        "zone_record.update",
    ]
    api_version: Literal["v2"]
    request_identifier: str
    data: Union[
        "EventAccountAddUser",
        "EventAccountBillingSettingsUpdate",
        "EventAccountPaymentDetailsUpdate",
        "EventAccountRemoveUser",
        "EventAccountUpdate",
        "EventAccountInvitationAccept",
        "EventAccountInvitationCreate",
        "EventAccountInvitationRemove",
        "EventAccountInvitationResend",
        "EventCertificateAutoRenewalDisable",
        "EventCertificateAutoRenewalEnable",
        "EventCertificateAutoRenewalFailed",
        "EventCertificateIssue",
        "EventCertificateReissue",
        "EventCertificateRemovePrivateKey",
        "EventContactCreate",
        "EventContactDelete",
        "EventContactUpdate",
        "EventDNSSECCreate",
        "EventDNSSECDelete",
        "EventDNSSECRotationStart",
        "EventDNSSECRotationComplete",
        "EventDomainAutoRenewalDisable",
        "EventDomainAutoRenewalEnable",
        "EventDomainCreate",
        "EventDomainDelete",
        "EventDomainRegisterStarted",
        "EventDomainRegister",
        "EventDomainRegisterCancelled",
        "EventDomainRenewStarted",
        "EventDomainRenew",
        "EventDomainRenewCancelled",
        "EventDomainDelegationChange",
        "EventDomainRegistrantChangeStarted",
        "EventDomainRegistrantChange",
        "EventDomainRegistrantChangeCancelled",
        "EventDomainResolutionDisable",
        "EventDomainResolutionEnable",
        "EventDomainTransferStarted",
        "EventDomainTransfer",
        "EventDomainTransferCancelled",
        "EventEmailForwardCreate",
        "EventEmailForwardDelete",
        "EventEmailForwardUpdate",
        "EventInvoiceCollect",
        "EventNameServerDeregister",
        "EventNameServerRegister",
        "EventOauthApplicationCreate",
        "EventOauthApplicationDelete",
        "EventOauthApplicationUpdate",
        "EventOauthApplicationResetClientSecret",
        "EventOauthApplicationRevokeAccessTokens",
        "EventPushAccept",
        "EventPushInitiate",
        "EventPushReject",
        "EventRecordCreate",
        "EventRecordDelete",
        "EventRecordUpdate",
        "EventSecondaryDNSCreate",
        "EventSecondaryDNSDelete",
        "EventSecondaryDNSUpdate",
        "EventSubscriptionMigrate",
        "EventSubscriptionRenew",
        "EventSubscriptionSubscribe",
        "EventSubscriptionUnsubscribe",
        "EventTemplateApply",
        "EventTemplateCreate",
        "EventTemplateDelete",
        "EventTemplateUpdate",
        "EventTemplateRecordCreate",
        "EventTemplateRecordDelete",
        "EventVanityDisable",
        "EventVanityEnable",
        "EventWebhookCreate",
        "EventWebhookDelete",
        "EventWhoisPrivacyDisable",
        "EventWhoisPrivacyEnable",
        "EventWhoisPrivacyPurchase",
        "EventWhoisPrivacyRenew",
        "EventZoneCreate",
        "EventZoneDelete",
    ]
    account: Any
    actor: Any


@dataclass_json
@dataclass
class WhoisPrivacy:
    id: int
    domain_id: int
    enabled: bool
    expires_on: "Date"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class WhoisPrivacyRenewal:
    id: int
    domain_id: int
    whois_privacy_id: int
    state: str
    enabled: bool
    expires_on: "Date"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class Zone:
    id: int
    account_id: int
    name: str
    reverse: bool
    secondary: bool
    last_transferred_at: "DateTime"
    created_at: "DateTime"
    updated_at: "DateTime"


@dataclass_json
@dataclass
class ZoneFile:
    zone: str


@dataclass_json
@dataclass
class ZoneDistribution:
    distributed: bool


@dataclass_json
@dataclass
class ZoneRecord:
    id: int
    zone_id: str
    parent_id: int
    name: str
    content: str
    ttl: "TTL"
    priority: int
    type: "ZoneRecordType"
    regions: List["ZoneRecordRegion"]
    system_record: bool
    created_at: "DateTime"
    updated_at: "DateTime"


ZoneRecordRegion = Literal[
    "global", "SV1", "ORD", "IAD", "AMS", "TKO", "SYD", "CDG", "FRA"
]


ZoneRecordType = Literal[
    "A",
    "AAAA",
    "ALIAS",
    "CAA",
    "CNAME",
    "DNSKEY",
    "DS",
    "HINFO",
    "MX",
    "NAPTR",
    "NS",
    "POOL",
    "PTR",
    "SOA",
    "SPF",
    "SRV",
    "SSHFP",
    "TXT",
    "URL",
]


@dataclass_json
@dataclass
class WhoamiOutput:
    account: "Account"
    user: "User"


@dataclass_json
@dataclass
class CreateContactInput:
    label: str
    first_name: str
    last_name: str
    address1: str
    address2: str
    city: str
    state_province: str
    postal_code: str
    country: str
    email: str
    phone: str
    fax: str
    organization_name: str
    job_title: str


@dataclass_json
@dataclass
class UpdateContactInput:
    label: str
    first_name: str
    last_name: str
    address1: str
    address2: str
    city: str
    state_province: str
    postal_code: str
    country: str
    email: str
    phone: str
    fax: str
    organization_name: str
    job_title: str


@dataclass_json
@dataclass
class AppliedServicesInput:
    ...


@dataclass_json
@dataclass
class CreatePrimaryServerInput:
    name: str
    ip: str
    port: str


@dataclass_json
@dataclass
class CreateSecondaryZoneInput:
    name: str


@dataclass_json
@dataclass
class UpdateZoneNsRecordsInput:
    ns_names: List[str]
    ns_set_ids: List[int]


@dataclass_json
@dataclass
class CreateZoneRecordInput:
    name: str
    type: "ZoneRecordType"
    content: str
    ttl: "TTL"
    priority: int
    regions: List["ZoneRecordRegion"]
    integrated_zones: List[int]


@dataclass_json
@dataclass
class UpdateZoneRecordInput:
    name: str
    content: str
    ttl: "TTL"
    priority: int
    regions: List["ZoneRecordRegion"]
    integrated_zones: List[int]


@dataclass_json
@dataclass
class DeleteZoneRecordInput:
    integrated_zones: List[int]


@dataclass_json
@dataclass
class CreateTemplateInput:
    sid: str
    name: str
    description: str


@dataclass_json
@dataclass
class UpdateTemplateInput:
    sid: str
    name: str
    description: str


@dataclass_json
@dataclass
class CreateTemplateRecordInput:
    ...


@dataclass_json
@dataclass
class CreateWebhookInput:
    url: str


@dataclass_json
@dataclass
class CreateDomainInput:
    name: str


@dataclass_json
@dataclass
class AddCollaboratorInput:
    email: str


@dataclass_json
@dataclass
class CreateDelegationSignerRecordInput:
    algorithm: str
    digest: str
    digest_type: str
    keytag: str
    public_key: str


@dataclass_json
@dataclass
class CreateEmailForwardInput:
    alias_name: str
    destination_email: str


@dataclass_json
@dataclass
class InitiatePushInput:
    new_account_email: str


@dataclass_json
@dataclass
class AcceptPushInput:
    contact_id: int


@dataclass_json
@dataclass
class PurchaseLetsencryptCertificateInput:
    auto_renew: bool
    name: str
    alternate_names: List[str]
    signature_algorithm: str


@dataclass_json
@dataclass
class PurchaseLetsencryptCertificateRenewalInput:
    auto_renew: bool
    signature_algorithm: str


@dataclass_json
@dataclass
class RegisterDomainInputExtendedAttributes:
    ...


@dataclass_json
@dataclass
class RegisterDomainInput:
    registrant_id: int
    whois_privacy: bool
    auto_renew: bool
    extended_attributes: "RegisterDomainInputExtendedAttributes"
    premium_price: str


@dataclass_json
@dataclass
class TransferDomainInputExtendedAttributes:
    ...


@dataclass_json
@dataclass
class TransferDomainInput:
    registrant_id: int
    auth_code: str
    whois_privacy: bool
    auto_renew: bool
    extended_attributes: "TransferDomainInputExtendedAttributes"
    premium_price: str


@dataclass_json
@dataclass
class RenewDomainInput:
    period: int
    premium_price: str


@dataclass_json
@dataclass
class CreateRegistrantChangeInput:
    domain_id: Union[str, int]
    contact_id: Union[str, int]
    extended_attributes: "TradeExtendedAttributes"


@dataclass_json
@dataclass
class CheckRegistrantChangeInput:
    domain_id: Union[str, int]
    contact_id: Union[str, int]


@dataclass_json
@dataclass
class EventNameServerDeregisterNameServer:
    name: str


@dataclass_json
@dataclass
class EventNameServerRegisterNameServer:
    name: str
