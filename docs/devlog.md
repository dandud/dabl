### **2021.10.17** ###
* created base template of application using [flasky application](https://github.com/miguelgrinberg/flasky)
* created database design 
* developed models and html for overview

![database design](docs/screenshots/20211017_database design.png)

### **2021.10.18** ###
* created view batch view and route
* created html page to show simple batch data and started steps to pull measurements
* updated batch overview page to link to new batch data view page
* setup route to batch data view to use batch name a variable to the route

### **2021.10.19** ###
* added more models to database for actions and components
* updated db with new migration script
* added actions view batch page

### **2021.10.20** ###
* created route for adding action and form
* need to add date picker and dropdown for action to form

### **2021.10.21** ###
* updated action form to prepopulate with data
* added drop down for action type
* created measurement route and form (similar to action form)
* confirmed functionality of database writes of measurement and action form

### **2021.10.22** ###
* created add batch form and associated components
* experimented with timeline [object](https://bbbootstrap.com/snippets/basic-timeline-for-users-without-avatar-37843493)

### **2021.10.23** ###
* created edit batch from and associated components 
* updated overview edit button to link to new form
* added and experimented with [Flask-QRcode library](https://marcoagner.github.io/Flask-QRcode/)

### **2021.10.24** ###
* add containers to models and migrate db
* created add container route and form in subfolder
* create route for view vessel and start vessel overview

### **2021.10.25** ###
* add containers batch view page and route

### **2021.10.26** ###
* added vessel lookup route to view current batch based on vessel id
* added vessel label route to generate QR Code label for designated container 
* added view lable links to vessel overview

### **2021.10.27** ###
* added age since start to model, need to investigate how to determine brew length and show with total age
* started work on form to move batch to different container
* added view lable links to vessel overview

### **2021.10.31** ###
* Created move contents form and test
* added link to move contents on batch view
* created ability to update vessel status and added to vessel overview

### **2021.11.02** ###
* Added container and batch history models
* Added listen events to detect changes on container and batch tables

### **2021.11.06** ###
* added fill vessel view and linked to batch view

### **2021.11.07** ###
* updated vessel over view to filter out out of service containers
* updated move contents form to show batch id
* worked on login functionality
* added email to user model and updated db

### **2022.01.16** ###
* reverted to commit 84f1f5ef56b7126ab2333170aa28da9095fc8110

### **2022.01.17** ###
* began refactor to split container and vessel

### **2022.01.18** ###
* initial development of vessel create form

### **2022.01.23** ###
* refactor vessel label and overview

### **2022.03.07** ###
* refactor vessel move, update status, fill, edit label html

### **2022.03.08** ###
* create container overview
* create container add
* add containers to batch view

### **2022.03.09** ###
* create container label
* added abv and description column to batch model
* database migrations

### **2022.05.02** ###
* explore modals for container label and container consumption
* need to create route for consumption of container

### **2022.05.03** ###
* added route for consumption of containers
* updated container overview
* updated route for container add to set container status when created

### **2022.05.04** ###
* began work of refactoring engineering units
* created engunits table, updated container model with relationship
* migrate / updated db

### **2022.12.29** ###
* updates to vessel form to set name
* initial docker config

### **2022.12.31** ###
* Modifications to docker config and requirements to support postgres