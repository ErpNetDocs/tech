# Rate limits

The rate limits in @@erpnet are a set of limits, related to the requests **per each session** that can be made within a specified period. Rate limiting is used to prevent overloading and ensure fair usage for all users (i.e. sessions).

Exceeding any type of limit will result in an HTTP response `429 - Too Many Requests`.

## Types

"@@erpnet introduces several types of rate limits, each targeting a specific use case. These rate limits are summarized in the following table and described in more detail below.

| Rate limit | Config key | Default value |
| ----------- | ----------- |
| Requests per minute per session | `SessionRpm` | 600 |
| Concurrent requests per session | `SessionConcurrentRequests` | 1 |
| Concurrent transactions per session | `SessionConcurrentTransactions` | 1 |
| Global concurrent requests | `GlobalConcurrentRequests` | 2 |

> [!NOTE]
> 
> Please note that the support for these rate limits may vary across different websites, so you should refer to the documentation of the specific site you are interested in for more information.
> 

### SessionRpm

A session requests per minute (RPM) rate limit restricts the number of API requests that can be made within a single session, measured over a one-minute period.

The default session RPM rate limit is set to 600, allowing up to 600 requests per minute. Exceeding this limit will result in an HTTP response of 429 - Too Many Requests.

### SessionConcurrentRequests

Session concurrent requests is a rate limit that restricts the number of simultaneous API requests within a single session. The default limit is set to 1, allowing only one request at a time during a session. Exceeding this limit will result in an HTTP response of 429 - Too Many Requests until the previous request is completed.

### SessionConcurrentTransactions

Session concurrent transactions is a rate limit that restricts the number of simultaneous API transactions within a session. By default, only one open transaction is allowed at a time during a session. Exceeding this limit will result in an HTTP response of 429 - Too Many Requests until the current transaction is completed.

### GlobalConcurrentRequests

`GlobalConcurrentRequests` is a rate limit that restricts the total number of concurrent API requests across all sessions. The default limit is set to 2, but it can be configured to allow up to the lesser of the number of processor cores or 4 concurrent requests. If this global limit is exceeded, new requests will receive an HTTP response of 429 - Too Many Requests until the number of active requests falls below the threshold.

## Configuring rate limits

The limits above are the default ones. You may specify others in the related web site definition.

![Web-site-settings](./pictures/website-settings.png)


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

> [!NOTE]
> 
> To apply the changes, a restart of the website is required.
>
> This task can be performed by your @@erpnet instance administrator or by accessing the website Instance Manager and navigate to the 'Web Sites' section.
> 
> Тypically, Instance Manager is located at the following address: `https://<your-erpnet-instance>.my.erp.net/manage`
> ![Web-site-restart](./pictures/instance-manager-restart-website.png)