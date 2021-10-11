# Creating a duplicate document and a new document from current


The current article describes the principles and some specifics in creating a duplicate of an existing document. Also different usages of the algorithm are presented.
 
## Basic principles

Creating a duplicate of a given document is actually creating a new document which contains identical **business** data with the original one, meaning that in the duplicate  all ***substantial*** and ***meaningful*** data is copied from the original document and there is an exception for some technical data (such as internal identification numbers - Primary Keys, IDs of reference links between different parts of one document and more).

This is the common algorithm used when creating a duplicate of a given document:

1. A new document is created with the same Document type and in its headers the ***substantial*** data from the original document is copied:

a. the ***substantial*** data from the original document header is copied to the new document header;

b. in each of the specific headers in the new document only the***substantial*** data from the corresponding specific headers of the original documents is copied.

2. If the original document has rows - for each row a new row is created in the duplicate document and the ***substantial*** data from the original row is copied to the new one.

3. If the original document has *rows of the rows* (i.e. a document row has dependent records in different part of the document) - for each main row from the original document its duplicate row in the new document is fixed and for each of its sub-rows of the main row a new sub-row in the duplicate document is created and from the original sub-row only the ***substantial*** data is copied.

4. If the original document has *rows of the rows of the rows*, the same procedure is applied until the original document structure is covered.

Thus, the new document - the duplicate - must contain the same number of records (headers, rows, rows of rows etc.) as the original document and these records must have the same structure as they are in the original document.

As document rows are considered not only the standard rows which most of the documents have, but also the document properties and the **Additional amounts**. Also, if the specific document header has its own properties, then they are considered document rows. The records in ‘Document amount referenced documents’ panel are considered *rows of rows* (rows of the additional amounts). Also, the records in ‘Document line amounts’ are considered as such (they are rows of the standard document rows). Currently, the attached files are not copied when creating a duplicate of a document.

