---
uid: brat-AISET
items: ActionTypes
---
 
# AISET

| Name             | AISET                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | AISET sets the value of an attribute with the result of an AI prompt. It uses the default AI model to process the prompt. |
| Parameter 1      | Attribute, which should be set.                              |
| Parameter 1 type | Attribute                                                    |
| Parameter 2      | AI Prompt                                                    |
| Parameter 2 type | Constant (string)                                            |
| Parameter 3      | Timeout, ms (optional) Default = 2000 ms.                    |
| Parameter 3 type | Constant (integer)                                           |
| Examples         | See the [Example](#example) section below                    |
| Version          | Introduced in: 24                                            |

## Compatible events chart

AISET is compatible with all events.

| Event type                                                     | Compatibility with AISET                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| Client commit (e.g. [CLIENTCOMMIT](../events/client-commit.md), [AGGREGATECLIENTCOMMIT](../events/aggregate-client-commit.md)) | compatible |
| Client committed (e.g. [CLIENTCOMMITTED](../events/client-committed.md), [AGGREGATECLIENTCOMMITTED](../events/aggregate-client-committed.md)) | compatible |
| Document events - (e.g. [STATECHANGING](../events/statechanging.md), [STATECHANGED](../events/statechanged.md), [VOIDING](../events/voiding.md))| compatible |
| Commit (e.g. [COMMIT](../events/commit.md))                    | compatible                                                   |
| Committed (e.g. [COMMITTED](../events/committed.md))                    | compatible                                                   |
| Front-end (e.g. [CREATENEW](../events/create-new.md), ATTRIBUTECHANGING, ATTRIBUTECHANGED) | compatible |

### Example:

А **[business rule](../index.md)** triggers when a [product name](https://docs.erp.net/model/entities/General.Products.Products.html#name) is changed and generates its abbreviated version (i.e., [Product.ShortName](https://docs.erp.net/model/entities/General.Products.Products.html#shortname)).

| Repository                             |                 |                    |                  |                  |                  |                  |                  |
| -------------------------------------- | --------------- | ------------------ | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| General.Products.Products              |                 |                    |                  |                  |                  |                  |                  |
| **Events**                             |                 |                    |                  |                  |                  |                  |                  |
| Event type                             | Event parameter | Execution priority |                  |                  |                  |                  |                  |
| ATTRIBUTECHANGED                       | Name            | Normal             |                  |                  |                  |                  |                  |
| **Actions**                            |                 |                    |                  |                  |                  |                  |                  |
| Action No                              | Action type     | Parameter1 type    | Parameter1 value | Parameter2 type  | Parameter2 value | Parameter3 type (optional) | Parameter3 value |
| 1                                      | AISET           | Attribute          | ShortName        | Constant         | Just return a 4-symbol abbreviation of this input: {Name}. | Constant | 2000 |

The parameters are as follows:
- Specifies that we'll set a new value in the ShortName attribute.
- Specifies an AI prompt, instructing for the desired result.
- Specifies that there's a timeout of 2000 milliseconds.

## Key points and specific limitations
* The results depend entirely on the AI engine and the specified prompt.
* With vaguer instructions, it's possible to receive different output for the same input.
* If the AI engine doesn't respond within the specified timeout, you will receive an empty string.

-------------
## See more

- **[String interpolation](../../string-interpolation/index.md)**
