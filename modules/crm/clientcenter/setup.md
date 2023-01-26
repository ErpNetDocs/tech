# Setup Client Center  

## Define website of type ClientCenter as follows: 
- Enterprise Company
- Relative URL
- Is Active - check marked
- Trusted application – you can create it directly from the website definition form by using the function Create/Update Trusted Application 

> [!NOTE]
> For each Enterprise Company, a different site with a different Relative URL or Host should be defined. 

## Define Trusted Application as follows:  
- Is Enabled: check marked 
- System User Allowed: - check marked
- Impersonate As Community User Allowed - check marked
- Impersonate As Internal User Allowed - check marked
- System user:  <SYSTEM-APPLICATION-USER> 
- Client type: Confidential
- Scope: Update   
  
> [!NOTE]
> Through the Instance Manager you can see and restart all sites.

## Setup User settings: 
1.	New User registers himself from the Client Center – it creates a new User definition as External Community User.  
2.	Define Person for this User. 
3.	Define Parent Party for this Person. 
4.	Define Customer for this Parent Party as follows: 
    - Enterprise Company 
    -	Serviced by Enterprise Company Location 
