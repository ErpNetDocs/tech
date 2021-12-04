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

## Transliteration

Transliteration is the process of **translating** one language version of a string to another, based on the sounding of the string. It works great for people and company names and addresses. It allows branch offices to work in their local language, and reports can still be shown in corporate language.

For example, the Russian "Иван" would be transliterated in English as "Ivan".

Transliteration works in **two** ways: manual and automatic.

### Manual transliteration

This transliteration is actually automatic, but initiated manually while editing the different language versions of a multi-language string. The client application usually provides a function button which transliterates the current language version to other languages.

### Automatic transliteration

Automatic transliteration occurs when the system needs to display multi-language strings in a **different** language, but the translation isn't saved in the database.

For example, an employee working in a branch office in Russia enters "Иван" as a first name. 

The database saves **only** the Russian version. 

Another employee at a British location requests to see the name of the same person. 

The system would **automatically** transliterate the string and display it as "Ivan".

> [!NOTE]
> 
> Transliteration works normally from Latin to Cyrillic.
