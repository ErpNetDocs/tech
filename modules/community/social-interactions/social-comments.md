---
items: Social-interactions
---

# Social comments
This represents a comment to a data object within the system. 

- Social posts are data objects. This is the most common object to which comments can be added.

- Besides social posts, there are other objects which are frequent targets by comments:

    - Marketplace products
    - Documents
    - Definitions
    - Settings
    
- However, comments can be added to any data object within the system.

#### Important attributes:

- **Data object** - the data object being commented.

- **Reply to comment** - the comment to which the current comment replies. 

If empty, the comment is a root comment to the data object.

Тhe Data object always points to the root data object being commented (it does not point to a data object for a comment).

- **Comment text** - comment contents in clear text.

> [!NОТЕ]
> It is planned that text will be allowed to contain some mark-down constructs in the future.

- **Creation Time Utc** - automatically set by the server to the time of initial creation of the comment.
