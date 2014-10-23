## A Java Developer's Attempt at Python Programming
---
#### Overview
This is an attempt at learning Flask, a Python web framework and using it to do something useful. The project will attempt to use SendGrid and Mandrill email services in order to allow the user to send emails. The project will automatically do failover if one of the services are down or none-responsive.

#### Program Explaination
The project is a simple email form which is connected to Mandrill and SendGrid services. The user is allowed to use any email address for the TO and FROM fields and write a text based email. Yahoo apparently has issues with Mandrill and hence you won't be able to use a Yahoo email address for the From field ([more info](http://comluv.com/yahoo-changed-policy-emails-using-services-like-mandrill)). Currenlty the drop down for simulating different situations is not connected to the backend, but you can simulate a failure of one of the services by updating the API credentials in the **config.py** file. The backend will attempt to send the email via the first service and if it fails, it will immediately try the second service. If both services fail, it will notify the user of the failure.




#### 
---

### Stats
#### Time Spent: 
+ **Researching Technologies to Choose From:** 2 hours
+ **Learning Flask:** 2 hours
+ **Learning Mandrill and SendGrid API:** 1 hours
+ **Coding Backend REST API:** 4 hours
+ **Coding Frontend:** 2 hours
+ **Testing and Debugging:** 3 hours

#### Total Time: 15 hours

---

### Technology Stack
#### Backend
* Python
* Flask Web Framework
* Mandrill
* SendGrid

#### Frontend
* Backbone.js
* Underscore.js
* Bootstrap
* BootstrapValidator

#### Decision Making Process for Choosing Technology Stack

I knew from the begining that I wanted to attempt to use Python to do this task. I had very little previous experience in Python, and absolutely no experience in writing web applications in Python. After carefully examining my options in Python (Flask, Django, web2py, Pyramid) I chose to use Flask for this implementation. My reasning depended on the fact that this was a faily simple framework to learn in a short period of time, and since the application would never grow to a large scale application, it did everything I needed it to do. The speed at which I was able to write my "hello world" app in Flask gave me the confidence to continue the project with it.

I have used the rest of the technology stack in previous projects, with the exception of BootstrapValidator which I chose to use for validating the form. My goal was to keep this very simple and straightforward, without any complexities in UI or backend.


---

### Running Locally
1. Clone this repo with

   ```
   git clone https://github.com/asaghatelian/email-service.git
   ```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

   ```
   cd email-service
   pip install -r requirements.txt -t lib
   ```
4. Run this project locally from the command line:

   ```
   python server.py
   ```

5. Visit the application [http://localhost:5000](http://localhost:5000)

---

### Next Steps

`TODO` Write test cases for front and backend. I should have started this project with writing test cases before coding, but I wanted to finish it within the timeframe that I had allowed myself

`TODO` Implement the drop down for allowing the user to simlulate different environments, such as one of the services failing

`TODO` Implement stronger security measures for the API as well as the frontend with user login or verification

`TODO` Add WYSIWYG editor for the email message composer and allow the user to send HTML emails

