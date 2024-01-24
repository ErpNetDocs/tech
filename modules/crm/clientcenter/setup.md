# Setup Client Center  

There are a couple of actions you can take to set up your **Client Center** effectively.

### Define website of type ClientCenter 

The following fields need to be considered when defining the website:

1. **Enterprise Company**
 
2. **Relative URL**
 
3. **Is Active** - must be checked

4. **Trusted application** – you can create it from the website definition by using the **Create/Update Trusted Application** function 

> [!NOTE]
> You should define a distinct site with a unique **Relative URL** or **Host** for each **Enterprise Company**.

### Define Trusted Application as follows: 

The following fields need to be considered when defining a trusted application:

1.	**Is Enabled** - must be checked
 
2.	**System User Allowed** - must be checked
 
3.	**Impersonate As Community User Allowed** - must be checked

4.	**Impersonate As Internal User Allowed** - must be checked
  
5.	**System user** - this is the SYSTEM-APPLICATION-USER
  
6.	**Client type** - must be set as "Confidential"
  
7.	**Scope** - must be set as "Update"  
  
> [!NOTE]
> You can observe and restart all sites through the **Instance Manager**.

### Setup User settings: 

The process of configuring user settings typically goes like this:

1. A new user is registered in the Client Center; that creates a **new** user definition called "External Community User".
   
2. You need to define a **Person** and **Parent Party** for this user.
          
3. Then, you need to specify a **Customer** for the Parent Party, taking in mind the following:

   * **Enterprise Company** - must the same as the Client Center's 
   * **Enterprise Company Location** - location of the company

If any of these settings are missing, an **error exception code** from CC002 to CC007 will be displayed depending on what's missing.

