# Social Interaction

The **Social Interaction** framework in ERP.net brings team collaboration to life through three core components — Social Groups, the Discussions/Chat panel, and Notifications. 
<br>**Social Groups** provide a centralized space for teams to collaborate, share updates, and manage discussions, forming the foundation of the platform’s Social ERP concept. 
<br>Тhe integrated **Chat** component enables real-time communication within groups, while **Notifications** keep users informed and engaged with relevant activities. 
<br>Together, these tools create a connected, efficient, and adaptive collaboration environment for organizations of any size or industry.

## ⚠️ Breaking Changes 
### Breaking Change: Follow Levels and Notification Behavior

Notifications now depend on the Follow Level of objects. All existing follows have been migrated to TAGGED.
<br>TAGGED objects deliver chat/comment events only.
<br>➡️ To continue receiving update or implicit notifications, mark important objects as Follow or Favorite.[Details](../breaking-changes/follows-and-notifications.md)

## Notable features
## Other features

### **1. Gallery of uploaded files**

We’ve added a new Preview option to the Files tab in Social Groups! 🎉
Now, when you select Preview from the file menu, the file opens in a pop-up window, and below it you’ll see a handy gallery of all uploaded files with thumbnails. 

This makes it easier to quickly browse and view shared content without downloading each file — perfect for fast collaboration and visual overview.

 ![files-preview](pictures/files-preview.png)  

### **2. System comment when a Case is assigned**

In our effort to strengthen teamwork and ensure clear announcements, we’ve added a new rule: when a Case is assigned to a group, a system comment and the corresponding notification are automatically generated. This keeps the Case visible to all members and ensures nothing important is missed.

![case_comment](pictures/case_comment.png)
