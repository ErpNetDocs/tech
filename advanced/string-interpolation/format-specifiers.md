---
uid: format-specifiers
---


# Format specifiers
Format specifiers are used to state the desired format when formatting object values. 
In @@name they can be used, for example, as a second parameter for the calculated attribute operator [FORMATSTRING](https://docs.erp.net/tech/advanced/calculated-attributes/operators/formatstring.html) or in the formatting string (‘:FormatSpecifier’) when referencing domain attributes in the [SENDMAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/sendmail.html) action (‘{DomainAttribute:FormatSpecifier}’). 
There are two main types of format specifiers - standard .Net format specifiers (Numeric, Date - Time,..) and custom format specifiers (Multilanguge string, Custom property). 

## Standard .Net format specifiers
The standard .Net format specifiers are supported.
The list below contains the most frequently used .Net format specifiers. 
For a complete list and more information, please look at the official .Net documentation site.

#### Numeric format specifiers
- 'C', 'c' - abbreviation of Currency. Converts a number to a string that represents a currency amount. 
- Can be used with a precision specifier that indicates the desired number of digits after the decimal point. The decimal symbol separator and the currency symbol depend on the local regional settings. Returns: <br>
123.4656 ('C') → $123.46 <br>
123.4656 ('C3') → $123.466

- 'D', 'd' -abbreviation of Decimal. Converts a number to a string of decimal digits (0-9), prefixed by a minus sign if the number is negative. Can be used with a precision specifier that indicates the desired number of digits after the decimal point. This format is supported only for integral types. Returns:1234 ('D') →  1234 <br>
-1234 ('D6') → -001234

- 'N', 'n' - abbreviation of Number. Converts a number to a string. Can be used with a precision specifier that indicates the desired number of digits after the decimal point. The decimal symbol separator depends on the local regional settings. Returns <br>
123.4656 (N) → 123.47 <br>
123.4656 (N3) → 123.466  

 - 'P', 'p' - abbreviation of Percent. Multiplies a number by 100 and converts it to a string that represents a percentage. The precision specifier indicates the desired number of decimal places. The decimal symbol separator depends on the local regional settings. Returns <br>
           0.488869 (P) → 48.89% <br>
           0.488869 (P3) → 48.887%

#### Date and Time format strings
Standard date and time format specifiers can be used alone (standard date and time format string) or in a combination (custom format string) in order to define the text representation of a date and time value.
A standard date and time format string uses a single format specifier to define the text representation of a date and time value. 
Any date and time format string that contains more than one character, including white space, is interpreted as a custom date and time format string.

#### Standard date and time format strings:
- 'D', 'd' - Short date pattern. The returned format depends on the pattern set for Short date in the local regional settings.  Returns: <br>
           2019-05-10 15:18:39.013 → 10.5.2019
- 'D' - Long date pattern. The returned format depends on the pattern set for Long date in the local regional settings. Returns: <br>
           2019-05-10 15:18:39.013 → 10 May 2019
- 'f' - Full date/time pattern (short time). The returned format depends on the pattern set for Long date and Short time in the local regional settings. Returns: <br>
2019-05-10 15:18:39.013 → 10 May 2019 5:18
- 'F' - Full date/time pattern (long time).. The returned format depends on the pattern set for Long date and Short time in the local regional settings. Returns: <br>
2019-05-10 15:18:39.013 → 10 May 2019 5:18:39
- 'M', 'm' - Month/day pattern. The returned format depends on the current culture set in the local regional settings. Returns: <br>
2019-05-10 15:18:39.013 → May 10
- 'u' - Universal sortable date/time pattern. Returns: <br>
2019-05-10 15:18:39.013 → 2019-05-10 15:18:39Z
- 'U' - Universal full date/time pattern. Returns: <br>
2019-05-10 15:18:39.013 → 10 May 2019 5:18:39

## Custom format strings:
- 'd' - The day of the month, from 1 through 31.
- 'M' - The month, from 1 through 12.
- 'y' - The year, from 0 to 99.
- 'h' - The hour, using a 12-hour clock from 1 to 12.
- 'H' - The hour, using a 24-hour clock from 00 to 23.
- 'm' - The minute, from 0 through 59.
- 's' - The second, from 0 through 59.
- 'f' - The tenths of a second in a date and time value.
- '%' - Defines the following character as a custom 
- '/' - Тhe current's culture date seperator.
- '\' - The escape character.
- 'string', 'string' - Literal string delimiter.

## Examples: 
- 2019-05-10 15:18:39.013 ('dd MM yyyy hh:mm:ss.fff')→ 10 05 2019 03:18:39.013
- 2019-05-10 15:18:39.013 ('yyyy MM dd  hh:mm:ss.fff')→ 2019 05 10  03:18:39.013
- 2019-05-10 15:18:39.013 ('dd M yyyy hh:mm:ss.fff')→ 10 5 2019 03:18
- 2019-05-10 15:18:39.013 ('dd MMM yyyy hh:mm')→ 10 May 2019 03:18
- 2019-05-10 15:18:39.013 ('dd/MM/yyyy hh:mm')→ 10.05.2019 03:18
- 2019-05-10 15:18:39.013 ('dd\/MM\/yyyy hh:mm')→ 10/05/2019 03:18
- 2019-05-10 15:18:39.013 (dd-MM-yyyy hh:mm)→ 10-05-2019 03:18
- 2019-05-10 15:18:39.013 ('dd MM yyyy hh:mm 'h'')→ 10 05 2019 03:18 h

## Custom format specifiers
There are also custom format specifiers that are created especially for @@name. They are different for the different data types and are described below.

## Multilanguge string
- 'C', 'CURRENT' - returns the string of the current value.

- 'D', 'DUMP' - returns the content of the multilanguage string in the format: <br>
EN=<english-string> DE=<german-string>
- 'T', 'TRANSLITERATED' - returns transliteration to the current language.

- format specifiers for a particular language - returns the translation of the specified language. If there is no transliteration set for this language, returns an empty string. 
Note: The format specifiers for a particular language are supported since EnterpriseOne version 2019.1. <br>
Language format specifiers:
     -'EN' - English
     - 'BG' - Bulgarian
     - 'CS' - Czech
     - 'FR' - French
     - 'DE' - German
     - 'EL' - Greek
     - 'HU' - Hungarian
     - 'IT' - Italian
     - 'MK' - Macedonian
     - 'PL' - Polish
     - 'PT' - Portuguese
     - 'RO' - Romanian
     - 'RU' - Russian
     - 'SR' - Serbian
     - 'ES' - Spanish

## Custom property
- 'VD' - abbreviation of Value/Description, returns:
          <Value>: <Description>
- 'V' - abbreviation of Value, returns:
          <Value>
- 'VDI' - abbreviation of Value/Description/Id, returns:
         <Value>: <Description> (<Value-Id>)
- 'D' - abbreviation of Description, returns:
        <Description>
