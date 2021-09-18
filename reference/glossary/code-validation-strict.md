# CODE Validation (Strict)


The strict CODE validation is stricter than the standard **Code Validation**.

### Discussion
The primary reasons for creating codes are:
- Short visual identification of an entity. <br>
The code does not need to fully describe the entity, just to uniquely identify it.
- Easily type the code in drop-down search fields.
- In case of need, easily write down the code.
- Sort (order) the entities by some logic.

### Allowed Characters
Under strict code validation, the code can contain only (in order of suggested usage):
- Digits
- Minus (-)
- Uppercase letters (the English alphabet only)
- Plus (+)

Specifically, the following symbols are NOT allowed:
- Space ( )
- Dot (.)
- Forward slash (/)
- Back slash (\)
- Lowercase letters

The reason behind the strict limiting of the allowed code symbols is that this helps to concatenate, parse and generally - process the codes with more freedom.

### Length
The default maximum length for CODE attributes is **16 characters**. It is however suggested that codes should be kept as 5 characters or less in length.

### Suggestions
When creating codes, there are some general rules, suggested to be followed:

1. Usage of digits only is highly suggested.<br>
Digits (and minus sign) are universal and language-agnostic. They can be typed on any keyboard (especially numeric keypads), without switching language settings. They are also easier to memorize.

2. It is better to create short, consecutive code, than a long, meaningful code (usually with several parts).

3. Usage of letters is generally not advised.
4. When letters are used, use uppercase English letters.
5. Keep codes short. Preferably 5 characters maximum. <br>
Note: The human eye can read codes up to 5 chars in length directly (look at 78542). Longer codes need more attention to read (784521).
6. For a small (less than 20) number of items, meaningful, letters-only codes might be adequate. For example "ABC", "LIB", etc.
7. When creation of meaningful codes is unavoidable: <br>
        a. You can still use digits only, and keep the code type-able on a numeric keypad.<br>
        b. Separate the parts with a minus sign<br>
        c. Keep the length of each part to less than 5 chars.<br>
        d. Keep the total length to the minimum.<br>
            For example: "01-1234".


