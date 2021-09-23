# CODE Validation (Strict)


This code validation is stricter than the standard **Code Validation**.

### Discussion
The primary reasons for creating codes are:
- Short visual identification of an entity. The code does not need to fully describe the entity just to uniquely identify it.
- Easily type the code in dropdown search fields.
- When needed, easily write down the code.
- Sort (order) the entities by different criteria.

### Allowed Characters
Under strict code validation, the code can only contain (in order of suggested usage):
- Digits
- Minus (-)
- Uppercase letters (the English alphabet only)
- Plus (+)

The following symbols are **NOT** allowed:
- Space ( )
- Dot (.)
- Forward slash (/)
- Backslash (\)
- Lowercase letters

The reasons for strict limiting of the code symbols are concatenation, parsing and processing of codes with more freedom.

### Length
The default maximum length for CODE attributes is **16 characters**. It is still recommended that codes be 5 characters or less.

### Suggestions
When creating codes, there are some general rules:

1. Usage of digits is highly suggested.

Digits (and the minus sign) are universal and language-agnostic. They can be typed on any keyboard without switching language settings. They are also easier to memorize.

2. It is better to create short, consecutive code than a long, meaningful code (usually with several parts).

3. Usage of letters is generally not advised.

4. When letters are used, use uppercase English letters.

5. Keep codes short. Preferably 5 characters maximum. 

> [!Note]
> The human eye can immediately read codes up to 5 chars in length (78542). Longer codes take more time (784521).

6. For a small (less than 20) number of items, meaningful, letter-only codes might be adequate. For example "ABC", "LIB", etc.

7. When creation of meaningful codes is unavoidable: 

a. You can still use digits and keep the code type-able on a numeric keypad.<br>
b. Separate the parts with a minus sign<br>
c. Keep the length of each part less than 5 chars.<br>
d. Keep the total length to minimum.<br>

   For example: "01-1234".
