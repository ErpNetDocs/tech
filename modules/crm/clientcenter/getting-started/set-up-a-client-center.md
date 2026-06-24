# Set up a Client Center

This article provides a step-by-step guide on creating a Client Center website through ERP.net.

## Before you start

Before creating the website, determine:

- the **Enterprise Company** for which the Client Center will be created;
- the **Relative Url** that the website will use.

> [!TIP]
> Define a distinct site with a unique **Relative Url** for each **Enterprise Company**.

## Step-by-step process

To set up a website of **Client Center** type, navigate to **System** > **Configuration** > **Web Sites**.

Then click **New** to begin creating a new website.

[screenshot: client-center/getting-started/set-up-a-client-center/cc-getting-started-set-up-a-client-center-01-new-web-site-form.png]

### Website definition

In the **New Web Site** form, enter the relevant data in the available fields.

1. Select the appropriate **Enterprise Company**.  
   The currently logged-in company is selected by default.

2. Set **Web Site Type** to **Client Center**.  
   
3. Specify the **Relative Url** of the website.  
   By default, it is set to `cc`.

4. If needed, specify the settings that will apply to the Client Center website.  
   You can do this now or later when editing the website.

   Client Center settings are entered in the **Settings** field in key-value pair JSON format.

   For more information, see [Configuration](../configuration/index.md).

When you are ready, click **Save and reload**.

The new Client Center website is created and can be accessed through the configured **Relative Url**.

> [!NOTE]
> The **Trusted Application** field does not need to be configured when creating a website. It can be left empty. The site runs under the internal **SYSTEM** user, and its background service session does not consume a license.

> [!NOTE]
> Whenever you apply or change settings for the Client Center, you need to restart the website through the Instance Manager.

## Expected result

After completing these steps, you have a Client Center website definition that can be accessed through its **Relative Url**.

## Related pages

- [Configuration](../configuration/index.md)
- [Common configuration notes](../configuration/common-configuration-notes.md)
- [Set up administrator access](set-up-administrator-access.md)


## Next step

After the website is created, continue with [Set up administrator access](set-up-administrator-access.md).
