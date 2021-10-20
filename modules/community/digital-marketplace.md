# Digital Marketplace

---
items: Community
---

A digital marketplace is where developers publish apps for the end-users. When an app is activated (installed) on a user device, it is granted certain permissions to access the device resources. The marketplace can, but not necessarily, include functionality for downloading and embedding the app on the device.

It resembles the way iOS and Android provide apps and other content with access to your phone.

The main entities are:

- **Marketplace** - where developers publish and end-users obtain (install) apps. Each marketplace operates only for a single device type (class).

- **Marketplace App** - a third-party app listed on a marketplace and published by an app developer. It manifests a set of permissions which might require functioning. An app can have multiple media resources attached to it. They can be used to display media to the end-user. 

- **Marketplace App Permission** - permission which an app might require. There are pre-installed permissions required before installation. Some permissions might be post-install and optional. Each app permission is of Marketplace Permission Type.

- **Marketplace App Review** - a review and star rating coming from a user who has installed the app. Uses the Social Interactions module for comments and reactions.

- **Marketplace App License Type** - a type of license which can be provided for an installed instance of an app. Some license types allow only a 0 or 1 license qty, while others allow multiple licenses (for example, for any maximum limit of the license).

- **Marketplace Permission Type** - permission which can be granted to an installed application. Each permission type has a permission key - a unique string identifying the permission.

- **User Device** - a device under the user's control. It can be a phone, computer, database, service, user account (in a social network) or anything else which allows secure access for apps to its resources.

- **User Device App** - an app from a marketplace installed and granted permission to access a device.

- **User Device App Permission** - permission granted to a specific app for a specific user device.

- **User Device App License** - a license granted to a user using an app on the device. The app can request its license data through an API call. It is up to the app to limit its usage, based on license information.

- **App Developer** - a developer account. This is a third-party organization developing applications for a marketplace. Each marketplace has a different set of approved app developers.

- **App Developer Users** - user accounts which have access to an App Developer account. Users can be admins, developers (editing app resources) and moderators (interacting with app users). The user (and his role) can be for the whole developer account, or just for a single app.


