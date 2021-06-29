---
uid: brat-SETLANGUAGEVALUE
items: ActionTypes
---

# SETLANGUAGEVALUE (in implementation)

The platform supports multi language attributes, for example Product  Name. This gives the user the opportunity to enter the product name in  more than one language - let's say - in English and in German. 

The [Calculated Attributes](https://olddocs.erp.net/tech/calculated-attributes-35586101.html) operators cannot operate with multi-language string attributes. When  such operation is required, the multi-language attribute is cast to  string and then it is used by the calculated attribute operators. The [CAST](https://olddocs.erp.net/tech/cast-40145742.html) of the multi-language string returns the current language translation  and not all translations. So if there is a calculated attribute which  returns the first 10 symbols of the product name, it would:

1. cast the product name to string (which would cut only the current language translation);
2. return the first 10 symbols of the string from p.1. 

And then if we set up a rule which sets (via [SETVALUE](https://olddocs.erp.net/tech/setvalue-41146590.html)) this value in the product name, the rest of the translations are lost. This is because [SETVALUE](https://olddocs.erp.net/tech/setvalue-41146590.html) explicitly sets the value where specified. And as we do not specify all translations and just one of them, the rest of the translations are set as null - so they are lost.

This is the reason behind the current action SETLANGUAGEVALUE.

## Syntax

The SETLANGUAGEVALUE action may receive 2 or 3 input parameters:

1. Parameter 1 - an attribute which holds multi-language string;
2. Parameter 2 - currently, the second parameter may be deliver as an attribute or a constant. This parameter says what would be the new value of the  attribute from Parameter 1.
3. Parameter 3 is delivered as a  constant. If necessary, this parameter is used to specify the language  in which the new value (parameter 2) is set as a translation. This  parameter is optional. If it is null - the action sets the new value into the current language translation.

## Example

If there is a product in the database with the following name:

- in English: "abcdefg"
- in German: "higklm"

And if a user business rule is activated which does the following action:

- SETLANGUAGE ATTRIB: ProductName CONST: "qwerty"

If this rule is started when the current language in German, then after the rule is executed, the product name would be:

- in English: "abcdefg"
- in German: "qwerty"

If the action is defined as follows:

- SETLANGUAGE ATTRIB: ProductName CONST: "qwerty" CONST: en

And again - the current language is German - then after the rule execution, the product name would be:

- in English: "qwerty"
- in German: "higklm"
