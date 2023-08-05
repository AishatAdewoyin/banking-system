### INTERNSHIP & MENTORSHIP (Mentor: Martha Kaburi) on: 


## Dynamic Banking Website
A simple and dynamic website that allows users(bank system admins) to transfer money between multiple customers. This website is designed to handle up to 10 customers and record all transfer transactions in a database. There are login pages & user creation functionality included in this website.


### The Features
Home Page: The landing page of the website.
View all Customers: Displays a list of all the customers in the database.
Select and View One Customer: Allows users to view the details of a specific customer.
Transfer Money: it will enable users to transfer money from one customer to another.
Select customer to transfer to: Provides a list of customers to choose from for transferring money.
View all Customers: Displays the updated list of all customers after a transfer transaction.

Database
The website requires a database to store customer information and transfer records. I'm using PostgreSQL. For this project, I will create a database with a table named "Customers" and a table named "Transfers".

The "Customers" table will include the following fields:

Name: The name of the customer.
Email: The email address of the customer.
Current Balance: The current balance of the customer.
The "Transfers" table will record all transfer transactions and include the following fields:

Sender: The customer who sent the money.
Receiver: The customer who received the money.
Amount: The amount of money transferred.
Timestamp: The timestamp of the transfer.
Making sure I populate the "Customers" table with dummy data for up to 10 customers.

### Hosting
Using any of 000webhost, GitHub Pages, Heroku, or Netlify.

