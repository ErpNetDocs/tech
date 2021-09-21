# Identifier Validation

The rules for naming an identifier are:

- An identifier **cannot** be a keyword.
- An identifier **must** begin with a letter or an underscore. The remaining part can contain letters, digits, and underscore symbols.
- Whitespaces and symbols other than letter, digit and underscore are **not** allowed.
- @ is **not** allowed to be used as a prefix.
- Identifiers are **case-sensitive**. That's why getName, GetName and getname represent 3 different identifiers.
 
 
These are **valid** identifiers:

- number;
- doCalculation;
- identifier1;
- *hello*world;

These are **invalid** identifiers:

- hello# - contains symbol other than letter, digit or underscore;
- int - this is a keyword
- hello world - contains whitespace
- 1HelloWorld
- @hello
