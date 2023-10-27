# Hospital Management
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sai%20Emani-red)
---
### Problem Statement
This project aims to develop a stubble management system for farmers, industries, and manufacturing companies to ease the process of ordering, tracking, and managing one’s inventory(aka stubble). There is no compelling reason to go to crowded stores or shopping centers during festival seasons: all that one requires is a PC or a laptop. To access, farmers or consumers need credentials to log in. The login credentials for the system are very secure. Upon successful login, the customers can order and track a stubble. It is simple to navigate and use.
## screenshots
### Homepage
![homepage snap](https://github.com/sumitkumar1503/hospitalmanagement/blob/master/static/screenshots/homepage.png?raw=true)
### Admin Dashboard
![dashboard snap](https://github.com/sumitkumar1503/hospitalmanagement/blob/master/static/screenshots/admin_dashboard.png?raw=true)
### Invoice
![invoice snap](https://github.com/sumitkumar1503/hospitalmanagement/blob/master/static/screenshots/invoice.png?raw=true)
### Doctor list
![doctor snap](https://github.com/sumitkumar1503/hospitalmanagement/blob/master/static/screenshots/admin_doctor.png?raw=true)
---
## Functions
### Admin
- Sign up for their account. Then log in (No Approval Required).
- Can register/view/approve/reject/delete doctors (approve those doctors who applied for jobs in their hospital).
- Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
- Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge, and other charge).
- Can view/book/approve Appointments (approve those appointments that the patient requests).

### Doctor
- Apply for a job in a hospital. Then log in (Approval required by hospital admin, only the doctor can log in).
- Can only view their patient details (symptoms, name, mobile ) assigned to that doctor by admin.
- Can view their discharged(by admin) patient list.
- Can view their Appointments, booked by admin.
- Can delete their Appointment, when the doctor attended their appointment.

### Patient
- Create an account for admission to the hospital. Then log in (Approval required by hospital admin, only the patient can log in).
- Can view assigned doctor's details like ( specialization, mobile, address).
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments. (approval required by admin)
- Can view/download Invoice pdf (Only when admin discharges that patient).

---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Do forget to Tick Add to Path while installing Python)
- Open the Terminal and Execute the Following Commands :
```
pip install django==3.0.5
pip install Django-widget-tweaks
pip install xhtml2pdf
```
- Download This Project Zip Folder and Extract it
- Move to the project folder in Terminal. Then run the following Commands :
```
py manage.py make migrations
py manage.py migrate
py manage.py run server
```
- Now enter the following URL in Your Browser Installed On Your PC
```
http://127.0.0.1:8000/
```

## CHANGES REQUIRED FOR CONTACT US PAGE
- In the settins.py file, You have to give your email and password
```
EMAIL_HOST_USER = 'youremail@gmail.com'
EMAIL_HOST_PASSWORD = 'your email password'
EMAIL_RECEIVING_USER = 'youremail@gmail.com'
```
- Login to Gmail through the host email ID in your browser open the following link and turn it ON
```
https://myaccount.google.com/lesssecureapps
```
## Drawbacks/LoopHoles
- Anyone can be an Admin. There is no Approval required for the admin account. So you can disable the admin signup process and use any logic like creating a superuser.
- There should be at least one doctor in the hospital before admitting a patient. So first add doctor.
- On the update page of the doctor/patient you must update the password.
