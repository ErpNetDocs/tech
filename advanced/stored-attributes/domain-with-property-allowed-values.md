---
uid: domain-with-property-allowed-values
---

# Domain with property allowed values

Domain is the range of the allowed values of a particular stored attribute (custom property). 

It's determined in one of the following ways, sorted by high-to-low priority:

1. If _Limit To Allowed Values_ **doesn't** have a check mark, <br> any value is valid and the domain is a range of **all** possible values.

2. If _Allowed Values Entity Name_ **has** a value, <br> the domain is **all records** of the specified data type.
   
     This field has a value **ONLY** if _Limit To Allowed Values_ has a check mark <br> and _Allowed Values Property_ does NOT have a value.

3. If _Allowed Values Property_ has a value, <br> the stored attribute domain is **equal** to the stored attribute domain specified in this field.

```
CustomProperty.Domain = CustomProperty.AllowedValuesProperty.Domain
```

   This field has a value **ONLY** if _Limit To Allowed Values_ has a checkmark and _Allowed Values Entity Name_ does NOT have a value.

4. A range of the _Property Allowed Values_ listed in the **Gen_Property_Allowed_Values** sub-table.


**Example 1:**

Let's assume you have the following properties:

- Property 1 (entity name = Products)

- Property 2 (allowed values property = Property 1)

- Property 3 (entity name = Products)

- Property 4 (entity name = Companies)

- Property 5 (allowed values property = Property 2)

- Property 6 (limit to allowed values = False)

**In this case, the domains are:**

- Property 1 - Products

- Property 2 - Products

- Property 3 - Products

- Property 4 - Companies

- Property 5 - Products

- Property 6 – all possible values

## Compatible stored attributes

Two stored attributes are copy-compatible **ONLY** when their domains are the same. 

Compatibility allows you to copy values from one stored attribute to another. This process could result in an error, but it would be caused by various reasons, such as additional filters being set in the definition. 

> [!NOTE]
> 
> Additional filters **don't** change the domain of the stored attribute - they simply reduce the range with allowed values. 
> It's also possible for future procedures or rules to be added, but they **won’t** change the domain of the stored attribute, either.
> From a programming perspective, the domain of allowed values could be defined as a **stored attribute type**.

**Example 2:**

If you use Example 1, you can conclude that:

- 'Property 1' is compatible with 'Property 2'.  Both of them are compatible with 'Property 3' and 'Property 5'. Therefore, 'Property 1', 'Property 2', 'Property 3' and 'Property 5' are compatible with еach other.

- 'Property 4' is compatible with none of the above.

- 'Property 6' can take any value and it is also incompatible with the other stored attributes.

## Inheriting and hereditary root

A stored attribute inherits another stored attribute by indicating a (hereditary) **parent** property in the _Allowed Values Property_ field. The hereditary root of a stored attribute is considered **grand-parent**, which doesn't have a root on its own. It clearly defines the domain and is a prerequisite for automatic copying of its allowed values.

A hereditary root is defined as follows:

1. If _Allowed Values Property_ doesn't have a value, the hereditary root is **the stored attribute** itself.

2. Otherwise, it's equal to the hereditary root of the **parent stored attribute**.

   This means that:<br>
   HereditaryRoot (Property) = HereditaryRoot(Property. AllowedValuesProperty)<br>
   i.e. you look recursively in the relation _Allowed Values Property_.

**Example 3:**

According to the example above, stored attributes have the following hereditary roots:

- Property 1: Property 1

- Property 2: Property 1

- Property 3: Property 3

- Property 4: Property 4

- Property 5: Property 1

- Property 6: Property 6

## Copying

Hereditary roots determine the most appropriate 'partner' to copy allowed values of stored attributes.

**Example 4:** 

Let’s assume that you want to copy stored attributes from a customer to a sales order document.

The customer has the following properties:

- FAVORITE-PRODUCT: (entity name = Products)

- ADVANCE-PRODUCT: (entity name = Products)

In the sales order document type, the following stored attributes are set:

- FAVORITE-PRODUCT-CUSTOMER: Allowed Values Property = CUSTOMER. FAVORITE-PRODUCT

- SALE-ADVANCE-PRODUCT: Allowed Values Property = CUSTOMER.ADVANCE-PRODUCT

**In this case:**

- All four stored attributes are 'compatible'. They could inherit values from one another.

- At the same time, only the following pairs have the same hereditary root:

​    A) FAVORITE-PRODUCT-CUSTOMER and FAVORITE-PRODUCT

​    B) SALE-ADVANCE-PRODUCT and ADVANCE-PRODUCT

When specifying a customer in a sales order, **only** the stored attributes that have the same hereditary root <br> will be automatically copied to the document.

## Stored attributes value priorities

The priority for automatic copying of stored attributes by the following priorities:

> [!NOTE]
>
> If a value with higher priority is found for a stored attribute, it's copied. If not – you should search for values with lower priorities.

1. Values inherited from the parent document. (Priority 80)

2. Values set in the panel **Copy Customer Properties**. (Priority 70) 
 
   This is valid for sales orders, but the same priority applies if there's a similar table for other data.

3. Values of stored attributes with the same hereditary root in the definition of the 'main contractor' of the document. (Priority 50)
   
    In general cases, this is the party loaded in the field _To Party_. <br> Purchase invoices are exceptions - there, the supplier is considered a 'main contractor'. 

4. Default values specified in the document type. (Priority 20)

5. If none of the above contains a value for the stored attributes, but the value is instead specified in the document type: Set an empty (NULL) value. (Priority 10)

> [!NOTE]
>
> Every manual change of a value of a stored attribute should be done after the values are entered in the relevant nomenclatures (enterprise company, customer, parent document etc.)
