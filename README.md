
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
provides return an email to the suscribed user. Footer of the page provides content based around copyright.

---Login---

The login page allows a user to login to the service once registered. The login function has been created using 
Flask and Werkzeug encryption which is linked to mongodb for storing the user variables.

---Register---

The Register function allows users to register for the service if they have not already. This function also
utilises Flask & Werkzeug. The register function has some user authentication built in. Users must have a
username longer than 5 characters and a password that is also greater than 5 characters. The email must use
alpha numerical and also allows symbols. The users variables are stored within mongodb and called upon login.

--Data


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

Within my code I have used HTML, CSS, JS, and Bootstrap with the inclusion of several API services. I have also begun to implement a 
search function using ‘React’ and have also begun to research ‘indexeddb’. I have left my code in comments within the development of 
my Github submission. I primarily used bootstrap for the development of the layout as this provided a responsive design for mobile, 
tablet, desktop and larger screens. The primary learning curve revolved around the inclusion of API’s within the site. I have included 
3 API’s in the development of the site. Google Maps API, Mail.js API, and Ticketmaster API. Google maps API was implemented to show 
the featured artists event locations as a visual representation on the home page. Mail.js API provides a response welcome e-mail to 
subscribers of the website and is provided on all three webpages. Ticketmaster API provides a Widget to the home page which re-directs 
users to the Ticketmaster purchase site, the Ticketmaster API also provides JSON data which is used to provide a listing of events, 
date location and time on the ‘Events’ section of the website. 


## Further-Development

Further development of the website will allow the site to include a search function using either Fetch or React which can search the 
Ticketmaster API JSON data and allow users to filter for their desired result. Further development would link the JSON location data 
to the google Maps API and provide a live location of the event. Connecting the subscribe service to a database to track a listing of 
all subscribers is a development feature to be included. Within the ‘What are you Sayin’ section by connecting to twitter or other 
social media platforms API this would allow the site to pull live updates with the use of a hashtag.

## User Feedback
User feedback was positive for the purposes of UX.


## Technologies-Utilised

- HTML
- CSS
- Java script
- Python
- [Bootstrap](https://getbootstrap.com/)
- [Mongodb](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)


- [Font Awesome](fontawesome.com)
- [Google Fonts](https://fonts.google.com/)
- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/)
- [MDN](https://developer.mozilla.org/en-US/)


- [W3schools](https://www.w3schools.com/)
- Sam's Teach Yourself - HTML, CSS, Javascript

## API's

- [Email.JS](https://www.emailjs.com/)
- [Google-Maps](https://cloud.google.com/maps-platform)
- [TicketMaster](https://developer.ticketmaster.com/)

## Testing

Testing was completed as the site was developed, I took the approach of start with the easy aspects and develop around these. 
This allowed me to develop the core functionality of the site and test this rigorously as the site developed across mobile, 
tablet, desktop, larger screens and multiple browsers Windows IE, Mozilla Firefox, Google Chrome, Opera.
Testing began with responsiveness around the navigation bar which performed as expected across all pages. I attempted to 
include a search function using PHP script within the navigation bar however this was decided against due to the complexity 
of the code and the requirement to ensure all relevant functionality was in place to ensure necessary submission grade was 
achieved. This feature was returned to in later versions using a separate approach. 
The carousel feature was then tested to ensure responsive across mobile, tablet, desktop and larger screens and the above-mentioned 
browsers. This performed as expected and remained responsive throughout site development. 
The Featured artists section was then tested which required some amendments to the code as I had initially intended on including two 
artists initially however decided to include three for increased content. The feature performed well upon updated container div.
The Map feature is a feature that is only available on desktop view and not a feature that is provided on mobile view. The functionality 
is now available on smaller screens and causes user inoperability die to the scale.
The Ticketmaster API Widget performs over all tested screen sizes and browsers and provides a good user experience due to its size and 
carousel of events.
Subscribe function required some fixes as the site progressed. Initially the subscribe function was floating left I then had to amend the 
display CSS to centre the content. The Mail.js API service is fully functional and users receiving a customised welcome mail upon entering 
their email address on site.
Footer remained responsive across all screen sizes and browsers.
The ‘What are you Sayin’ section of Social page utilises bootstrap for the functionality and has remained functional across all screens sizes 
and browsers tested.The events page Ticketmaster API required and initial learning curve however upon researching the implementation it was a correctly developed 
within the website. This API has remained responsive over all screen sizes and browsers tested.

## HTML/CSS-Validator

- HTML

Shows warning on across all pages related to text/javascript which states is not required however is neccessary for mail.js function
Errors showing on index.html related to Ticketmaster Widget which are necessary for Widget to function. Specific Error - 'W-type not allowed in div' at this point.
Warnings relating to comments -- however errors are necessary and do not affect functionality.
Warnings on event page relating to empty heading, JSON data fills empty heading and warning does not affect function for API.

- CSS 

No errors or warnings detected in CSS validator.

## Deployment

The site was deployed on Github and code is available to view using this site.
I navigated to my Github account, on the top left of the screen I selected my "Event-Planner" repository, 
I then deployed through the settings section by scrolling to the 'Github Pages' section roughly 3/4 of the 
way down the page. Selected my master branch as my source and my page was presented to me as


- Event-Planner : (https://karlitoyo.github.io/Event-Planner/)

**Cloning**

Can be achieved by selecting the green highlighted button which states - "Clone or Download" via the webpage: (https://github.com/Karlitoyo/Event-Planner) this will 
give the option of downloading a .zip file or opening in desktop an option to clone using HTTP is also given for cloning and running project locally through Gitpod. 
I make use of the git pull function (if required to update the branch) and git clone and then git push to named repository.

**Version-Control**

My versions overall style has remained largely the same throughout the development of the site.
My initial versions included a search function which would provide a visual search function through the Ticketmaster API’s JSON data. I began 
by researching PHP script to achieve this goal however time became a constraint and I was then forced to focus on the functionality I could 
manage before returning to this function. My next attempt at the search function was through ‘indexeddb’ which is an emerging tech utilising 
the browsers memory to index a database within the browser. This was initially successful as I created a search function and DB within the 
browser however I was unable to link the API JSON data to the db. My next attempt at the search function was related to ‘React’ and ‘Fetch’. 
I am currently researching this technology however due to time constraint I have been unsuccessful in implementing this feature in this version. 
I have included my code for review within app.js + search.js.


> # User-Stories

## First-User
First user found this navigation of the site to be fluid and easy to navigate. User commented on responsiveness of website on mobile device and desktop. 
User could easily navigate the events section and locate an act.

## Second-User
Second user found the site to be well developed and found the user comments on the Social page to be a good feature. User commented that map service was a 
great feature as it would provide the venue’s locational data to foreign holiday makers or users unfamiliar with the local terrain who wish to see a performance. 

## Developer comments
I will continue to develop this site to include a search function as the ‘React’ method to searching JSON data seems to be the complete method however has a large 
learning curve. I also would like to link the Ticketmaster API JSON data to the Google maps API showing the location of a searched event. Indexeddb is a further 
technology I am interested to develop.


> # Credits

Special thanks must be given to the creators of all the above and below mentioned sources I used to develop 'Event-Panner'.

## Credits

- Imran Sayed - Codeytek Academy (Youtube content creator channel for the React Search API function being developed)
- Hussein Nasser - (Youtube content creator channel for the Indexeddb function being developed)
- W3schools
- MDN
- https://rapidapi.com/blog/how-to-use-an-api-with-javascript/
- https://google.github.io/styleguide/jsguide.html
