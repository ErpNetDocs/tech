---
uid: wst-TABLEAPI
items: Types
---

# Table API

The web site provides Table API to the @@erpnet table model using the [OData (Open Data Protocol)](https://www.odata.org/) standard. Table API allows for data consumption in a RESTful manner and offers external applications the opportunity to interact with the table model.

The primary purpose of the Table API is to allow external BI (Business Intelligence) tools to quickly pull raw data for further analysis.

Table API is secured using [OAuth 2.0](https://oauth.net/2/), which provides an industry-standard for authorization.

## Rate limits

Table API is subject to rate limiting, which means that the number of requests you can make within a given time period is limited. The rate limit policy for this API includes multiple constraints, such as the maximum number of requests per minute, maximum number of concurrent requests, and so on. If you exceed any of these constraints, your requests may be rejected with an error response.

For more information, see the separate topic **[Rate limits](../rate-limits.md)**.

### Applicable rate limits

Below are the rate limiting options supported by Table API:

- **[GlobalConcurrentRequests](../rate-limits.md#globalconcurrentrequests)** - Caps total concurrent API requests across all sessions.

-------------
## See more

- **[Table API docs](https://docs.erp.net/dev/topics/table-api)**
- **[Rate limits](../rate-limits.md)**
