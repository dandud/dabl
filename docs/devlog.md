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