# National Parks 
### All things National Parks in one place!

 ###### * a full-stack group learning project *
 Requirements were: 

  1. Support CRUD operations on 1, or more, features
  2. Implement one or more 1 -> ∞ relationships, and one or more ∞ -> ∞ relationships.
  3. At least one creation form must have a dropdown/radio button group/checkbox group to attached related resources to it.
  4. One of the lists of resources must implement a filtering mechanism in the UI. The filtering must happen at the server, not in the client.
  5. Login and register must be implemented to track data for multiple users.
  6. Users should only be able to edit/delete their own data.


Our team of five spent two days creating the concept, wireframe, ERD and gathering/creating seed data and models 

Two Agile scrum sprints were completed, during which the project client and server were built:
 
  * Week 1 concluded with a client exceeding our MVP requirements and a server built in python and SQL queries
  * Week 2 (client side) concluded with a further updated client with improved styling and a near-fully responsive layout
  * Week 2 (server side) rebuilding the server to utilize Django REST framework instead of pure python/SQL
 
We were given leeway to develop our own project management and ticketing strategies, which was perhaps the toughest part of the project 😅

## Project Overview

National Parks is a responsive web application intended to allow park visitors to have one place with all the resources and information about US national parks.
Users should be able to view and/or interact with a variety of park information and create and view public blog posts.
The back end is coded in Python with a Django framework and utilizes a SQLite database.

## Feature Highlights

#### Switch between map and card views for national parks:


#### View details about specific parks like location, history, wildlife and amenities:




## Installation
Follow the steps below to download and run this project on your computer
- [ ] Client is required for full functionality. [View client repo here](https://github.com/nss-day-cohort-60/national-parks-client-v2)
- [ ] Clone this repo
- [ ] From repo directory, run "npm pipenv install"
- [ ] Run some other things to install requireds
- [ ] Run "python manage.py runserver"


## Tech Stack

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Credits & Acknowledgements

### Hazel Preza
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/segadreamgirl)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hazelpreza)

* Created models for blogs, blog favorites, park favorites, event favorites, and photo favorites 
* Created views for events and blogs
* Participated in code reviews and reviewing pull requests


### John Doll
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/JohnMDoll)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/john-m-doll)

* Favorite View
* Contributed to refactoring SQL insert statements to seed database
* Blog view add, search, edit functions
* README.md


### Maia Dutta
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mvdutta)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/john-m-doll)

* Created models for events, event registration, campground, and camping reservation
* Created views for wildlife and amenities
* Reviewed pull requests and performed code reviews


### Shaina Couch
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shaibird)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shaina-couch)

* 
* 
* 

### Vanessa Spear
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vanessaspear)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vanessavspear)

- Created models for wildlife groups, park wildlife, natural attractions, park natural attractions
- Created photos view to handle requests from the client to the server
- Contributed to refactoring of SQL queries from client version 1 to be able to seed database without having to create fixtures in the Django REST framework
- Created the parks list component and parks map component on the client landing page 
- Reviewed pull requests and performed code reviews
