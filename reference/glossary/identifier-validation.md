
# Identifier Validation

The rules for naming an identifier are:
- An identifier can not be a keyword.
- An identifier must begin with a letter or an underscore. The remaining part of the identifier can contain letters, digits and underscore symbols.
- Whitespaces and symbols other than letter, digit and underscore are not allowed.
- @ symbol is not allowed to be used as a prefix.
- Identifiers are case-sensitive. So, getName, GetName and getname represent 3 different identifiers.
 
 
For example: these are valid identifiers:

- number;
- doCalculation;
- identifier1;
- *hello*world;

Invalid identifiers would be:
- hello# - contains symbol other than letter, digit or underscore;
- int - this is a keyword
- hello world - contains whitespace
- 1HelloWorld
- @hello

