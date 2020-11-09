
**Data-Trader** - ***ReadMe***


Data Trader has been designed to easily visualise recent stock data by taking advantage of the Alpha Vantage
API. Data Trader takes utilises Alpha Vantages API to pull a user's desired stock and visualise this within
a users profile.


The website development and purpose has been broken down, into the detailed sections below -

  > ## Contents


* [Features](https://github.com/Karlitoyo/Trading#UX)
    - [Users](https://github.com/Karlitoyo/Trading#Users)
    - [Strategy](https://github.com/Karlitoyo/Trading#Strategy)
    - [Scope](https://github.com/Karlitoyo/Trading#Scope)
    - [Structure](https://github.com/Karlitoyo/Trading#Structure)
    - [Skeleton](https://github.com/Karlitoyo/Trading#Skeleton)
    - [Surface](https://github.com/Karlitoyo/Trading#Surface)
 * [Development](https://github.com/Karlitoyo/Trading#Development)
    - [Current-Features](https://github.com/Karlitoyo/Trading#Current-Features)
    - [Further-Development](https://github.com/Karlitoyo/Trading#Further-Development)
 * [Technologies-Utilised](https://github.com/Karlitoyo/Trading#Technologies-Utilised)
 * [Testing](https://github.com/Karlitoyo/Trading#Testing)
 * [Deployment](https://github.com/Karlitoyo/Trading#Deployment)
 * [User-Stories](https://github.com/Karlitoyo/Trading#User-Stories)
 * [Credits/Media](https://github.com/Karlitoyo/Trading#Credits/Media)
 * [Acknowledgements](https://github.com/Karlitoyo/Trading#Acknowledgements)


  > # UX

The user experience when reaching the site is intended to encourage sign up. Bright colour scheme with content 
related to the service provided as a user scrolls the page. The addition of a javascript button on the bottom
right hand of the page with an embedded GIF is a fun way to encourage users to delve deeper into the service.
Upon signing up and registering for the service using the register page a user is then directed to the dashboard
page. This is a simple design which included a number of card divs to visualize information. At the top right of
the page a user is provided with a grop down which can allow the options of profile & logout. Below the the 
navigation bar then sits 4 card divs with static information. This is purely asthetic. Below the 4 card divs
lies the card div which holds the primary function of the page. With the search function a user can input
any relevant stock ticker held with Alpha Vantage. The information is then visualzied below the search function
allowing a user to see clearly the open,high,low,close,volume of a chosen stock on a particular day. The user can
then log out upon searching for their perferred stock using the drop down on the top right hand corner of the 
navigation bar. The user is prompted if they wish to logout, and upon confirming this they are then logged out
and directed to the home page.

## Users

The website has a target audience of 18-70 year olds. Users must sign up to the service using the register function.
The user also has the option to subscribe to the website newsletter at the bottom of the home page.


## Strategy

The strategy for the website is users will ideally sign up for the service and provide
emails for newsletters which in turn can generate revenue.


## Scope

The Scope of the website is to provide up to date relevant information to users on stocks of their choosing.


## Structure

---Home---

The home page is designed to be intuitive and provide bright vibrant colours to users to create a new and exciting
feeling about the service. The home page is created using a bootstrap theme and customised to purpose. I have
included a macbook and surface picture. I have also amended the content to reflect the service provided. I have then
placed a custom javascript button which shows a gif of a computer searching the net which is hilarious. I have also
included a search box and subscribe button located at the bottom of the page. This is linked to email js and 
provides return an email to the suscribed user. Footer of the page provides content based around copyright. The home
page uses a number of static elements. Jquery, css, js, jquery-easing.

---Login---

The login page allows a user to login to the service once registered. The login function has been created using 
Flask and Werkzeug encryption which is linked to mongodb for storing the user variables.

---Register---

The Register function allows users to register for the service if they have not already. This function also
utilises Flask & Werkzeug. The register function has some user authentication built in. Users must have a
username longer than 5 characters and a password that is also greater than 5 characters. The email must use
alpha numerical and also allows symbols. The users variables are stored within mongodb and called upon login.

---Data---

The data page is the 'piece de resistance' of the entire project. The layout is minimalist in design with
the search function as the primary aspect of the page. The search function utilises python programming and
calls the Alpha Vantage API which is then stored within mongodb. The code is built to recognise when a stock
has been called previously within the db to reduce API calls. The pythin function calls the API through the 
page index.py. This is connected to Mongodb through the env2.py.(Initally called env.py however a workaround
required the creating of env2.py and it remains). The API key is stored in the key.py. Upon pushing to Heroku
I descovered that the the API key must be stored as a config var as my key.py file has been included within
my .gitignore. The index.py function rsi_dataframe is imported to the app.py file as rsi. This is then used
within a Flask function to render this function within my search bow on the base.html page. The python function
with my index.py file (rsi_dataframe), sends the data to mongodb and from mongodb the information is rendered on
the data.html page which is then visualixed on the base.html page.

---Profile---

The profile page is built also using a flask function in python and is currenty designed to provide a welcome message
to the user upon login or registering using jinja templating language.

## Skeleton

Wireframes for the main navigation pages can be found below -

 --Wireframes--
 
- [Home-Page](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Event-Planner-Home.png)
- [Social-Page](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Event-Planner-Social.png)
- [Events-Page](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Event-Planner-Events.png)
- [Home-Page-Mobile](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Events-Planner-Mobile.png)
- [Social-Page-Mobile](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Event-Planner-Mobile-Social.png)
- [Events-Page-Mobile](https://github.com/Karlitoyo/Event-Planner/blob/master/assets/balsamiq/Event-Planner-Mobile-Events.png)


## Surface

The surface of the website is intended to be easy to navigate and provide content that users are drawn to. 
The navigation on mobile and desktop does not alter except for the navigation bar collapsing. 

 > # Development

 ## Current-Features

Within my code I have used HTML5, CSS3, JS, Python, Jquery, Jinja, Flask, Mongodb, email js, Heroku and Bootstrap with 
the inclusion of Alpha Vantgae API services. The current features store users register information and .json data received
from Alpha Vantage.

## Further-Development

Further development would allow for manipulation of the data received and graphing of the data. This would be in
place of the static data cards on the base.html page. Other developments would allow for recently searched data 
by the user within the profile.html page which currently shows a welcome message.

## User Feedback
User feedback was positive for the purposes of UX.


## Technologies-Utilised

- HTML5
- CSS3
- [Java-script](https://www.javascript.com/)
- [Python](https://www.python.org/)
- [JQuery](https://jqueryui.com/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Jquery](https://jqueryui.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Mongodb](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)


- [Font Awesome](fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)
- [MDN](https://developer.mozilla.org/en-US/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Py-Mongo](https://pypi.org/project/pymongo/)
- [W3schools](https://www.w3schools.com/)
- Sam's Teach Yourself - HTML, CSS, Javascript

## API's

- [Email.JS](https://www.emailjs.com/)
- [Alpha-Vantage](https://www.alphavantage.co/)

## Testing

I have multiple iterations of the original styling for the website. I then chose to use two seperate bootstrap templates
for the final product. The home page uses a landing page taken from bootstrap while the core functioning pages use a
seperate template. This has allowed for a unique design that has been styled to purpose. The orignal base.html has a number
of cards which I removed as they did not serve a purpose and created clutter in the UI. My login function had difficulty with
the user authentication however upon review the pattern aspect of the input was amended to ensure proper functionality.

The index.py code went through a number of iterations also as this was the greatest challenge of the entire project.
Originally I was pulling the data in a pandas format however this was changed to allow easier manipulation of data to 
.json format. The rsi_dataframe function was also amended on a number of occasions as originally the function would originally
show within the terminal window. This required further research as the requirement was that the function be uses within the
front end UI.

The date of the rsi_dataframe was also troublesome and required a fix - ohlc_date. This allowed for the data to be rendered
in the required format.

Storing the data in the mongodb was a challenge as this the data was provided with 2 tuples [0],[1]. The [0] was the meta data
and the [1] was the price related data. This can be seen in the rsi_dataframe function within index.py which then returns stock_data.


## HTML/CSS-Validator

- HTML

HTML Validator shows error relating to Jinja templating language used. This is unavoidable as this is a 
requirment for the page to run effectively.

- CSS 

Two warnings shown on css validator however they are also required for operation of site. A bracket and a value 
of text has shown.

## Deployment

The site was deployed on Github and code is available to view using this site.
I navigated to my Github account, on the top left of the screen I selected my "Trading" repository, 
I then deployed through the settings section by scrolling to the 'Github Pages' section roughly 3/4 of the 
way down the page. Selected my master branch as my source and my page was presented to me as.


- Event-Planner : (https://github.com/Karlitoyo/Trading)

**Cloning**

Can be achieved by selecting the green highlighted button which states - "Clone or Download" via the webpage: (https://github.com/Karlitoyo/Trading) this will 
give the option of downloading a .zip file or opening in desktop an option to clone using HTTP is also given for cloning and running project locally through Gitpod. 
I make use of the git pull function (if required to update the branch) and git clone and then git push to named repository.

**Version-Control**

My initial version of the site were mainly a login function and then directed to the profile page upon login. I then
changed the approach to direct users to the base.html page to allow direct access to the search function of the 
webpage. I then included the index.html page as the landing page to provide some eactra functionality and 
information about the site. Many previous versions of the site included differing iterations of the search 
function and base.html layouts. I then decided on a minimalist approach to this page as the search result 
provides alot of information which the user can naviagte upon use of the function.


> # User-Stories

## First-User
The first user who navigated the site found the layout of the index.html page enticing and commented on the 
colous scheme being bright and vibrant. User also found the search function to be very eay to use.

## Second-User
The second user completed register function and found the pop up on landing page to be a good addition. 
Stated wished for more functionality on profile page of website. This is planned for future iterations.


## Developer comments
I will continue to develop date trader. I took on this project to learn more about have data is manipulated
by code. I felt that stock data was the most readily available and easiest to work with in a short amount of
time. Upon starting the project I learnt how to pull data using the API, storing the data in a db, and then 
visualising the data on my UI.


> # Credits

Special thanks must be given to the creators of all the above and below mentioned sources I used to develop 'Data-Trader'.
Thanks to my mentor Sandeep Agarwal, the code institute tutors, in particular Scott as he provided invaluable advise and
feedback throughout my project.

## Credits

- Romel Torres - https://github.com/RomelTorres/alpha_vantage
- Rapid API - https://rapidapi.com/alphavantage/api/alpha-vantage
- PIP install Python - Youtube creator
- W3schools
- MDN
