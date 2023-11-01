---
uid: brat-AIVALIDATE
items: ActionTypes
---
 
# AIVALIDATE

| Name             | AIVALIDATE                                                   |
| ---------------- | ------------------------------------------------------------ |
| Description      | Perform a validation, based on AI prompt. If the validation fails, an exception is thrown. |
| Parameter 1      | The AI prompt used to perform the validation. Usually, the AI prompt would be an interpolated string, interpolating the values, which should be validated in an AI prompt. It should return "true" if the validation is successful. Any other value (or timeout) would mean failure. |
| Parameter 1 type | string - Constant, [Formatted string](../parameter-types/formattedstring.md) or [Interpolate](../parameter-types/interpolate.md) |
| Parameter 2      | The message, which should be provided to the user if the validation fails. The message might include the validated values using an interpolated (formatted) string parameter. |
| Parameter 2 type | string - Constant, [Formatted string](../parameter-types/formattedstring.md) or [Interpolate](../parameter-types/interpolate.md) |
| Parameter 3      | Timeout, ms (optional)                                       |
| Parameter 3 type | Constant (integer) Default = 2000 ms.                        |
| Examples         | See the [Example](#example) section below                    |
| Version          | Introduced in: 24                                            |

## Compatible events chart

AIVALIDATE is compatible with all events.

| Event type                                                     | Compatibility with AIVALIDATE                                     |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| Client commit (e.g. [CLIENTCOMMIT](../events/client-commit.md), [AGGREGATECLIENTCOMMIT](../events/aggregate-client-commit.md)) | compatible |
| Client committed (e.g. [CLIENTCOMMITTED](../events/client-committed.md), [AGGREGATECLIENTCOMMITTED](../events/aggregate-client-committed.md)) | compatible |
| Document events - (e.g. [STATECHANGING](../events/statechanging.md), [STATECHANGED](../events/statechanged.md), [VOIDING](../events/voiding.md))| compatible |
| Commit (e.g. [COMMIT](../events/commit.md))                    | compatible                                                   |
| Committed (e.g. [COMMITTED](../events/committed.md))                    | compatible                                                   |
| Front-end (e.g. [CREATENEW](../events/create-new.md), ATTRIBUTECHANGING, ATTRIBUTECHANGED) | compatible |

### Example:

А **[business rule](../index.md)** FAILS when a [bank account code](https://docs.erp.net/model/entities/General.Contacts.PartyBankAccounts.html#bankaccountcode) is not validated.

| Repository                             |                 |                    |                  |                  |                  |                  |                  |
| -------------------------------------- | --------------- | ------------------ | ---------------- | ---------------- | ---------------- | ---------------- | ---------------- |
| General.Contacts.PartyBankAccounts     |                 |                    |                  |                  |                  |                  |                  |
| **Events**                             |                 |                    |                  |                  |                  |                  |                  |
| Event type                             | Event parameter | Execution priority |                  |                  |                  |                  |                  |
| ATTRIBUTECHANGED                       | BankAccountCode | Normal             |                  |                  |                  |                  |                  |
| **Actions**                            |                 |                    |                  |                  |                  |                  |                  |
| Action No                              | Action type     | Parameter1 type    | Parameter1 value | Parameter2 type  | Parameter2 value | Parameter3 type (optional) | Parameter3 value |
| 1                                      | AIVALIDATE      | Interpolate        | Is '{BankAccountCode}' a valid IBAN?  | Interpolate         | The provided IBAN {BankAccountCode} isn't valid! | Constant | 2000 |

The parameters are as follows:
- Specifies that we're checking if the provided IBAN is valid.
- Specifies the error message to return if the validation fails.
- Specifies that there's a timeout of 2000 milliseconds.

## Key points and specific limitations
* The results depend entirely on the AI engine and the specified prompt.
* With vaguer instructions, it's possible to receive different output for the same input.
* If the AI engine doesn't respond within the specified timeout, you will receive an empty string.

-------------
## See more

- **[String interpolation](../../string-interpolation/index.md)**
