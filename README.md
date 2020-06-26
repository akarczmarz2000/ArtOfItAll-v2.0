# Art Of It All - v2.0
This is a recreation of one of my previous projects. 
The idea of this is displaying art from different artists for sale. 
Also, allowing customers to make personal requests for pieces of art they would like made. 
The site would also be an opportunity to help the artist get a foothold in the industry, 
for exposure and learning how to handle these types of situations before doing it on their own. 
The interaction I want for this are:-

* I'd like to have a market bag to show all products
* I'd like users, artist and the owner to be able to sign in to the page
* I'd like to send emails at specific times, after registration and check out

# UX
## User Story
This link goes to a sheet for user stories - [Art Of It All - User Story](https://docs.google.com/spreadsheets/d/1Xfan3NTHD1KlfTOiNTYsND1w7PdOSklX85RNjhFjeRc/edit?usp=sharing)

## Wireframe
### Home Page Wireframe
![Home Page Wireframe](/assets/Home.png)
### Products Page Wireframe
![Products Page Wireframe](/assets/Products.png)
### Artists Page Wireframe
![Artists Page Wireframe](/assets/Artists.png)
### Request Page Wireframe
![Request Page Wireframe](/assets/Request.png)
### Chat Select Page Wireframe
![Chat Select Page Wireframe](/assets/Chat-Select.png)
### Chat Page Wireframe
![Chat Page Wireframe](/assets/Chat.png)
### Policies Page Wireframe
![Policies Page Wireframe](/assets/Policies.png)
### Profile Page Wireframe
![Profile Page Wireframe](/assets/Profile.png)
### Edit Profile Page Wireframe
![Edit Profile Page Wireframe](/assets/Edit-Profile.png)
### Sign In and Up Pages Wireframe
![Sign In Page Wireframe](/assets/Sign-In.png)
![Sign Up Page Wireframe](/assets/Sign-Up.png)
### Checkout Pages Wireframe
![Checkout Page Wireframe](/assets/Checkout.png)

## Mockup 
![Art Of It All Colour Mockup](/assets/ArtOfItAll_color_mockup.psd.png)

# Features of the site
## Features
### UX Features
* Sticky bar at the top with navigation bar, site title, company logo, 
page title, checkout button, sign up and sign in button 
* Sign In that will allow people to login with an account made on the page
* Sign Up that allows people to create an account for the page
* Has a link to chats that people have because of requests
* Has checkout total and link to total bag
* Page structure for multiple screen sizes made by Bootstrap
* Links to the products page that has a drop down for different art types
* Links to artist of certain type of art
### Home Features
* Slide with art with the tag popular cycling through
* Show a list of popular art displayed in row of 4 on normal screen,
 2 on smaller and 1 on smallest
* Allow to refine popular by category and sort by different options
### Products Features
* Picture of the art displayed in a grid with the product name above, 
price across the bottom of the picture and description underneath the picture
* A filter section on the top of the page, this will be sticky underneath the main bar
* The user will be able to filter by category and search bar
* The user will be able to sort by different varibles like rating, alphabet ect
* Clicking the picture will show more information about the image on a new page
* When the add button is clicked the corrisponding is added to basket
* Search results will be displayed before image, 
with the keyword and number of results returned
* The user will be able to choose a size and quantity before adding product to there bag
### Policies Features
* The page will have three titles. Purchase, request and chat policies
* These titles will have a download link to a copy of the policies
* Underneath the titles will be a description 
### Request Features
* A form with a dropdown input with all the different artist and the help department
* The form will have a name box for the person using it
* The form will have a box for the request they want to put in, 
the text in there before they start typing will be an example
### Chat Features
* The chat selection page will have a table of all chats made for requests
* The table will show date of request, artists name, 
a link to the chat and the chats current status
* The chat page will have a box for the user to write what they want to say
* Sent messages will have a time stamp and will have the senders name
* Sent messages will have the content of what was sent
### Artists Features
* Will have a picture of the artist if availible 
or picture of there art if not possible
* A title will have artist name and art type/s
* Underneath will be a description of the artist and there work
### Checkout Features
* Will have all the items in the current basket
* These items will have a description, product name, quantity and size
* A total will be displayed after all the products
* A checkout/pay button will be under that
### Profile Features
* Will have a photo the user can choose 
(will be default till they change it)
* Will show the users name, 
saved address and save billing information
* Underneath the user information will be previous orders 
and request information in a table
* The table order history will show order date, product name/s, 
overall price and link to more details
* The table request history will show request date, artist name,
agreed price abd link to more details
* Edit profile button
* The edit page will display all already know information and 
will allow the user to edit any of there except username
### Sign In
* Will ask for username and password
* Will use allauth to authenticate
### Sign Up
* Will ask for some details like name, username, password ect to create account
* Will send confirmation email that they need to access before they are able to enter the site

## Features Left to Implement
### UX Features
* Sticky bar at the top with navigation bar, site title, company logo, 
page title, checkout button, sign up and sign in button 
* Sign In that will allow people to login with an account made on the page
* Sign Up that allows people to create an account for the page
* Has a link to chats that people have because of requests
* Has checkout total and link to total bag
* Page structure for multiple screen sizes made by Bootstrap
* Links to the products page that has a drop down for different art types
* Links to artist of certain type of art
### Home Features
* Slide with art with the tag popular cycling through
* Show a list of popular art displayed in row of 4 on normal screen,
 2 on smaller and 1 on smallest
* Allow to refine popular by category and sort by different options
### Products Features
* Picture of the art displayed in a grid with the product name above, 
price across the bottom of the picture and description underneath the picture
* A filter section on the top of the page, this will be sticky underneath the main bar
* The user will be able to filter by category and search bar
* The user will be able to sort by different varibles like rating, alphabet ect
* Clicking the picture will show more information about the image on a new page
* When the add button is clicked the corrisponding is added to basket
* Search results will be displayed before image, 
with the keyword and number of results returned
* The user will be able to choose a size and quantity before adding product to there bag
### Policies Features
* The page will have three titles. Purchase, request and chat policies
* These titles will have a download link to a copy of the policies
* Underneath the titles will be a description 
### Request Features
* A form with a dropdown input with all the different artist and the help department
* The form will have a name box for the person using it
* The form will have a box for the request they want to put in, 
the text in there before they start typing will be an example
### Chat Features
* The chat selection page will have a table of all chats made for requests
* The table will show date of request, artists name, 
a link to the chat and the chats current status
* The chat page will have a box for the user to write what they want to say
* Sent messages will have a time stamp and will have the senders name
* Sent messages will have the content of what was sent
### Artists Features
* Will have a picture of the artist if availible 
or picture of there art if not possible
* A title will have artist name and art type/s
* Underneath will be a description of the artist and there work
### Checkout Features
* Will have all the items in the current basket
* These items will have a description, product name, quantity and size
* A total will be displayed after all the products
* A checkout/pay button will be under that
### Profile Features
* Will have a photo the user can choose 
(will be default till they change it)
* Will show the users name, 
saved address and save billing information
* Underneath the user information will be previous orders 
and request information in a table
* The table order history will show order date, product name/s, 
overall price and link to more details
* The table request history will show request date, artist name,
agreed price abd link to more details
* Edit profile button
* The edit page will display all already know information and 
will allow the user to edit any of there except username
### Sign In
* Will ask for username and password
* Will use allauth to authenticate
### Sign Up
* Will ask for some details like name, username, password ect to create account
* Will send confirmation email that they need to access before they are able to enter the site

## Existing Features

# Technologies Used

# Deployment

# Credits

# Content

# Media

# Acknowledgements
The idea for the user story layout came from Chris Z