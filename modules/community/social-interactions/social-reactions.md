
# Social Reactions

The reactions represent user reactions to social content. They resemble Facebook reactions.

## Important Attributes

- **Data Object** - the root data object. The reaction can be attached to the data object itself, or to a comment to the data object. In any case, the data object contains the root data object, just like the comments.
- **Social Comment** - when not null, contains a comment to the same Data Object to which the reaction is attached.
- **Reaction Type** - one of:
    - LIKE
    - LOVE
    - HAHA
    - WOW
    - SAD
    - ANGRY
- **Creation Time Utc** - automatically set by the server to the time of the initial creation of the reaction.
