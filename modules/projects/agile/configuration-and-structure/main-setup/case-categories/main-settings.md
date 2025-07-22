---
uid: main-settings
---

## Main settings

### Allowed Project Types

Each Case Category must be explicitly linked to one or more Project Types.  
This means that a Case of a given Category can only be associated with Projects of an allowed Type.

**For example:**

- The "User Story" category may allow Cases to be created only in Projects of type:
  - Business Analysis  
  - Website Development

- A Project of type Marketing Campaign will not appear in the selection list when creating a User Story.

This setup ensures consistency across the system and prevents Case misclassification.

**Configuration path:** *Case Category definition → Project Types panel*

![Allowed Project Types](pictures/category-project-types.png)

### Allowed Parent Categories

When defining a Case Category, it is also possible to specify which other Case Categories are allowed to act as parents for this Category.  
This enables organizations to control the hierarchy of Cases based on business logic.

**For example:**
- A Case of category "User Story" may only be allowed to be subordinated to parent Cases from categories such as:
  - User Story  
  - Feature  
  - Epic  
  - Feature  
  - Initiative
- It would typically not be allowed to have another User Story as a parent, unless explicitly configured.

These parent-child rules ensure logical structure and prevent recursive or nonsensical relationships between Cases.

**Configuration path:** *Case Category definition → Allowed Parents panel*  
*Display panel name:* **Allowed Parents**  
*System panel name:* **Relationships**

**Examples of Case Categories with their allowed Project Types and parent context**

| **Case Category**     | **Allowed Project Types**                             | **Allowed Parent Categories**         |
|-----------------------|--------------------------------------------------------|----------------------------------------|
| Bug                   | Product Development                                    | User Story, Feature, Epic              |
| Feature               | Product Development                                    | Epic, Initiative                       |
| User Story            | Product Development<br>Website Development            | Epic, Initiative                       |
| QA Task               | Product Development<br>Client Implementation          | Feature                                |
| Discussion            | Client Implementation<br>Process Optimization         | Epic, Initiative, Feature              |
| Scheduled Task        | Process Optimization<br>Client Implementation         | –                                      |
| Social Media Task     | Social Media Strategy                                  | Campaign Concept, Initiative           |
| Campaign Concept      | Social Media Strategy                                  | Initiative                             |

