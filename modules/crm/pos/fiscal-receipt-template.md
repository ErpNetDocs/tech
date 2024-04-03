# Overview

Receipt templates can provide businesses with a customizable solution that enhances their fiscal printing process. They serve as pre-designed formats that you can easily modify and apply on a document type level.

By creating such templates, you gain the flexibility to incorporate personalized text using **[interpolated strings](https://docs.erp.net/tech/advanced/string-interpolation/index.html)** in different sections on the fiscal receipt itself. This includes the ability to define:

* **Custom Header** - refers to the text that will be printed at the top of the fiscal receipt.
  
* **Custom Row Header** - refers to the text that will be printed on certain rows within the mid portion of the fiscal receipt.
  
* **Custom Row Footer** - refers to the text that will be printed on certain rows within the lower portion of the fiscal receipt.
  
* **Custom Footer** - refers to the text that will be printed at the bottom of the fiscal receipt.

By tailoring these elements to their specific needs, users can ensure that every receipt reflects the identity and values of their company, sending the right messages and ultimately enhancing customer experience.

![Pictures](pictures/mceclip5png.png)

## Creating a template

To craft a distinctive template tailored to your business needs, you need to follow a specific set of steps.

1. Locate the **Fiscal Receipt Templates** panel within the **POS** section of the **CRM** module.

2. Click on the panel's **Plus** button to initiate the creation of a new template.

   This takes you to a new page specifically designed for customizing the printouts of fiscal receipts, providing you     with a comprehensive set of options to personalize a template according to your preferences.

3. The first required step in crafting a new template is providing a distinctive **name** for it.
   
   You can do that by using the **Template Name** field.

4. Decide whether to include the **Print System Header** and **Print System Row Header** options.

   This determines if custom headers and row headers will be printed as part of a fiscal receipt.

   To select these options, simply press on their respective **check boxes**. 

5. Click the **three-dot button** on any **Custom** field to open a separate window with several customization options. 

   It is here that you can provide **[interpolated strings](https://docs.erp.net/tech/advanced/string-interpolation/index.html)** for defining what exactly will be written in each respective section. They will be
   arranged across one or more rows.
   
   You can use the **search bar** to locate a particular interpolated string from within the **System Variables**
   section. The latter allows you to choose variables such as date, time, or location of the current transaction that
   will be updated automatically.

> [!NOTE] 
>
> Interpolated strings can include text, domain attributes, and system variables available in the respective document type (e.g. sales order) for which you are creating a fiscal receipt template. You can also import user-defined calculated attributes, which allow for various calculations of prices, amounts, discounts, and more, all of which are printed on the receipt.
 
## How to use fiscal receipts templates

Now that we've created our templates, we are ready to put them into action. To do so, we navigate to the Sales panel and select Orders.
 
In this panel, we can select a document.
 
Once the document is opened, a new page will display all the relevant information. From there, we proceed by clicking on Document Type. 
 
This action will direct us to the Detail panel and from there we can open our document.

When we select the Printouts panel and click on the field labeled Fiscal Receipt Template, it opens the detailed panel associated with selecting the template for fiscal receipts. This panel allows us to choose from the available templates we have created.

Select open and the template will appear.

Selecting the Edit button grants you the ability to make desired modifications to the selected template. Each field within the editing interface provides the option to utilize interpolated strings, provided you've added them during the template creation process.

Once you have made the desired changes to your template, simply click on the Save and Reload button to apply your modifications.
screnshot

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
