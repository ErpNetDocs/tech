 # Display and search document and line numbers
 
### 1. Displaying document and line numbers

#### a) The general format for displaying document and line numbers is:

<**DocTypeCode**>**:**<**DocNumber**>**:**<**LineNumber**> - <**DocTypeName**>

For example, let's have the following:

- The document type is ‘Sales order’, with code ‘SO’
- The document number is ‘00503’
- The line number is 120 (the line numbers are integers)

This will be represented as:

**SO:00503:120 - Sales order**
 
 #### b) If we have to display only a document number (without line number), the format is the following:
 
<**DocTypeCode**>**:**<**DocNumber**> - <**DocTypeName**>

Now, let's have the following:

- The document type is ‘Sales order’, with code ‘SO’
- The document number is ‘00503’

This will be represented as:

**SO:00503 - Sales order**

### 2. Sorting lists of documents and line numbers

When a list containing document and line numbers is sorted, the order is the following:

- First, sort lexicographically by "DocTypeCode"
- Then, sort lexicographically by "DocNumber"
- Then, sort numerically by "LineNumber" (if applicable)
 
### 3. Searching through document and line numbers
  
When a user wants to find a document or a specific document line, they enter a search term. The following rules apply:
 
 #### a) Generally, a search is processed in the same format as the display text
 
<**DocTypeSearchTerm**>**:**<**DocNumberSearchTerm**>**:**<**LineNumberSearchTerm**>

For example, searching for ‘SO:00503:120’ will find and match ‘O:00503:120’ and nothing else.

This is a non-wildcard search and is the fastest search. It is usually used when a value is pasted in a user application.

#### b) Some of the search terms might be missing

We can search for ‘SO:00503’ and this will match all lines from ‘SO:00503’, e.g. ‘SO:00503:10’, ‘SO:00503:20’, etc.

> If the search contains only one search term and does not contain colon (':'), it will be performed over the document number!

Searching for '00503' will find 'SO:00503'. But searching for 'SO' will **NOT** match 'SO:00503', because 'SO' would not be found among the document numbers (unless there is a document with the number 'SO').

#### c) Some of the search terms might contain a wildcard symbol (%)

The "DocTypeSearchTerm" and "DocNumberSearchTerm" can contain the wildcard symbol and it will perform a wildcard search. However, the "LineNumberSearchTerm" **cannot** contain wildcard symbol and will not perform a wildcard search.

The system wildcard symbol is '%'. In the user applications, the generally accepted symbol is ' ' (space).

### 4. Examples
 
|System search term|User Application Visualization|Description
|:---|:---|:---
|S%:%503|'S : 503'| • Document types, starting with 'S'.<br> • Document Numbers, finishing with '503'
|SO:%503|'SO: 503'| • Document type with code 'SO'.<br> • Document Numbers, finishing with '503'
|SO:%503:10|'SO: 503:10'| • Document type with code 'SO'.<br> • Document Numbers, finishing with '503'.<br> • Line Number 10 (line numbers do not support wildcard search)
|::10|'::10'| • All lines in all documents, with line number = 10
|SO::10|'SO::10'| • Document type with code 'SO'.<br> • All lines, with line number = 10
|:%503%|': 503 '|• All documents, with numbers, containing '503'.<br> This could be specified simpler, as in the following example:
|%503%|' 503 '|Because there are no colons (':'), the search term is applied to the document number.<br> • All documents, with number, containing '503'.<br> Note: If you want to search by document type only, append a colon at the end of the search string, as in the following example:
|SO:|'SO:'| • All documents (and lines) for document type with code = 'SO'
|SO::|'SO::'|(same as above).<br> • All documents (and lines) for document type with code = 'SO'

 
> When searching in large databases, **DO NOT** put a wildcard symbol **in front** of the document number. Search for '0047858%' instead of '%47858%'. In a user application, search for '0047858' instead of ' 47858'.
>
> The difference in speed might be substantial. Performance tests have shown 0.2 sec for '0047858%', against 120 sec for '%47858%' in a database with 50 million documents.
>
> This recommendation is only for the document number. The document type code can contain wildcard symbols in any position and this does not affect performance.

