# Document Flow

### Description

The sequence of documents in a process forms a document flow. Just a sequence of documents is a rare occurrence, so documents in a process are more likely to be in a hierarchy.

Documents in @@name often have **sub-documents**. Most of the time, they are [automatically generated](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/document-generation.md) or created by some [fulfillment function](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/document-fulfillment.md). However, manually entering a sub-document is also allowed and sometimes encouraged.

Documents, their sub-documents, the sub-documents of the sub-documents, etc. form the sequence (or hierarchy). The document flow design, therefore, is one of the most important aspects of implementing @@name for a target enterprise.

The designed is achieved with the help of specific document routes for each Document Type.
