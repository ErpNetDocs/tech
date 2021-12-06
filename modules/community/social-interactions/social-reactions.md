---
items: social-interactions
---

# Social reactions

Social reactions represent user reactions to social content. They resemble Facebook reactions.

#### Important attributes:

- **Data object** - the root data object. A reaction can be attached to the data object itself, or to a comment of the data object. In any case, the data object contains the root data object, just like the comments.

- **Social comment** - when not null, it contains a comment to the same Data Object to which the reaction is attached.

- **Reaction type** - one of:

    - LIKE
    - LOVE
    - HAHA
    - WOW
    - SAD
    - ANGRY
    
- **Creation time Utc** - automatically set by the server to the time of initial creation of the reaction.
