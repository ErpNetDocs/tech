# Set up a Client Center

This article provides a step-by-step guide on creating a Client Center website in ERP.net.

## Step-by-step process

To set up a website of **Client Center** type, open the **Web Sites** navigator in the **Configuration** section of the **System** module.

Then click **New** to begin creating a new website.

## Website definition

<!-- Screenshot needed: New Web Site form with Enterprise Company, Web Site Type, Relative Url, and Settings -->

In the **New Web Site** form:

1. Select the appropriate **Enterprise Company** for which the Client Center is created.  
   The currently logged-in company is selected by default.

2. Set **Web Site Type** to **Client Center**.  
   This is the only mandatory field.

3. Specify the **Relative Url** of the website.  
   By default, it is set to `cc`.

> [!TIP]
> Define a separate site with a unique **Relative Url** for each **Enterprise Company**.

You can also specify the settings that will apply to the Client Center website.

You can do this now or later when editing the website. For more information, see [Configuration](../configuration/index.md).

When you are ready, click **Save and reload**.

The new Client Center website is created and can be accessed through the configured **Relative Url**.

> [!NOTE]
> The **Trusted Application** field does not need to be configured when creating a website. It can be left empty. The site runs under the internal **SYSTEM** user, and its background service session does not consume a license.

## Apply platform settings

Client Center supports settings that control its visual appearance and functional behavior.

Important examples include:

- showing or hiding the **New Order** module;
- defining which document types are shown in the **Orders** module;
- defining which document types are shown in the **Invoices** module.

For the full list of settings, see [Configuration](../configuration/index.md).

## Next step

After the website is created, continue with [Add your first external user](add-your-first-external-user.md).
