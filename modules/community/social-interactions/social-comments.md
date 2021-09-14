
# Social Comments

This represents a comment to a data object within the system. 

- Social posts are data objects. This is the most common object to which comments can be added.
- Besides social posts, there are other objects, which frequently are the target of comments:
    - Marketplace Products
    - Documents
    - Definitions
    - Settings
- However, comments can be added to any data object within the system.

### Important Attributes

- **Data Object** - the data object, being commented.
- **Reply To Comment** - the comment, to which the current comment replies. <br> 
If empty, the comment is a root comment to the data object.<br> 
Note, that the Data Object always points to the root data object, which is being commented (e.g., it does not point to a data object for a comment).
- **Comment Text** - comment contents in clear text.
> Note: It is planned that text will be allowed to contain some mark-down constructs in the future.
- **Creation Time Utc** - automatically set by the server to the time of the initial creation of the comment.
