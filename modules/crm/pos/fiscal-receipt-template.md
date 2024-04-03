# Overview

Receipt templates can provide businesses with a customizable solution that enhances their fiscal printing process. They serve as pre-designed formats that you can easily modify and apply on a document type level.

By creating such templates, you gain the flexibility to incorporate personalized text using **[interpolated strings](https://docs.erp.net/tech/advanced/string-interpolation/index.html)** in different sections on the fiscal receipt itself. This includes the ability to define:

* **Custom Header** - refers to the text that will be printed at the top of the fiscal receipt, above the system header.
  
* **Custom Row Header** - refers to the text that will be printed before certain rows of the fiscal receipt.
  
* **Custom Row Footer** - refers to the text that will be printed after certain rows of the fiscal receipt.
  
* **Custom Footer** - refers to the text that will be printed at the bottom of the fiscal receipt, next to the system footer.

It's possible to take fiscal receipt customization even further by defining interpolated strings:

* **Before/after a sale**

* **Before/after a discount**

* **Before/after a subtotal**

* **Before/after payment**

By tailoring these elements to their specific needs, users can ensure that every receipt reflects the identity and values of their company, sending the right messages and ultimately enhancing customer experience.

![Pictures](pictures/mceclip5png.png)

## Creating a template

To craft a distinctive template tailored to your business needs, you need to follow a specific set of steps.

1. Locate the **Fiscal Receipt Templates** panel within the **POS** section of the **CRM** module.

   ![Pictures](pictures/Screenshot_22.png)

2. Click on the panel's **Plus** button to initiate the creation of a new template.

   This takes you to a new page specifically designed for customizing the printouts of fiscal receipts, providing you with a comprehensive set of options to personalize a template according to your preferences.

   ![Pictures](pictures/Screenshot_44.png)

3. The first required step in crafting a new template is providing a distinctive **name** for it.
   
   You can do that by using the **Template Name** field.

4. Decide whether to include the **Print System Header** and **Print System Row Header** options.

   This determines if custom headers and row headers will be printed as part of a fiscal receipt.

   To select these options, simply press on their respective **check boxes**.

   ![Pictures](pictures/Screenshot_88.png)

5. Click the **three-dot button** on any **Custom** field to open a separate window with several customization options.

   ![Pictures](pictures/button_click.png)

   It is here that you can provide text as well as **[interpolated strings](https://docs.erp.net/tech/advanced/string-interpolation/index.html)** for defining what exactly will be written in each respective section.

   You can also locate and directly add **system variables** such as date, time, or location.

   ![Pictures](pictures/variables.png)

  > [!WARNING] 
  > Keep in mind that writing interpolated strings comes with a few rules and limitations. The width of a row is considered a unique parameter for each cash register. Therefore, certain symbols need to be added when you want to align or fill out fiscal receipt rows.

   * You should use the following operators to transfer interpolated strings to another row:
   
     "\r\n", "\\n", "'\\r", "\n", "\r".

     The string will be transfered into a new row as long as it contains symbols such as "<CR> <LF>, <CR>, <LF>" or a sequence of "\n" or "\r" symbols.

  * To prevent receipts becoming too long in size, there is a limit in terms of how many symbols can be provided and how many new rows with interpolated strings can be created.

   * Text will be automatically trasferred on a new line as long as identical symbols are present to fill the rest of the previous line. In that case, the identical symbols will be scrapped and whatever follows them is moved to a new line.
       
     **Example:**
     
     "This is <br>
       text\+++++++++++++++++++++++++++++++++++<br>
     ++++++++++++++++++++++++++ more text"

     **This will result in two lines:**

     "This is text"<br>
     "+++++++++++++more text"

     The length of each row depends on the cash register's capabilities. <br><br>

6. When you're ready building your fiscal receipt template, click **Save and reload**.

   ![Pictures](pictures/templatereadysaved.png)

> [!NOTE] 
>
> Interpolated strings can include text, domain attributes, and system variables available in the respective document type (e.g. sales order) for which you are creating a fiscal receipt template. <br><br> You can also import user-defined calculated attributes, which allow for various calculations of prices, amounts, discounts, and more, all of which are printed on the receipt.
 
## Defining a template for a document type

Now that you've created a template, you are ready to link it to a document template. 

1. Navigate to a document, e.g. a sales order, and open its **document type**.

   ![Pictures](pictures/documenttypes.png)

2. Edit the document type definition and locate the **Printouts** panel. If it isn't already visible, add it through the **Customize panel** feature.
  
3. From the **Fiscal Receipt Template** field, select the fiscal receipt template you created.

   ![Pictures](pictures/template_select.png)

4. Click **Save and reload** to apply your changes.
  
   The fiscal receipt template will now be enforced for all documents of the respective document type.

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
