# generated by datamodel-codegen:
#   filename:  bom-1.3.schema.json
#   timestamp: 2022-08-02T21:03:56+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, EmailStr, Field, constr

from . import spdx


class BomFormat(Enum):
    CycloneDX = 'CycloneDX'


class OrganizationalContact(BaseModel):
    name: Optional[str] = Field(
        None,
        description='The name of a contact',
        examples=['Contact name'],
        title='Name',
    )
    email: Optional[str] = Field(
        None,
        description='The email address of the contact.',
        examples=['firstname.lastname@example.com'],
        title='Email Address',
    )
    phone: Optional[str] = Field(
        None,
        description='The phone number of the contact.',
        examples=['800-555-1212'],
        title='Phone',
    )


class Type(Enum):
    application = 'application'
    framework = 'framework'
    library = 'library'
    container = 'container'
    operating_system = 'operating-system'
    device = 'device'
    firmware = 'firmware'
    file = 'file'


class Scope(Enum):
    required = 'required'
    optional = 'optional'
    excluded = 'excluded'


class Encoding(Enum):
    base64 = 'base64'


class Attachment(BaseModel):
    contentType: Optional[str] = Field(
        'text/plain',
        description='Specifies the content type of the text. Defaults to text/plain if not specified.',
        title='Content-Type',
    )
    encoding: Optional[Encoding] = Field(
        None,
        description='Specifies the optional encoding the text is represented in.',
        title='Encoding',
    )
    content: str = Field(
        ..., description='The attachment data', title='Attachment Text'
    )


class HashAlg(Enum):
    MD5 = 'MD5'
    SHA_1 = 'SHA-1'
    SHA_256 = 'SHA-256'
    SHA_384 = 'SHA-384'
    SHA_512 = 'SHA-512'
    SHA3_256 = 'SHA3-256'
    SHA3_384 = 'SHA3-384'
    SHA3_512 = 'SHA3-512'
    BLAKE2b_256 = 'BLAKE2b-256'
    BLAKE2b_384 = 'BLAKE2b-384'
    BLAKE2b_512 = 'BLAKE2b-512'
    BLAKE3 = 'BLAKE3'


class HashContent(BaseModel):
    __root__: constr(
        regex=r'^([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}|[a-fA-F0-9]{96}|[a-fA-F0-9]{128})$'
    ) = Field(
        ..., examples=['3942447fac867ae5cdb3229b658f4d48'], title='Hash Content (value)'
    )


class Type1(Enum):
    unofficial = 'unofficial'
    monkey = 'monkey'
    backport = 'backport'
    cherry_pick = 'cherry-pick'


class Diff(BaseModel):
    text: Optional[Attachment] = Field(
        None, description='Specifies the optional text of the diff', title='Diff text'
    )
    url: Optional[str] = Field(
        None, description='Specifies the URL to the diff', title='URL'
    )


class Type2(Enum):
    defect = 'defect'
    enhancement = 'enhancement'
    security = 'security'


class Source(BaseModel):
    name: Optional[str] = Field(
        None,
        description="The name of the source. For example 'National Vulnerability Database', 'NVD', and 'Apache'",
        title='Name',
    )
    url: Optional[str] = Field(
        None,
        description='The url of the issue documentation as provided by the source',
        title='URL',
    )


class Issue(BaseModel):
    type: Type2 = Field(..., description='Specifies the type of issue', title='Type')
    id: Optional[str] = Field(
        None,
        description='The identifier of the issue assigned by the source of the issue',
        title='ID',
    )
    name: Optional[str] = Field(None, description='The name of the issue', title='Name')
    description: Optional[str] = Field(
        None, description='A description of the issue', title='Description'
    )
    source: Optional[Source] = Field(
        None,
        description='The source of the issue where it is documented',
        title='Source',
    )
    references: Optional[List[str]] = Field(
        None,
        description="A collection of URL's for reference. Multiple URLs are allowed.",
        examples=['https://example.com'],
        title='References',
    )


class IdentifiableAction(BaseModel):
    timestamp: Optional[datetime] = Field(
        None,
        description='The timestamp in which the action occurred',
        title='Timestamp',
    )
    name: Optional[str] = Field(
        None,
        description='The name of the individual who performed the action',
        title='Name',
    )
    email: Optional[EmailStr] = Field(
        None,
        description='The email address of the individual who performed the action',
        title='E-mail',
    )


class Type3(Enum):
    vcs = 'vcs'
    issue_tracker = 'issue-tracker'
    website = 'website'
    advisories = 'advisories'
    bom = 'bom'
    mailing_list = 'mailing-list'
    social = 'social'
    chat = 'chat'
    documentation = 'documentation'
    support = 'support'
    distribution = 'distribution'
    license = 'license'
    build_meta = 'build-meta'
    build_system = 'build-system'
    other = 'other'


class Dependency(BaseModel):
    ref: str = Field(
        ...,
        description='References a component by the components bom-ref attribute',
        title='Reference',
    )
    dependsOn: Optional[List[str]] = Field(
        None,
        description='The bom-ref identifiers of the components that are dependencies of this dependency object.',
        title='Depends On',
        
    )


class DataFlow(Enum):
    inbound = 'inbound'
    outbound = 'outbound'
    bi_directional = 'bi-directional'
    unknown = 'unknown'


class Copyright(BaseModel):
    text: str = Field(..., title='Copyright Text')


class AggregateType(Enum):
    complete = 'complete'
    incomplete = 'incomplete'
    incomplete_first_party_only = 'incomplete_first_party_only'
    incomplete_third_party_only = 'incomplete_third_party_only'
    unknown = 'unknown'
    not_specified = 'not_specified'


class Property(BaseModel):
    name: Optional[str] = Field(
        None,
        description='The name of the property. Duplicate names are allowed, each potentially having a different value.',
        title='Name',
    )
    value: Optional[str] = Field(
        None, description='The value of the property.', title='Value'
    )


class OrganizationalEntity(BaseModel):
    name: Optional[str] = Field(
        None,
        description='The name of the organization',
        examples=['Example Inc.'],
        title='Name',
    )
    url: Optional[List[str]] = Field(
        None,
        description='The URL of the organization. Multiple URLs are allowed.',
        examples=['https://example.com'],
        title='URL',
    )
    contact: Optional[List[OrganizationalContact]] = Field(
        None,
        description='A contact at the organization. Multiple contacts are allowed.',
        title='Contact',
    )


class Swid(BaseModel):
    tagId: str = Field(
        ..., description='Maps to the tagId of a SoftwareIdentity.', title='Tag ID'
    )
    name: str = Field(
        ..., description='Maps to the name of a SoftwareIdentity.', title='Name'
    )
    version: Optional[str] = Field(
        '0.0', description='Maps to the version of a SoftwareIdentity.', title='Version'
    )
    tagVersion: Optional[int] = Field(
        0,
        description='Maps to the tagVersion of a SoftwareIdentity.',
        title='Tag Version',
    )
    patch: Optional[bool] = Field(
        False, description='Maps to the patch of a SoftwareIdentity.', title='Patch'
    )
    text: Optional[Attachment] = Field(
        None,
        description='Specifies the metadata and content of the SWID tag.',
        title='Attachment text',
    )
    url: Optional[str] = Field(
        None, description='The URL to the SWID file.', title='URL'
    )


class Hash(BaseModel):
    alg: HashAlg
    content: HashContent


class License(BaseModel):
    id: Optional[spdx.Schema] = Field(
        None,
        description='A valid SPDX license ID',
        examples=['Apache-2.0'],
        title='License ID (SPDX)',
    )
    name: Optional[str] = Field(
        None,
        description='If SPDX does not define the license used, this field may be used to provide the license name',
        examples=['Acme Software License'],
        title='License Name',
    )
    text: Optional[Attachment] = Field(
        None,
        description='An optional way to include the textual content of a license.',
        title='License text',
    )
    url: Optional[str] = Field(
        None,
        description="The URL to the license file. If specified, a 'license' externalReference should also be specified for completeness",
        examples=['https://www.apache.org/licenses/LICENSE-2.0.txt'],
        title='License URL',
    )


class License1(BaseModel):
    __root__: Union[License, Any, Any] = Field(..., title='License Object')


class LicenseChoice1(BaseModel):
    license: Optional[License1] = None
    expression: Optional[str] = Field(
        None,
        examples=[
            'Apache-2.0 AND (MIT OR GPL-2.0-only)',
            'GPL-3.0-only WITH Classpath-exception-2.0',
        ],
        title='SPDX License Expression',
    )


class LicenseChoice(BaseModel):
    __root__: Union[LicenseChoice1, Any, Any] = Field(..., title='License(s)')


class Commit(BaseModel):
    uid: Optional[str] = Field(
        None,
        description='A unique identifier of the commit. This may be version control specific. For example, Subversion uses revision numbers whereas git uses commit hashes.',
        title='UID',
    )
    url: Optional[str] = Field(
        None,
        description='The URL to the commit. This URL will typically point to a commit in a version control system.',
        title='URL',
    )
    author: Optional[IdentifiableAction] = Field(
        None,
        description='The author who created the changes in the commit',
        title='Author',
    )
    committer: Optional[IdentifiableAction] = Field(
        None,
        description='The person who committed or pushed the commit',
        title='Committer',
    )
    message: Optional[str] = Field(
        None,
        description='The text description of the contents of the commit',
        title='Message',
    )


class Patch(BaseModel):
    type: Type1 = Field(
        ...,
        description='Specifies the purpose for the patch including the resolution of defects, security issues, or new behavior or functionality',
        title='Type',
    )
    diff: Optional[Diff] = Field(
        None,
        description='The patch file (or diff) that show changes. Refer to https://en.wikipedia.org/wiki/Diff',
        title='Diff',
    )
    resolves: Optional[List[Issue]] = Field(
        None, description='A collection of issues the patch resolves', title='Resolves'
    )


class ExternalReference(BaseModel):
    url: str = Field(..., description='The URL to the external reference', title='URL')
    comment: Optional[str] = Field(
        None,
        description='An optional comment describing the external reference',
        title='Comment',
    )
    type: Type3 = Field(
        ...,
        description='Specifies the type of external reference. There are built-in types to describe common references. If a type does not exist for the reference being referred to, use the "other" type.',
        title='Type',
    )
    hashes: Optional[List[Hash]] = Field(
        None,
        description='The hashes of the external reference (if applicable).',
        title='Hashes',
    )


class DataClassification(BaseModel):
    flow: DataFlow
    classification: str


class ComponentEvidence(BaseModel):
    licenses: Optional[List[LicenseChoice]] = Field(None, title='Component License(s)')
    copyright: Optional[List[Copyright]] = Field(None, title='Copyright')


class Compositions(BaseModel):
    aggregate: AggregateType = Field(
        ...,
        description='Specifies an aggregate type that describe how complete a relationship is.',
        title='Aggregate',
    )
    assemblies: Optional[List[str]] = Field(
        None,
        description='The bom-ref identifiers of the components or services being described. Assemblies refer to nested relationships whereby a constituent part may include other constituent parts. References do not cascade to child parts. References are explicit for the specified constituent part only.',
        title='BOM references',
        
    )
    dependencies: Optional[List[str]] = Field(
        None,
        description='The bom-ref identifiers of the components or services being described. Dependencies refer to a relationship whereby an independent constituent part requires another independent constituent part. References do not cascade to transitive dependencies. References are explicit for the specified dependency only.',
        title='BOM references',
        
    )


class Tool(BaseModel):
    vendor: Optional[str] = Field(
        None,
        description='The date and time (timestamp) when the document was created.',
        title='Tool Vendor',
    )
    name: Optional[str] = Field(
        None,
        description='The date and time (timestamp) when the document was created.',
        title='Tool Name',
    )
    version: Optional[str] = Field(
        None,
        description='The date and time (timestamp) when the document was created.',
        title='Tool Version',
    )
    hashes: Optional[List[Hash]] = Field(
        None, description='The hashes of the tool (if applicable).', title='Hashes'
    )


class Service(BaseModel):
    bom_ref: Optional[str] = Field(
        None,
        alias='bom-ref',
        description='An optional identifier which can be used to reference the service elsewhere in the BOM. Every bom-ref should be unique.',
        title='BOM Reference',
    )
    provider: Optional[OrganizationalEntity] = Field(
        None,
        description='The organization that provides the service.',
        title='Provider',
    )
    group: Optional[str] = Field(
        None,
        description='The grouping name, namespace, or identifier. This will often be a shortened, single name of the company or project that produced the service or domain name. Whitespace and special characters should be avoided.',
        examples=['com.acme'],
        title='Service Group',
    )
    name: str = Field(
        ...,
        description='The name of the service. This will often be a shortened, single name of the service.',
        examples=['ticker-service'],
        title='Service Name',
    )
    version: Optional[str] = Field(
        None,
        description='The service version.',
        examples=['1.0.0'],
        title='Service Version',
    )
    description: Optional[str] = Field(
        None,
        description='Specifies a description for the service',
        title='Service Description',
    )
    endpoints: Optional[List[str]] = Field(
        None,
        description='The endpoint URIs of the service. Multiple endpoints are allowed.',
        examples=['https://example.com/api/v1/ticker'],
        title='Endpoints',
    )
    authenticated: Optional[bool] = Field(
        None,
        description='A boolean value indicating if the service requires authentication. A value of true indicates the service requires authentication prior to use. A value of false indicates the service does not require authentication.',
        title='Authentication Required',
    )
    x_trust_boundary: Optional[bool] = Field(
        None,
        alias='x-trust-boundary',
        description='A boolean value indicating if use of the service crosses a trust zone or boundary. A value of true indicates that by using the service, a trust boundary is crossed. A value of false indicates that by using the service, a trust boundary is not crossed.',
        title='Crosses Trust Boundary',
    )
    data: Optional[List[DataClassification]] = Field(
        None,
        description='Specifies the data classification.',
        title='Data Classification',
    )
    licenses: Optional[List[LicenseChoice]] = Field(None, title='Component License(s)')
    externalReferences: Optional[List[ExternalReference]] = Field(
        None, title='External References'
    )
    services: Optional[List[Service]] = Field(None, title='Services')
    properties: Optional[List[Property]] = Field(
        None,
        description='Provides the ability to document properties in a name-value store. This provides flexibility to include data not officially supported in the standard without having to use additional namespaces or create extensions. Unlike key-value stores, properties support duplicate names, each potentially having different values.',
        title='Properties',
    )


class CyclonedxSoftwareBillOfMaterialSpecification(BaseModel):
    bomFormat: BomFormat = Field(
        ...,
        description='Specifies the format of the BOM. This helps to identify the file as CycloneDX since BOMs do not have a filename convention nor does JSON schema support namespaces.',
        title='BOM Format',
    )
    specVersion: str = Field(
        ...,
        description='The version of the CycloneDX specification a BOM is written to (starting at version 1.2)',
        examples=['1.3'],
        title='CycloneDX Specification Version',
    )
    serialNumber: Optional[
        constr(
            regex=r'^urn:uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        )
    ] = Field(
        None,
        description="Every BOM generated should have a unique serial number, even if the contents of the BOM being generated have not changed over time. The process or tool responsible for creating the BOM should create random UUID's for every BOM generated.",
        examples=['urn:uuid:3e671687-395b-41f5-a30f-a58921a69b79'],
        title='BOM Serial Number',
    )
    version: int = Field(
        ...,
        description="The version allows component publishers/authors to make changes to existing BOMs to update various aspects of the document such as description or licenses. When a system is presented with multiple BOMs for the same component, the system should use the most recent version of the BOM. The default version is '1' and should be incremented for each version of the BOM that is published. Each version of a component should have a unique BOM and if no changes are made to the BOMs, then each BOM will have a version of '1'.",
        examples=[1],
        title='BOM Version',
    )
    metadata: Optional[Metadata] = Field(
        None,
        description='Provides additional information about a BOM.',
        title='BOM Metadata',
    )
    components: Optional[List[Component]] = Field(
        None, title='Components', 
    )
    services: Optional[List[Service]] = Field(None, title='Services', ) 
    externalReferences: Optional[List[ExternalReference]] = Field(
        None,
        description='External references provide a way to document systems, sites, and information that may be relevant but which are not included with the BOM.',
        title='External References',
    )
    dependencies: Optional[List[Dependency]] = Field(
        None,
        description='Provides the ability to document dependency relationships.',
        title='Dependencies',
        
    )
    compositions: Optional[List[Compositions]] = Field(
        None,
        description='Compositions describe constituent parts (including components, services, and dependency relationships) and their completeness.',
        title='Compositions',
        
    )


class Metadata(BaseModel):
    timestamp: Optional[datetime] = Field(
        None,
        description='The date and time (timestamp) when the document was created.',
        title='Timestamp',
    )
    tools: Optional[List[Tool]] = Field(
        None,
        description='The tool(s) used in the creation of the BOM.',
        title='Creation Tools',
    )
    authors: Optional[List[OrganizationalContact]] = Field(
        None,
        description='The person(s) who created the BOM. Authors are common in BOMs created through manual processes. BOMs created through automated means may not have authors.',
        title='Authors',
    )
    component: Optional[Component] = Field(
        None, description='The component that the BOM describes.', title='Component'
    )
    manufacture: Optional[OrganizationalEntity] = Field(
        None,
        description='The organization that manufactured the component that the BOM describes.',
        title='Manufacture',
    )
    supplier: Optional[OrganizationalEntity] = Field(
        None,
        description=' The organization that supplied the component that the BOM describes. The supplier may often be the manufacturer, but may also be a distributor or repackager.',
        title='Supplier',
    )
    licenses: Optional[List[LicenseChoice]] = Field(None, title='BOM License(s)')
    properties: Optional[List[Property]] = Field(
        None,
        description='Provides the ability to document properties in a name-value store. This provides flexibility to include data not officially supported in the standard without having to use additional namespaces or create extensions. Unlike key-value stores, properties support duplicate names, each potentially having different values.',
        title='Properties',
    )


class Pedigree(BaseModel):
    ancestors: Optional[List[Component]] = Field(
        None,
        description='Describes zero or more components in which a component is derived from. This is commonly used to describe forks from existing projects where the forked version contains a ancestor node containing the original component it was forked from. For example, Component A is the original component. Component B is the component being used and documented in the BOM. However, Component B contains a pedigree node with a single ancestor documenting Component A - the original component from which Component B is derived from.',
        title='Ancestors',
    )
    descendants: Optional[List[Component]] = Field(
        None,
        description='Descendants are the exact opposite of ancestors. This provides a way to document all forks (and their forks) of an original or root component.',
        title='Descendants',
    )
    variants: Optional[List[Component]] = Field(
        None,
        description='Variants describe relations where the relationship between the components are not known. For example, if Component A contains nearly identical code to Component B. They are both related, but it is unclear if one is derived from the other, or if they share a common ancestor.',
        title='Variants',
    )
    commits: Optional[List[Commit]] = Field(
        None,
        description='A list of zero or more commits which provide a trail describing how the component deviates from an ancestor, descendant, or variant.',
        title='Commits',
    )
    patches: Optional[List[Patch]] = Field(
        None,
        description='>A list of zero or more patches describing how the component deviates from an ancestor, descendant, or variant. Patches may be complimentary to commits or may be used in place of commits.',
        title='Patches',
    )
    notes: Optional[str] = Field(
        None,
        description='Notes, observations, and other non-structured commentary describing the components pedigree.',
        title='Notes',
    )


class Component(BaseModel):
    type: Type = Field(
        ...,
        description='Specifies the type of component. For software components, classify as application if no more specific appropriate classification is available or cannot be determined for the component.',
        examples=['library'],
        title='Component Type',
    )
    mime_type: Optional[constr(regex=r'^[-+a-z0-9.]+/[-+a-z0-9.]+$')] = Field(
        None,
        alias='mime-type',
        description='The optional mime-type of the component. When used on file components, the mime-type can provide additional context about the kind of file being represented such as an image, font, or executable. Some library or framework components may also have an associated mime-type.',
        examples=['image/jpeg'],
        title='Mime-Type',
    )
    bom_ref: Optional[str] = Field(
        None,
        alias='bom-ref',
        description='An optional identifier which can be used to reference the component elsewhere in the BOM. Every bom-ref should be unique.',
        title='BOM Reference',
    )
    supplier: Optional[OrganizationalEntity] = Field(
        None,
        description=' The organization that supplied the component. The supplier may often be the manufacturer, but may also be a distributor or repackager.',
        title='Component Supplier',
    )
    author: Optional[str] = Field(
        None,
        description='The person(s) or organization(s) that authored the component',
        examples=['Acme Inc'],
        title='Component Author',
    )
    publisher: Optional[str] = Field(
        None,
        description='The person(s) or organization(s) that published the component',
        examples=['Acme Inc'],
        title='Component Publisher',
    )
    group: Optional[str] = Field(
        None,
        description='The grouping name or identifier. This will often be a shortened, single name of the company or project that produced the component, or the source package or domain name. Whitespace and special characters should be avoided. Examples include: apache, org.apache.commons, and apache.org.',
        examples=['com.acme'],
        title='Component Group',
    )
    name: str = Field(
        ...,
        description='The name of the component. This will often be a shortened, single name of the component. Examples: commons-lang3 and jquery',
        examples=['tomcat-catalina'],
        title='Component Name',
    )
    version: str = Field(
        ...,
        description='The component version. The version should ideally comply with semantic versioning but is not enforced.',
        examples=['9.0.14'],
        title='Component Version',
    )
    description: Optional[str] = Field(
        None,
        description='Specifies a description for the component',
        title='Component Description',
    )
    scope: Optional[Scope] = Field(
        'required',
        description="Specifies the scope of the component. If scope is not specified, 'required' scope should be assumed by the consumer of the BOM",
        title='Component Scope',
    )
    hashes: Optional[List[Hash]] = Field(None, title='Component Hashes')
    licenses: Optional[List[LicenseChoice]] = Field(None, title='Component License(s)')
    copyright: Optional[str] = Field(
        None,
        description='An optional copyright notice informing users of the underlying claims to copyright ownership in a published work.',
        examples=['Acme Inc'],
        title='Component Copyright',
    )
    cpe: Optional[str] = Field(
        None,
        description='DEPRECATED - DO NOT USE. This will be removed in a future version. Specifies a well-formed CPE name. See https://nvd.nist.gov/products/cpe',
        examples=['cpe:2.3:a:acme:component_framework:-:*:*:*:*:*:*:*'],
        title='Component Common Platform Enumeration (CPE)',
    )
    purl: Optional[str] = Field(
        None,
        examples=['pkg:maven/com.acme/tomcat-catalina@9.0.14?packaging=jar'],
        title='Component Package URL (purl)',
    )
    swid: Optional[Swid] = Field(
        None,
        description='Specifies metadata and content for ISO-IEC 19770-2 Software Identification (SWID) Tags.',
        title='SWID Tag',
    )
    modified: Optional[bool] = Field(
        None,
        description='DEPRECATED - DO NOT USE. This will be removed in a future version. Use the pedigree element instead to supply information on exactly how the component was modified. A boolean value indicating is the component has been modified from the original. A value of true indicates the component is a derivative of the original. A value of false indicates the component has not been modified from the original.',
        title='Component Modified From Original',
    )
    pedigree: Optional[Pedigree] = Field(
        None,
        description='Component pedigree is a way to document complex supply chain scenarios where components are created, distributed, modified, redistributed, combined with other components, etc. Pedigree supports viewing this complex chain from the beginning, the end, or anywhere in the middle. It also provides a way to document variants where the exact relation may not be known.',
        title='Component Pedigree',
    )
    externalReferences: Optional[List[ExternalReference]] = Field(
        None, title='External References'
    )
    components: Optional[List[Component]] = Field(None, title='Components')
    evidence: Optional[ComponentEvidence] = Field(
        None,
        description='Provides the ability to document evidence collected through various forms of extraction or analysis.',
        title='Evidence',
    )
    properties: Optional[List[Property]] = Field(
        None,
        description='Provides the ability to document properties in a name-value store. This provides flexibility to include data not officially supported in the standard without having to use additional namespaces or create extensions. Unlike key-value stores, properties support duplicate names, each potentially having different values.',
        title='Properties',
    )


Service.update_forward_refs()
CyclonedxSoftwareBillOfMaterialSpecification.update_forward_refs()
Metadata.update_forward_refs()
Pedigree.update_forward_refs()
