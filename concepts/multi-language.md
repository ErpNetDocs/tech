# Multi-language support
 
Multi-language strings are attributes in @@name support that save data in multiple languages. 

When visualizing the data, the correct version of the string is displayed automatically by the system, depending on the current user language. A product name, for example, can be entered in many languages simultaneously.

> [!NOTE]
> 
> For reports, a report designer can use the **current** user language or a **fixed** language. <br>
> In a Portuguese invoice, it'd be required for all labels and data to be displayed in Portuguese.

## Entering data in multiple languages

The client applications of @@name usually allow the following abilities regarding multi-language strings:

- **Entering** the string in many languages
- **Transliterating** a string from one language to another (or all)
- **Translating** a string from one language to another (or all)

When entering translations, the client application displays a **table** with cells for each translation:

| Language | Value |
| ---- | ----- |
| EN: | Toothpaste |
| DE: | Zahnpasta |

Depending on the client application, translation can sometimes be **automated**. 

Some applications support using an online service like Google Translate to automatically translate a string to other languages. Translation is better suited to **Description** and **Notes** attributes.

## Transliteration of names and addresses from Cyrillic

Transliteration is the process of converting text from one language script to another, based on the phonetic sounds of the original text.
This is particularly useful for names of people, companies, and addresses, allowing local branch offices in Cyrillic-using countries to operate in their native language while maintaining consistency in corporate reports.

For example, "Елена" (in Cyrillic) would be transliterated as "Elena" (in Latin) and vice versa.

When users enter data, they enter it using their current language setting.
If the user does not enter the latin translation, the system automatically generates one, based on transliteration.

## The role of the Default language of the instance

The base's language is crucial for its being and functioning, from day ONE. It is called "Default language" and this is the language from and to which all translations are executed. Once set it is strictly not advisable to be changed.
The switch is a configuration option called "Default language"  - _Defines the default language of multilanguage fields. For example: en - English, bg - Bulgarian._
Can be found in:
 - Dektop  - Settings/Tools/Setup/Configurations
 - WEB client - System/Configurations/Setup/Config
> [!WARNING]
> 
> Due to the way Multilanguage strings work - they do not keep track of the previous language - if you change the Default language of the instance at some point, all translations will be lost, all current strings become invalid.<br>

