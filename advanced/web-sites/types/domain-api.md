---
uid: wst-DOMAINAPI
items: Types
---

# Domain API

The web site provides Domain API to the @@erpnet domain model using the [OData (Open Data Protocol)](https://www.odata.org/) standard. Domain API allows for the creation and consumption of data, in a RESTful manner and provides an opportunity for external applications to interact with the domain model. 

It enables external applications to access the domain model by querying, filtering, and updating the data through standard HTTP requests. Domain API provides a convenient and standardized way for external applications to interact with the domain model while also ensuring the security of the data being accessed.

Domain API is secured using [OAuth 2.0](https://oauth.net/2/), which provides an industry-standard for authorization.

## Rate limits

The rate limits for the Domain API are a set of limits, related to the requests **per each session** that can be made within a specified period. It's used to prevent overloading the Domain API and ensure fair usage for all users (i.e. sessions).

### Types

ERP.net introduces several types rate limits, each targeting a specific use case. All are summarized in the following table and further described in more detail below:

| Rate limit | Config key | Default value | Error when reached |
| ----------- | ----------- |
| Requests per minute per session | `SessionRpm` | 600 | 429 - Too Many Requests |
| Concurrent requests per session | `SessionConcurrentRequests` | 1 | 429 - Too Many Requests |
| Concurrent transactions per session | `SessionConcurrentTransactions` | 1 | 500 - Internal Server Error |

#### SessionRpm

A session requests per minute rate limit (RPM) is a type of rate limit that restricts the number of API requests made within a single session, measured in minutes. 

The Domain API's session RPM rate limit is set to 600, allowing for up to 600 requests to be made in a one-minute session. Exceeding the limit will result in an HTTP response `429 - Too Many Requests`.

#### SessionConcurrentRequests

Session concurrent requests is a rate limit that restricts the number of concurrent API requests within a single session. The Domain API's limit is 1, allowing only one request at a time during a session. Exceeding the limit will result in an HTTP response `429 - Too Many Requests` until the previous request is completed.

#### SessionConcurrentTransactions

Session concurrent transactions is a rate limit that restricts the number of concurrent API transactions within a session. The Domain API allows only one open transaction at a time during a session. Exceeding the limit will result in an HTTP response `500 - Internal Server Error // You already have an open InMemoryTransaction in this session.` until the previous transaction is open.

### Configuring rate limits

The limits above are the default ones. You may specify others in the related web site definition.

![Web-site-settings](../pictures/website-settings.png)


The rate limits settings are expressed by a JSON object in a specific format. Here's what it looks like as part of a complete web site configuration:

```JSON
{
  "RateLimits": {
    "SessionRpm": 600,
    "SessionConcurrentRequests": 1,
    "SessionConcurrentTransactions": 1
  }
}
```

-------------
## See more

- **[Domain API docs](https://docs.erp.net/dev/domain-api/index.html)**
