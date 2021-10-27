# Document flow

## Description

The sequence of documents in a process forms a document flow. Just a sequence of documents is a rare occurrence, so documents in a process are more likely to be in a hierarchy.

Documents in @@name often have **sub-documents**. Most of the time, they are [automatically generated](https://docs.erp.net/tech/advanced/documents/generation.html) or created by some [fulfillment function](https://docs.erp.net/tech/advanced/documents/fulfillment.html). However, manually entering a sub-document is also allowed and sometimes encouraged.

Documents, their sub-documents, the sub-documents of the sub-documents, etc. **form** a sequence, or hierarchy. The document flow design, therefore, is one of the most important aspects of implementing @@name for a target enterprise.

The designed is achieved with the help of specific document routes built for each document type.

Temporary

[!list folder="." file="." exclude=deterministic*]
