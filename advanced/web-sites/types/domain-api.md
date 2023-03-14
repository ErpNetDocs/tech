---
uid: wst-DOMAINAPI
items: Types
---

# Domain API

The web site provides Domain API to the @@erpnet domain model using the [OData (Open Data Protocol)](https://www.odata.org/) standard. Domain API allows for the creation and consumption of data, in a RESTful manner and provides an opportunity for external applications to interact with the domain model. 

It enables external applications to access the domain model by querying, filtering, and updating the data through standard HTTP requests. Domain API provides a convenient and standardized way for external applications to interact with the domain model while also ensuring the security of the data being accessed.

Domain API is secured using [OAuth 2.0](https://oauth.net/2/), which provides an industry-standard for authorization.

## Rate limits

Domain API is subject to rate limiting, which means that the number of requests you can make within a given time period is limited. The rate limit policy for this API includes multiple constraints, such as the maximum number of requests per minute, maximum number of concurrent requests, and so on. If you exceed any of these constraints, your requests may be rejected with an error response.

For more information, see the separate topic **[Rate limits](../rate-limits.md)**.

-------------
## See more

- **[Domain API docs](https://docs.erp.net/dev/domain-api/index.html)**
- **[Rate limits](../rate-limits.md)**
