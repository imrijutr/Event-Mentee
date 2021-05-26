![BFH Banner](https://trello-attachments.s3.amazonaws.com/542e9c6316504d5797afbfb9/542e9c6316504d5797afbfc1/39dee8d993841943b5723510ce663233/Frame_19.png)
# Event Mentee
The Event Mentee is an event management platform for creating the events for organizers and registering the events for who wish to participate in it.
Event Mentee has features like 
- Create events
- Update created event's
- User profile
- Upcoming events
- Registered upcoming events
- History of all events registered, attended, created.
- Limit max registration for an event.
- RSVP in built
- And many more...

## Team members
1. [Ajin K J](https://github.com/Ajinkj)
2. [Leen David P B](https://github.com/LeenDavidPB)
## Team Id
BFH/recmliFUaORA6shU5/2021
## Link to product walkthrough
[Video Explanation in malayalam](https://www.loom.com/share/0b74dd06ea1648cbb776a0dc776cf8fe)
## How it Works ?

We used Django to build our webapp. We created the models to save datas of user, events, registered events, etc. Then we setup the url's and views associated with it. Once the user click on our webapp link they are takin to the Home, there they can find option to create event, profile, signup, login, upcoming events, etc. Anew user can signup and existing user can login. Then they can create event, register for the available events, update there profile picture and many more. A ton of faetures is added to our webapp.

2.[https://www.loom.com/share/0b74dd06ea1648cbb776a0dc776cf8fe]
## Libraries used
- asgiref==3.3.4
- dj-database-url==0.5.0
- Django==3.2.3
- django-ckeditor==6.0.0
- django-filter==2.4.0
- django-heroku==0.3.1
- django-js-asset==1.2.2
- gunicorn==20.1.0
- Pillow==8.2.0
- psycopg2==2.8.6
- psycopg2-binary==2.8.6
- pytz==2021.1
- sqlparse==0.4.1
## How to configure
#### 1. Clone to https://github.com/imrijutr/Event-Mentee.git
`git clone https://github.com/imrijutr/Event-Mentee.git`
#### 2. Create Virtual Environment 
`python3 -m venv /path/to/new/virtual/environment`
#### 3. Activate the Virtual Environment
` source <path to venv>/bin/activate`
#### 3. Install all the dependencies
`pip install requirements.txt`

## How to Run
####  Run the server using the following command
`python manage.py runserver`
