# Project Surf
![Homepage](/readmeimages/Homepage.png)

[Link to LIVE dashboard](https://surf-project-app.herokuapp.com/)

# Table of Contents:

1. Project Goals
2. UX
3. Project Sprints
4. Features
5. Technologies used 
6. Testing
7. Deployment
8. Acknowledgments 


# 1. Project Goals
The aim of this project is to create an MVP application for a volunteer dashboard for a (fictional) charity called Project Surf. The users will include volunteers and the lead volunteer (admin). 


# 2. User Experience

## 2.1 User Stories 

### Lead volunteer:

1. As a lead volunteer, I need to be able to upload a photo of myself and bio so that other volunteers can familiarise themselves with my face.
2. As a lead volunteer, I need to be able to add sessions (date, time) to the dashbaord, so the volunteers can see the upcoming sessions. 
3. As a lead volunteer, I need to be able to use the app on my phone, so I can be updated and sign up for sesssions on the go. 
4. As a lead volunteer, I need to be able to delete sessions, so the volunteers have up to date information about the sessions.
5. As a lead volunteer, I need to be able to edit sessions, so the volunteers have up to date information about the sessions.

### Volunteer:

1. As a volunteer, I need to be able to upload a photo of myself and bio so that other volunteers can familiarise themselves with my face.
2. As a volunteer, I need to be able to see sessions (date, time) on the dashbaord, so I can see the upcoming sessions. 
3. As a volunteer, I need to be able to use the app on my phone, so I can be updated and sign up for sesssions on the go.
4. As a volunteer, I need the dashboard to be clear and easy to use, so I don't get bogged down in volunteering admin.  


## 2.2 Structure

### Models
![Volunteer Model](/readmeimages/models.png)

### Site Map
![Site map](/readmeimages/Sitemap.png)



## 2.3 Wireframes (low-fidelity)
### Homepage/Desktop :
![Homepage](/readmeimages/Homepage_desktop.png)
### Dashboard/Desktop (logged in as admin)
![Dashboard](/readmeimages/Dashboard_desktop.png)
### Add Profile /Desktop
![Dashboard](/readmeimages/Add_profile_desktop.png)
### Add Session/Desktop (logged in as admin)
![Dashboard](/readmeimages/Add_session_desktop.png)
## 2.4 Design
The design for the dashboard is simple and functional. I added a hero image to ignite some excitment to the dashbaord. The colors are fitting with the simple design and also the theme of surfing and being in the water. 

# 3. Project Sprints

I used an agile approach to this project by following pre-planned sprints. The sprints were broken down into issues with were logged on the Github project board. [View here](https://github.com/users/angharadcaswell/projects/1/views/1)

As seen in the image below, I used a kanban board to track the progress of my tickets. 

![Project board](/readmeimages/project_board.png)

## Sprints:
1. Set up Python, database
2. Set up base html/css and create Home app
3. Volunteer log in and sign up
4. Create Session Dashboard app
5. Session dashboard log in (show profiles & sessions in swipe view)
6. Volunteer sessions (lead volunteer (admin) to be able to add, edit and delete sessions)
7. Profile (volunteers to be able to add bio and profile photo)
8. Lead volunteer to add volunteers to surf sessions
9. Testing and ReadMe



# 4. Features

## 4.1 All features
### Homepage:
![Homepage](/readmeimages/Homepage.png)
### Dashboard- Sessions on Dashboard (logged in as admin)
![Dashboard](/readmeimages/session_dashboard.png)
### Dashboard- Profiles on Dashboard:
![Dashboard](/readmeimages/profile_dashboard.png)
### Dashboard- Add Session (logged in as admin)
![Dashboard](/readmeimages/add_session.png)
### Session- Delete Session (logged in as admin)
![Dashboard](/readmeimages/delete_session.png)
### Session- Edit Session (logged in as admin)
![Dashboard](/readmeimages/delete_session.png)
### Dashboard- Full Session (logged in as admin)
![Dashboard](/readmeimages/full_session.png)
### Profile - Add Profile
![Dashboard](/readmeimages/add_profile1.png)



## 4.2 Features to implement:

1. Volunteers can sign themselves up to sessions and get approved by lead volunteer
2. Volunteers can upload training docs to their profile
3. Messaging platform for lead volunteer to be able to send news and information. 
4. Lead volunteer to be able to add and assign young people to the volunteers. 
5. Add FAQS page
6. Stats on dashbaord so lead volunteer can see volunteer's hours etc.


# 5. Technologies used 
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Content and structure
* [Heroku](https://id.heroku.com/login) - Host
* [Gitpod](https://www.gitpod.io/) - Coding workspace
* [Github/ Github pages](https://github.com/)- Commit my code
* [Am I responsive?](http://ami.responsivedesign.is/#)- To see display the website as mock ups  
* [Django Alauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
message. 




# 6. Testing  
The site was tested in Gitpod terminal and Heroku by users and myself on all browsers. The site was also peer reviewed by the Code Institute community. 

## 6.1 User testing:
Users were asked to navigate around the site and also to make intentional mistakes to help check for errors.
Users had tasks to complete, which included the following:

1. Register and log into the site. 
2. Add a photo and bio to your profile.
3. Update your bio and photo on your profile. 
4. Using the admin log in, add, edit and delete a session. 
5. Using the admin log in, assign volunteers to a session. 

Overall feedback was very positive and users found the site easy to navigate. Everyone was able to complete the tasks assigned. Users noticed the following issues:

1. Social links do not have links connected. **Fixed by** social links added.
2. One user found it frustrating that they didn't have any easy exit if they chose not to go ahead with deleting a session.  **Fixed by** adding a button with a cross that takes you back to the dashboard. 


[User Stories Tested](userstories.md)

## 6.2 Bugs:
These significant bugs were found during user testing and during the build process. 

1. During testing, a user noticed that the profile name on the profile section on the dashboard isn't showing. 
- **Solution**:

2. Users can access edit and delete sessions urls even if they aren't logged in as admin. 
- **Solution**:

## 6.3 Code Validation
- Used [PEP8 Python Validator](http://pep8online.com/) to check all Python content files. Each file recieved "All Right".



# 7. Deployment

To deploy this page to Heroku from its GitHub repository, the following steps were taken:
1. Clone this repository in Github
2. Create the Heroku App:
- Select "Create new app" in Heroku.
- Choose a name for your app and select the location.

3. Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

4. Prepare the environment and settings.py file:

- In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Add the SECRET_KEY value to the Config Vars in Heroku.
- Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
- Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
- In settings.py add the following sections:
Cloudinary to the INSTALLED_APPS list
STATICFILE_STORAGE
STATICFILES_DIRS
STATIC_ROOT
MEDIA_URL
DEFAULT_FILE_STORAGE
TEMPLATES_DIR
Update DIRS in TEMPLATES with TEMPLATES_DIR
Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']
5. Store Static and Media files in Cloudinary and Deploy to Heroku:

- Create three directories in the main directory; media, static and templates.
- Create a file named "Procfile" in the main directory and add the following:
- web: gunicorn project-name.wsgi
- Log in to Heroku using the terminal heroku login -i.
- Then run the following command: heroku git:remote -a vegan-a-eat. This will link the app to the Gitpod terminal.
- After linking your app to your workspace, you can then deploy new versions of the app by running the command git push 
heroku main and your app will be deployed to Heroku.

# 8. Credits
- Free images: [free image website](https://www.pexels.com/search/surfing/?orientation=landscape)
- Stackoverflow: [Stackoverflow](https://stackoverflow.com/)


## Acknowledgments: 
* [Code Institute](https://codeinstitute.net/) student support, slack community and tutorials. 