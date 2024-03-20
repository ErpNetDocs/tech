# Document print images 

Document print images contain the data of a **printout** of a document as it was obtained at the moment of printing. 

This data is used as a history in order to review the visual representation of the printed document.

## Print images tracking

For every document of a given document type, you can configure a setting that allows you to decide when document print images will be tracked.

This is done to ensure that no unnecessary amount of space is accummulated as a result of constant print image tracking.

### Step-by-step process

1. Go to a document type definition (e.g. Sales Order) and navigate to the **Track Print Images** field.

   If this field is disabled, enable it using the **Customize panel** option.

2. Select one of the available settings:

   * **Do not track** - prevents printouts of documents of the respective type to be automatically created
     
   * **Save source data (compressed)** - allows visual representations of a printed document of the respective type to be saved and previewed.

### Delete 

The **Track Print Images** feature often takes the most space in customer databases. Therefore, it is good to delete obsolete records periodically. 

It is highly recommended that you set up a system job for that purpose, such as **[Deletе old document print images](https://docs.erp.net/tech/advanced/jobs/J30903.html?q=J30903%20Delet%D0%B5%20old%20document%20print%20images)**.
