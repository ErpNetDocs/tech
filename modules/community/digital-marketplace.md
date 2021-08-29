# Digital Marketplace

A Digital Marketplace is a place, where developers publish, and the end-users obtain apps. When an app is activated (installed) on a user device, it is granted certain permissions to access the device resources. The marketplace can, but not necessarily, include functionality for downloading and embedding the app on the device.

It resembles the way iOS and Android provide apps and other content (and allow the apps to access your phone).

The main entities are:

- **Marketplace** - a place where developers publish, and the end-users obtain (install) apps. Each marketplace operates only for a single device type (class).
- **Marketplace App** - third-party app, listed on a marketplace.  The app manifests a set of permissions, which might require functioning. An app can have multiple media resources, attached to it (through its data object), which can be used to display media to the end-user. An app is published by an App Developer.
- **Marketplace App Permission** - permission, which the app might require. There are pre-install permissions, which are required to be granted before installation. Some permissions might be post-install and can be optional. Each app permission is of Marketplace Permission Type.
- **Marketplace App Review** - a review and star rating from a user, who has installed the app. Uses the Social Interactions module for comments and reactions.
- **Marketplace App License Type** - a type of license, which can be provided for an installed instance of the app. Some license types (for example for functionality) allow only a 0 or 1 license qty, while others allow multiple licenses (for example, for max users/max GB or any other max limit of the license).
- **Marketplace Permission Type** - possible permission, which can be requested/granted to an installed application. Each permission type has a permission key, which is a unique string, identifying the permission.
- **User Device** - a device under the user's control. It can be a phone, a computer, a database, a service, a user account (for example in a social network) or anything else, which can allow secure access of apps to its resources.
- **User Device App** - an app from a marketplace installed and granted permission to access a device.
- **User Device App Permission** - permission granted to a specific app for a specific user device.
- **User Device App License** - a license granted to the user, using the app on the device. The app can request its license data through an API call. It is up to the app to limit its usage, based on its license information.
- **App Developer** - a developer account. This is a third-party organization, developing applications for a marketplace. Each marketplace has a different set of approved app developers.
- **App Developer Users** - user accounts, which have access to an App Developer account. Users can be admins, developers (edit app resources) and moderators (interact with app users). The user (and his role) can be for the whole developer account, or just for a single app.


