# mdb-Project-3

This project focuses on using python flask to connect MongoDB. The website was build with the intention to bring people of different backgrounds and hobbies together. The website is designed to be intuitive and easy to navigate. It is targeted towards people who are looking for a partner in crime.  

## Demo

A live demo of the website can be found here: https://angie-database-project.herokuapp.com/


## Project Strategy and Scope
### User Stories

| User Stories        | Description           | Features to implement  |
| :------------- |:-------------| :-----|
| 1      | User would like to register| To include a registration form.  |
| 2      | User would like to update profile. | To include a form that lets the user update their profile.  |
| 3      | User would like to see potential matches  | To include a page full of potential matches that the user can choose from. These matches have been pulled from MondoDB  |
| 4      | User would like to see matches according to gender | To include a search filter that allows user to search by gender   |

## Project Structure
### (i) Overview
- Homepage - The homepage is fairly simple and straightforward to use. Users can register on the site before they are able to contact matches. From the homepage/landing page, they will be able to register their profile and search for matches. 

- Register page - With the register page, users will be able to register their profile. Once they have submitted their information, they will be redirected to their profile page. This information will also be sent to MongoDB. 

- Profile page - The profile page will showcase the information that the user entered into the register page. When they get to the profile page, the user will have the option to update their profile. After doing so, they will be redirected to the profile page with the updated information. 

- Update profile page - With the update profile page, users will be able to update their profile with ease and read the information they updated on their profile page. 

- Find Matches page - The matches page will showcase all the potential matches that the user can choose from. Users can delete the matches (this is to showcase the delete function).


### (ii) Wireframes here.
View wireframes for both desktop and mobile here:
https://drive.google.com/file/d/18nfM9JNUAi6mCA63bKsiRqSRWRZ4t08Y/view?usp=sharing

## Project Skeleton
### (i) Existing Features
- Landing page - The parallax images in the landing page gives users an overview of the site's function. There is also a short blurb that summarises the site's function. The navbar is simple to use, user's can easily register their profile to get started, or simply view the potential matches. If they want to return to the landing site, all they have to do is click home.

-  Find Matches page - Bootstrap features like cards were used to organise the matches. This makes the information displayed organised and neat. This will also allow the users to navigate with ease and see each match. 


### (ii) Features to implement in the future
In the future, I would like the website to have a login and logout function. This will enable returning, registered users to access their profile easily, without having to re-register all over again. Another thing I would like to implement is a functioning feedback or contact form for users to use. Including a more comprehensive search filter that filters according to age, location, etc would improve the site's user experience as well. Finally, I would like to add a delete profile option for users.  

### Limitation 
Registered users will not be able to see their profile when they enter the site. There is no login or logout function, hence a registered user will not be able to pull his/her information from the database. Users will not have an option to delete their profile. Although there is a link for users to send a message to the matches, this link doesn't work, it is only there as a means of display. 

## Project Surface
### Design Choices
(i) The colour scheme of header text and the nav bar is intended to make the title of the website stand out. 
(ii) The nav bar text changes colour when user hovers over the text. This will show them that the text is a clickable link. (iii) When the mouse hovers over the text, the cursor changes to further indicate that the link is clickable.  
(iv) The background image is attractive and colourful, so as to draw the user's eye. 
(v) The overall colour scheme was chosen to exude a romantic and relaxed vibe. 
(vi) The colour of the text box in the middle and the font colour of the text inside the box matches the colours of the background image. 
(vii) Included two parallax images in the landing page to give the website more depth. 


## Technologies

1. HTML (link to the documentation: https://devdocs.io/html/)
HTML was used to structure the content of the website.
2. CSS (link to the documentation: https://devdocs.io/css/)
CSS was used to style the website.
3. Bootstrap (link to the documentation: https://getbootstrap.com)

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
| 1      | When user hovers over the text on the header text , it will change colour. Additionally, hovering over the text will change the cursor to show users that it is a clickable link. | Pass  |
| 2      | When user clicks on the register link, they will be redirected to a form that allows them to register their profile. | Pass  |
| 3      | When user clicks on the matches link, they will be able to see the potential matches.| Pass  |
| 4      | User will be able to update their profile in the profile page. | Pass  |
| 5      | User will be able to delete matches. | Pass  |

## Bugs Discovered
No bugs found. 

## Deployment
My code was written using AWS. AWS serves as the local repository before it is deployed to GitHub. New commits made on the master branch will update the deployed site in real time. I add new changes and commit them in bash in AWS, before git pushing it to my GitHub. After all the changes have been made, and I'm done making minor changes to my project, I type git push heroku master into the bash so that my code is deployed in Heroku.

To access my project in GitHub, I will find it under Repositories to check if all my commits are up-to-date. To access my project under Heroku, I will select angie-database-project (the app name I provided for Heroku) and view my project. When I click angie-database-project, it will redirect me to another page that records all my activity. On the top hand side, there is an open app button that will let me access my website. 

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


