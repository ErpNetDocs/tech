# Document print images 

Document print images contain the data of a **printout** of a document as it was obtained at the moment of printing. 

This data is used as a history in order to review the visual representation of the printed document.

## Delete old images

Document print images often take the most space in customer databases. 

One means of managing them is to **delete** the more obsolete records periodically. This can be done with the **[Deletе old document print images](https://docs.erp.net/tech/advanced/jobs/J30903.html?q=J30903%20Delet%D0%B5%20old%20document%20print%20images)** system job. 

However, there is a way to not even track print records in the first place - for further details, please refer to the **Enable or disable print images Tracking** section.

## Enable or disable print images tracking

A **setting** is available to control the tracking of print images for all documents of a specific type.

This functionality is configured through the "Track Print Images" field within the Document Type definition.

The available settings are:

   * **Do not track** - prevents print images of all documents of the respective type from being automatically stored. This can be useful for scenarios where print image tracking is unnecessary or unwanted.
     
   * **Save source data (compressed)** - enables the tracking of visual representations of printed documents of the respective type. These images are compressed for efficient storage and are available for preview within the system.
   
