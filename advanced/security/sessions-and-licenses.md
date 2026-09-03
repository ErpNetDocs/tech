# Sessions and licenses

@@erpnet is licensed by **concurrent use**. The instance is sold a number of concurrent-session licenses, and a license is taken while people are actually working, not per named user.

This topic explains what takes a license, when it is released, and where to see the current usage.

## What takes a license

A license is occupied by **one user on one device**.

- All the sessions a user opens from the **same device** share one license. Several browser tabs, and an application embedded in the @@webclient, cost one license between them.
- The **same user on a second device**, for example a phone next to the workstation, takes a second license.
- **Two users on one device**, such as a shared terminal where colleagues sign in one after another, take one license each while both sessions are alive.
- A session with **no device** takes a license of its own. Integrations and services that authenticate as an application, without a person signing in, are always in this group.

> [!NOTE]
> The device is the browser profile that performed the sign-in, not the physical machine. Two different browsers on one computer, a private browsing window, and an application with its own built-in browser each count as a separate device.

## When a license is released

A license is held as long as at least one session is using it, and is released when the last of those sessions ends.

| Situation | When the license is freed |
| --- | --- |
| The user stops working | After **20 minutes** without a request (sliding expiration) |
| The user signs out | When the session closes |
| A service session (application authentication) | After **1 hour** at the latest, even if it stays active |

Closing a browser tab does not free a license immediately. The session behind it expires on the usual inactivity timeout.

## Reserved licenses

A database can reserve licenses for named accounts, so those users can always connect even when everyone else has filled the instance.

- The reserved accounts are listed per database, on the application server. Listing an account **twice** reserves **two** licenses for it.
- The guarantee is counted in licenses, not in sessions. A reserved user opening a second window on the same device still uses the one reserved license.
- Beyond its reservation, a reserved account competes for the remaining licenses like everybody else.

For example, with 10 licenses and 2 reserved for two named users, the other 8 are shared. When all 8 are in use, the two reserved users can still sign in, and everyone else waits for a license to free up.

## Where to see the usage

- **Instance Manager** reports the licenses in use on the instance home page and on its Sessions page. The figure comes from the application server itself, so it matches what the licensing rules actually count.
- **Current Sessions**, in the system monitoring views, lists the live sessions with the **Device** they were opened from. Sessions that share a device and a user are the ones sharing a license.
- Active sessions and used licenses are **different numbers**. Seeing more sessions than licenses is normal and means people are working in several windows.

## When the licenses run out

A user who tries to start a session when no license is available is refused with a message asking them to contact the system administrator. Nothing is lost: the person can sign in as soon as a license is released.

Requests to the Domain API and the Table API are answered with `503 Service Unavailable` and a `Retry-After` header, so an integration can wait and repeat the call. See the [developer documentation](https://docs.erp.net/dev/domain-api/data-manipulation/error-handling.html).

If this happens regularly, either sessions are being held by people who are no longer working, or the instance needs more licenses.
