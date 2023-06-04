# Full Stack Test Automation Project In Python 

### This project created to demonstrate my knowledge and skills in Automation Testing
***
### About
The project demonstrates a smart automation infrastructure. It is built in hierarchy order of modules. The modules contain number of classes with methods. There are main/common/helpers/actions/page_object modules. In this way, the tests can be created in very simple way with a minimum lines of code. Also the infrastructure allows to work with different kinds of applications. **Big advantage of the infrastructure is that it can be easy maintained!**

### Project Overview
The project is an example of infrastructure for automation testing of different kinds of applications:

* Web based application
* Mobile application
* Web API
* Electron application
* Desktop application

### Infrastructure project includes using of:

* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases...)
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support
* Reporting System (including screenshots)
* DB support
* CI support
***
### List of applications were used in this project:

* Grafana webpage - Web based application
* UK-mortgage_calculator - Mobile application [[APK]](https://github.com/EsterYIT/Test-Automation-Python/tree/main/APKs)
* typicode - API [[Api Url]](https://jsonplaceholder.typicode.com/)
* Electron application
* Windows calculator - Desktop application

### Tools & Frameworks used in the project:
* Pytest - Testing Framework
* MySQL - used for login to Conduit web page
* Jenkins- for tests execution
* REST Assured - for API testing
* Allure Reports - as the main reporting system


### Tests Execution:
Each of the applications has a few tests for demonstration purpose. These tests can be developed in a very simple way, due to a lot of work with the infrastructure. [[Sanity Tests]](https://github.com/EsterYIT/Test-Automation-Python/tree/main/test_cases)

### Known Issues:
Sometimes can be conflicts with some dependencies the applications are using. Hence, the project is for DEMO purpose only. In production it should be divided into several projects.




