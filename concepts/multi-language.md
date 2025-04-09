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

## Default Language Configuration
The default language is fundamental to the system's operation from day one. It serves as the base language from which all translations are derived and to which they are returned. Once the default language is set, it is strongly recommended not to change it.

This setting is configured via the “Default language” option, which defines the default language for multilingual fields. For example:
en – English
bg – Bulgarian

You can find the configuration here:
- Desktop Client: Settings > Tools > Setup > Configurations
- Web Client: System > Configurations > Setup > Config

> [!WARNING]
> 
> Due to the architecture of multilingual strings, the system does not keep track of previous language values. If you change the default language after it has been initially set:
> - All existing translations will be lost
> - Current string values will become invalid
> - The instance will require complete retranslation of all fields.

