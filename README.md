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
can be seen in image b) with address info and perosnal ifo sections aswell as a button to take you to order history if they have one. 

### a)
![register](./media/signup-page.png)

### b)
![profile](./media/profile-page.png)

# Scope

# Structure

## The Database Structure
The main database models are Merchandise, Team, League, UserProfile (user) and orders. On the admin screen staff and superusers can add, delete, update and read merchandise, teams,
leageus and order info. For User info they can only see who is registered an account and their email but profile info can only be edited on the my profile page or if payment info is saved to profile.
The merchandise model is connected to the team modles through a foreign key aswell as the league. The team model has a foreign eky connection to the league model aswell. This allows 
merchandise to connec to the respective pages of the teams and leagues which helps searching for them. 
When an order is made if the user is logged the order will have a foreign key attaching to the user profile allowing the user to view the details in order history at anytime, if they are not logged in this
field will be left null.

### Merchandise

![merchandise](./media/merchandise.png)

### Teams and Leagues

### User Profiles and Orders 

# Skeleton 

[index page](./media/wireframe-index.png)

[team page](./media/wireframe-team.png.png)

[merch page](./media/wireframe-individual-merch.png)

# Surface

# Features

## Future Features

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

# Deployment

# Credits

# Acknowledgements

# Media
