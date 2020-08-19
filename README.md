# Intro and Strategy
This website is a Sports Memorabilia e-commerce website, where users can search through, leagues and teams memorabilia and buy them.
Users can create profiles which will save their billing info for future purchases and save their order history. The overall goal of the website
is to provide a platform for users to search for american sports memoribila and purchase it. 

# User Stories

## Story 1

A user will be able to search through the relavent leagues by team on the home page with a dropdown, scroll menu or through
the search bar both which are located on the home page of the website as shown in image a). Once they have selected a team or
searched for an item the merchandise will be layed out as seen on image b) i which users can selected their prefered merchandise
and be taken to the individual merchandise page as seen on images ci) cii). Here a user can choose the quantity they would like and add it
too their cart for purchase. viewing the cart will always be possible on all screens by clicking the cart link in the navagation bar
 and will look like image d). Users can then checkout by clicking the secur checkout button and be taken to the checkout page to
complete the form for payment as seen on image e). On this page they cna also save used info to their profile if they are logged in.
Finally once complete they will be taken to the order success page as seen on image f), which will have their order details,
billing address and a confirmation that they have been sent an email. 

### a)
![home page](./media/home-page.png)

### b)
![team page](./media/team-page.png)

### ci)
![merch-page1](./media/merch-page1.png)
### cii)
![merch-page2](./media/merch-page2.png)

### d)
![cart-page](./media/cart-page.png)

### e)
![checkout](./media/checkout.png)

### f)
![order success](./media/order-page.png)

## Story 2

User's can also create profiles which can be used to store billing info such as address and phone numbers and let the user view his order-history.
user just has to click register on the account section of the navbar and will be takento a register page as seen on image a) below. Once filled 
out they will need to confirm their email address and will then have the ability to add info to their profile. the layout for their profile page
can be seen in image b) with address info and personal info sections aswell as a button to take you to order history if they have one. 

### a)
![register](./media/signup-page.png)

### b)
![profile](./media/profile-page.png)

# Scope

The [landing-page](./media/home-page.png) provides the user with an oversite of the page aswell as navagation tools such as a search bar, accout management, link to view cart with updated grand total number. 
It also porvides the user wit hthe abiltiy to scroll through the various leagues teams to help the user narrow down his search. 

The [team-page](./media/team-page.png) provdies users with view of all merchandise realted to the team which they have navagated to. From here they can slect a merchandise whos details they want
to view, filter based on price, if its signed or game used merchandise. 

The [merchandise-details-page](./media/merch-page1.png) lets users get a more detailed look a the prodcut with description, price etc. They can also select a quantity and add it to the cart. 

The [cart-page](./media/cart-page.png) is where users can view what they've added to the cart already. It also allows users to update quantity or remove items form the cart. The link to checkout is 
also here for users whihc means the yhave to view the cart before proceeed to pay for it which is important. 

The [payment-page](./media/checkout.png) is where users fill out a form in order to finalise the purchase of their cart. billing info and personal info can be saved here to a profile if the user
is logged in or if they are not will ask them if they would like to register or log in.

The [order-confimred-age](./media/order-page.png) is jsut a page for the user to confirm his order went through, display the order details and confirm the email that the details had been sent too. 
There is also a link provided to return to shopping. 

The [register/login/logout](./media/signup-page.png) page does exactly as youd expect, all layouts are similar but only the registeration page is linked. 

The [profile-page](./media/profile-page.png) page is set up to let the user enter default info for future checkouts. It also provides a link to order-history.

The [order-history-page](./media/order-history.png) here a usre can view all of their previous orders including date, items order number and address for delievery.

# Structure 

Website is layedout with a navagaiton bar which is fixed with a lonk to return home on every page, a search bar, account help and a link to cart wtih updated total cost numbers. 
There is clear direction on the homepage on what the website's function is. The Website functionality is based around allowing users to purchase goods from the store so everything is 
tailored to lead towards adding items to carts and buying them. All merchanidse, filtering and navagaiton requirements as well as order info is stored in the django database as explained below. 

## The Database Structure
The main database models are Merchandise, Team, League, UserProfile (user) and orders. On the admin screen staff and superusers can add, delete, update and read merchandise, teams,
leageus and order info. For User info they can only see who is registered an account and their email but profile info can only be edited on the my profile page or if payment info is saved to profile.
The merchandise model is connected to the team modles through a foreign key aswell as the league. The team model has a foreign eky connection to the league model aswell. This allows 
merchandise to connec to the respective pages of the teams and leagues which helps searching for them. 
When an order is made if the user is logged the order will have a foreign key attaching to the user profile allowing the user to view the details in order history at anytime, if they are not logged in this
field will be left null.

### Merchandise

The Merchandise model as said before is connected to league and team. It also has boolean fields for game-used or if the merchandise is signed which is used for filters. Stock field prevents
users from entering larger quantity then what is in stock. Name and description fields can be used for search and we've made a custom sku for all merchandise. 

![merchandise](./media/merchandise.png)

### Teams and Leagues

Both the league and the team are used as ways of filtering merchanidse aswell as keys for the merchandise to be allocated correctly. In league there is a font-awesome class aswell 
for display purposes, in the team model nickname and images are fields, the nickname's to differnetiate the different teams from the same city and the images are used as background
for the team pages. 

![league](./media/league-admin.png)
![team](./media/team-admin.png)

### User Profiles and Orders 

The userProfile model is used to store the default address info and attach it to a certain user. The info can be entered in conjuntion with UserForm na dthorugh saved-info on the checkout page. 
Orders are marked with uniquely generated order-numbers, date of order, deleivery cost, order cost and total cost. Orders are linked by a user foreign key which is used to add order to histroy, if
the user is not logged in this will just be an empty field. orignal_cart and the character field stripe_pid garuntee that even if users make identical orders being logged in the database as individual orders. 
![Order](./media/order-admin.png)

# Skeleton 

[landing page](./media/wireframe-index.png) - stayed true to origial desgns on landing page except we added a container div with background image. 

[team page](./media/wireframe-team.png) - changed the payout of team page slightly moved everything into a container div with background image of the team and added a welcome banner.

[merch page](./media/wireframe-individual-merch.png) - changed up the individual page a good bit this was because once again a container div was added to help contrast becasue of hero-image. Descriptions were not
as neccassary for these sort of items so image became a larger part aswell. 

# Surface
Hero image and index-container image are supposed to add to the cheesy american feel to the website. The font Special Elite is also suppsoed to add to this casual and fun feel.
Every team page has a background image of the team's logo aswell as a welcome banner to leave the user in no doubt what team merchandise they are browsing. 


# Features

# 1)
Users can browse through merchandise with the ability to  add to, update quantity, remove and view mechandise in cart. Payments can be made
for cart item with all fields that are required are submitted. 

# 2)
Profiles can be made to which cusotmers can pre-add billing info and look at their order-history.

# 3) 
If the profile logged in is a superuser or staff memeber they can access the admin page thorugh the management option in accounts nav, here they can 
 add, delete, update merchandise, team, league and check order info.

## Future Features

#### 1) Stock management

We would have liked to completed the features regarding stocks for the merchandise, such as removing purhcased quantity form stock and fixing bugs that allow more then the amount of stock to be added 
to cart but time was an issue here so we removed attempts to do this and hopefully will be added at a future date. 

#### 2) Favourite teams for user profile
Origianlly the userProfile model had favourtie team as a field but it was removed as once agian time constriants didnt allow us to fully use the function. We where
hoping to add background images on all profile pages of favourte team image aswell as maybe emails to users if stock was added of their favourite team. 

# Technologies 

1) HTML

2) CSS

3) Django

4) Python

5) Javascript
 
6) Bootstrap

7) Stripe

8) AWS

# Testing

Display, images and links worked fine on google chrome, firefox and microsoft edge. 
Used W3 validator for css and html and the pep8.com to check the python was displayed up 
to standard. On each browser check we tested on mobile view(iphone 6/78), ipad view on 
both rotations and on general browser view. On Checkout views.py, webhookhandler.py, 
webhooks.py and in setting.py all have one or two lines that are two long accoridng to pep8 but 
we determined that for readability and functionality that those respective lines would be left as is. 

All forms and links where tested manually and worked. Forms from the profile linked up nicely with checkout, payments went through
with correct response from webhooks and the order info was succesfully stored. 
Emails where sent for verification and on payment completion. Multiple practice accounts where setup successfully 
aswell with logout, login, password change and if authroised link to admin all functioning. 


# Deployment

The project was completed on gitpod and deployed on heroku. To connect our gitpod to heroku we
first created an app which we called ‘united-states-of-sports’. After this we associate the heroku
app with our master repository so that we can push our work on to Heroku. For this to work we had
to first create a Procfile in gitpod which is like an instructor to heroku on which files it needs
to run the project. 

All static files where stored on AWS in which the s3 bucket was connected through aws-access-key and
aws-secret-key on heroku. 

# Credits and Acknowledgements

Stripe documentation was used to help set up the stripe payments particularily the documentation on webhooks and
accepting payments linked [here](https://stripe.com/docs/webhooks/build) [here](https://stripe.com/docs/payments/checkout/accept-a-payment) respectively.

Django basics on Geeks for geeks was used to help with understanding of django linked [here](https://www.geeksforgeeks.org/django-basics/?ref=leftbar-rightbar)

Bootstrap documentation was used for navbars, scroll functions, template layout and for margins and paddings linked [here](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

For jinja realted issues and for many other small coding problems stack overflow proved to be a valuable asset. linked [here](https://stackoverflow.com/questions/26184070/return-a-conditional-if-statement-based-on-list-length) is
an example of how we fixed an if statement problem.

Testing emails for confirmation, vladiation and order summarys where checked with help of temp emails linked [here](https://temp-mail.org/en/)

AWS was used to store static files and media files linked [here](https://aws.amazon.com/free/?trk=ps_a131L0000085EJvQAM&trkCampaign=acq_paid_search_brand&sc_channel=ps&sc_campaign=acquisition_US&sc_publisher=google&sc_category=core-main&sc_country=US&sc_geo=NAMER&sc_outcome=acq&sc_detail=aws&sc_content=Brand_Core_aws_e&sc_segment=432339156150&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Core-Main|Core|US|EN|Text&s_kwcid=AL!4422!3!432339156150!e!!g!!aws&ef_id=CjwKCAjwm_P5BRAhEiwAwRzSO-e7eHWcphM6XbucO1BYMteUtdIM89kcsFTxevZIPj3-qhH031zLMRoC5t0QAvD_BwE:G:s&s_kwcid=AL!4422!3!432339156150!e!!g!!aws&all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc)

All Merchandise info was pulled from sportsmemorabilia.com including images linked [here](https://www.sportsmemorabilia.com/)


# Media

All teams images came from google searches

hero image and home page container image where pulled form google searches
