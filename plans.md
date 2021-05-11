# Pages:
## index.html 
Main landing page defaults to login with some basic information about the site
### Contains:
Login form
Link to sign up
Link to Owner sign up

## register.html
Main page to signup
### Contains:
Sign up form
Link back to log in page

## dashboard.html
Main landing page after login/register
### Contains:
Main navigation including a log out button
#### navigation:
logout
view shops
all items

## product.html?
Single product view

## shop.html
View information about specific shops and their items


# Tables:
## User ERD
### Register shop owner?
username = username
first name = firstName
last name = lastName
email = email
password = password
shop name = shopName

### register general user?
username = username
first name = firstName
last name = lastName
email = email
password = password

### login
username
password


## Product ERD
product = itemName
description = itemDescription
price = itemPrice
quantity = itemCount
shop name = [drop down with shopNames to ensure it goes to the right one]
