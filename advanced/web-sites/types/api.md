---
uid: wst-API
items: Types
---

# API

The web site provides an API to the @@erpnet domain model using the [OData (Open Data Protocol)](https://www.odata.org/) standard. This API allows for the creation and consumption of data, in a RESTful manner and provides an opportunity for external applications to interact with the domain model. 

It enables external applications to access the domain model by querying, filtering, and updating the data through standard HTTP requests. The API provides a convenient and standardized way for external applications to interact with the domain model while also ensuring the security of the data being accessed.

The API is secured using [OAuth 2.0](https://oauth.net/2/), which provides an industry-standard for authorization.

Domain API in @@erpnet has its separate documentation, available here:

https://docs.erp.net/dev/domain-api/index.html

## Rate limits

HTTP response code `429 - Too Many Requests` is returned if limits are exceeded.

There're several limiters in the API, including:
- 600 requests per minute per session.
- No concurrent requests in a single session.