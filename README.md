# mdb-project-3

The website, which utilises python flask and MongoDB, functions much like a dating website that connects people of different backgrounds and hobbies. The user interface and experience of the website has been improved to allow users to interact with the website easily.

# Revisions Made/Features Added

## Login Function
- Data integrity and user authentication has been implemented.
- Views are filtered based on user authentication status.

## Send Messages Function
- Logged in users are able to send messages to their matches. 

## Demo

A live demo of the website can be found here: https://angie-database-project.herokuapp.com/


## Project Strategy and Scope
### User Stories

| User Stories        | Description           | Features to implement  |
| :------------- |:-------------| :-----|
| 1      | User would like to login| To include a login function that allows users to login.  |
| 2      | User would like to register| To include a registration form.  |
| 3      | User would like to update profile. | To include a form that lets the user update their profile.  |
| 4      | User would like to see matches in the database  | To include a page that displays all the matches on the website. |
| 5      | User would like to see matches according to gender | To include a search filter that allows user to search by gender   |
| 6      | User would like to send a message to their chosen match | To include a send message link  that redirects the user to a message textbox, which enables users to send a message to their match. |

## Project Structure
### (i) Overview

- Homepage - The homepage has a navbar that allows users to navigate in and around the site.

- Login page - The login page will allow users to login into the site

- Register page - With the register page, users will be able to register their profile.

- Profile page - The profile page will showcase the information that the user entered into the register page. 

- Find Matches page - The matches page will showcase all the matches on the database. 

### (ii) Wireframes here.
View wireframes for both desktop and mobile here:
https://drive.google.com/file/d/18nfM9JNUAi6mCA63bKsiRqSRWRZ4t08Y/view?usp=sharing

## Project Skeleton
### (i) Existing Features

- Homepage - Users can use the navbar to login or register on the site before they are able to view or contact the matches on the site. 

- Login page - Once a user logs into the site, he/she will be able to see their profile page and matches page.

- Register page -  Once users have submitted their information, they will be redirected to their profile page. This information will also be sent to MongoDB. 

- Profile page - When users get to the profile page, they will have the option to update their profile. After doing so, they will be redirected to the profile page with the updated information. 

-  Find Matches page - Bootstrap features like cards were used to organise the matches. This makes the information displayed organised and neat. This will also allow logged in users to navigate the site with ease and see each match. Only logged in users can send messages and delete the matches.


### (ii) Features to implement in the future
In the future, I would like to implement is a functioning feedback or contact form for users to use. Including a more comprehensive search filter that filters according to age, location, etc would improve the site's user experience as well. Finally, I would like to add a delete profile option for users.  

### Limitation 
Users do not have an option to delete their profile. 

## Project Surface
### Design Choices
(i) The colour scheme of header text and the nav bar is intended to make the title of the website stand out. 
(ii) The nav bar text changes colour when user hovers over the text. This will show them that the text is a clickable link. (iii) When the mouse hovers over the text, the cursor changes to further indicate that the link is clickable.  
(iv) The background image is attractive and colourful, so as to draw the user's eye. 
(v) The overall colour scheme was chosen to exude a romantic and relaxed vibe. 
(vi) The colour of the text box in the middle and the font colour of the text inside the box matches the colours of the background image.


## Technologies

1. HTML (link to the documentation: https://devdocs.io/html/)
HTML was used to structure the content of the website.
2. CSS (link to the documentation: https://devdocs.io/css/)
CSS was used to style the website.
3. Bootstrap (link to the documentation: https://getbootstrap.com)
4. Python Flask was used to get the website working (link to the documentation: https://flask.palletsprojects.com/en/1.1.x/)

## Testing
(i) Mobile Responsiveness

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)

Website tested on mobile and on laptop mode : 

https://drive.google.com/open?id=1eRh_Z2AnyFMRqjL-4rVMMnBLnFnaqBDk

(ii) Browser Compatibility

This site was tested across multiple devices multiple mobile devices 
(iPhone 4, 5, 7: Chrome and Safari, iPad, Samsung Galaxy) to ensure compatibility and responsiveness.)


(v) Test Cases 

| Test Case(s)        | Description           | Outcome |
| :------------- |:-------------| :-----|
| 1      | When user hovers over the text on the navbar text , it will change colour. Additionally, hovering over the text will change the cursor to show users that it is a clickable link. | Pass  |
| 2      | When a user clicks on the register link, they will be redirected to a form that allows them to register their profile. | Pass  |
| 3      | Only logged in users clicks on the matches link, they will be able to see all the matches.| Pass  |
| 4      | Only logged in users will be able to update their profile in the profile page. | Pass  |
| 5      | Only logged in users will be able able to access the matches page. | Pass  |
| 6      | Only logged in users will be able to send messages to matches and delete messages. | Pass  |


## Bugs Discovered
No bugs found. 

## Deployment
My code was written using AWS. AWS serves as the local repository before it is deployed to GitHub. New commits made on the master branch will update the deployed site in real time. I add new changes and commit them in bash in AWS, before git pushing it to my GitHub. After all the changes have been made, and I'm done making minor changes to my project, I type git push heroku master into the bash so that my code is deployed in Heroku.

To access my project in GitHub, I will find it under Repositories to check if all my commits are up-to-date. To access my project under Heroku, I will select angie-database-project-3 (the app name I provided for Heroku) and view my project. When I click angie-database-project-3, it will redirect me to another page that records all my activity. On the top hand side, there is an open app button that will let me access my website. 

### Acknowledgements

W3Schools: To format background image.
https://www.w3schools.com/cssref/pr_background-image.asp

Pexels: To choose photos for matches profile.
https://www.pexels.com/

Stackoverflow:

1. Changing text color on hover then having it change back to the original colour.
https://stackoverflow.com/questions/3741157/change-background-color-on-mouseover-and-remove-it-after-mouseout

Google Fonts: For fonts.
https://fonts.google.com/

Bootstrap: For button, forms, cards, navbar.
https://getbootstrap.com/docs/4.4/components/buttons/

Python Flask documentation for login features:

https://flask.palletsprojects.com/en/1.1.x/
