## Simple Dynamic Website
This is a simple dynamic website that allows users to transfer money between multiple customers. The website is designed to handle up to 10 customers and record all transfer transactions in a database. There is no login page or user creation functionality included in this website.

### Features
Home Page: The landing page of the website.
View all Customers: Displays a list of all the customers in the database.
Select and View one Customer: Allows users to view the details of a specific customer.
Transfer Money: Enables users to transfer money from one customer to another.
Select customer to transfer to: Provides a list of customers to choose from for transferring money.
View all Customers: Displays the updated list of all customers after a transfer transaction.
Database
The website requires a database to store customer information and transfer records. You can choose from various database options such as MySQL, MongoDB, or Postgres. For this project, you need to create a database with a table named "Customers" and a table named "Transfers".

The "Customers" table should include the following fields:

Name: The name of the customer.
Email: The email address of the customer.
Current Balance: The current balance of the customer.
The "Transfers" table should record all transfer transactions and include the following fields:

Sender: The customer who sent the money.
Receiver: The customer who received the money.
Amount: The amount of money transferred.
Timestamp: The timestamp of the transfer.
Please make sure to populate the "Customers" table with dummy data for up to 10 customers.

### Hosting
You can choose any free hosting provider to host the website. Some popular options include 000webhost, GitHub Pages, Heroku, or GitLab Pages. Simply create an account with the hosting provider of your choice, follow their instructions to deploy the website, and make sure to check in your code to GitLab or any other version control system.

### Instructions
Set up a database of your choice (MySQL, MongoDB, Postgres, etc.) and create the necessary tables ("Customers" and "Transfers").
Populate the "Customers" table with dummy data for up to 10 customers.
Implement the website with the specified features using HTML, CSS, and JavaScript.
Connect the website to the database and write the necessary code to perform transfer transactions and update the customer balances.
Deploy the website to your chosen hosting provider (000webhost, GitHub Pages, Heroku, etc.).
Check in your code to a version control system such as GitLab.
Additional Notes
Make sure to include any necessary dependencies or libraries in your code.
Test the website thoroughly to ensure all features are working as expected.
Consider adding error handling and validation to enhance the user experience.
Update the README file with any specific deployment or setup instructions for your chosen hosting provider.
Happy 