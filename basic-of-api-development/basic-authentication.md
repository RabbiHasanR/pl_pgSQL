Cookie:

cookie properties:
sent with every request
cookie scope: domain, path
expires, max-age
same site

cookie types:

session cookie
permanent cookie
httponly cookie
secure cookie
third party cookie
zombie cookie


cookie security:
stealing cookies
cross site request forgery


Session Based  Auth:


JWT:

Json Web Token
Completely Stateless
3 Parts Header, Data, Signature
Signature ecryption can be symmetrical or asymmetrical
symmetrical require same key to create JWT and validate
Asymmetrical private key create JWT, public key validates

pros:
stateless
great of apis
Secure
Carry useful info
Can store info that derive UX
No need for centelized database

Cons:
Sharing secrets in Microservices
Key management
Very tricky to consume correctly
Storage of Refresh tokens
Token Revocation and Control
Insecure implementation
