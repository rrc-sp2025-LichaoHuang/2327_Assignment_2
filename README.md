# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Lichao Huang

## Assignment 1
Assignment 1: This assignment will produce some foundational classes to be used in an overall system. The classes will incorporate the outcomes associated with Module 01. Specifically, these classes will incorporate encapsulation through the use of private attributes and public accessors and mutators. Additionally, these classes will benefit from thorough unit testing, including unit test planning. Keep in mind that the classes developed in this assignment will contribute to upcoming assignments. Choosing appropriate identifiers and having comprehensive documentation will be of great importance as the overall project grows and changes throughout the semester.


## Encapsulation
In this assignment, I used self.__ to encapsulate two classes, ensuring that the data within each class cannot be accidentally referenced by other classes. I also wrote accessors for each class to access the data, ensuring that the data within the class cannot be arbitrarily modified.

#########################################################################################################################################################

## Assignment 2
Assignment 2: This assignment builds on the basic BankAccount class by adding Chequing, Investment, and Saving accounts. Each subclass implements its own service charge rules using inheritance and polymorphism. Encapsulation is kept with private attributes, and clear docstrings are added for readability and maintainability.

Since assignment 2 is saved in another repository, there is no step of creating a branch at the beginning of the job and merging the branches at the end.


## Strategy Pattern

In this project, I learned how to use the Strategy Pattern in a simple and practical way. The main idea is to separate the logic for calculating service fees from the main account classes. Instead of writing all the fee rules inside each class, I created different strategy classes like OverdraftStrategy, ManagementFeeStrategy, and MinimumBalanceStrategy. Each account type — Chequing, Investment, or Saving — uses one of these strategies to calculate its service charges.

When the program runs get_service_charges(), the account doesn’t do the math by itself. It simply asks its strategy object to handle it.

While testing, I ran into an error with the SavingAccount class. I accidentally passed a string like "aa" as the minimum balance, and the test crashed because it couldn’t convert it to a number. I realized I forgot to add a default value when the input was invalid. After fixing it by setting a default of 50, everything worked fine and all tests passed.


## Observer Pattern

During Part 2 of the assignment, I worked on implementing the Observer Pattern. At first, I was quite confused about how the different components interacted, especially the relationship between the Observer (Client) and the Subject (BankAccount). I initially tried to directly connect the Client and the BankAccount classes, not realizing that their communication should happen through the Subject-Observer mechanism rather than by directly referencing each other.

Another major source of confusion was the simulate_send_email function. I didn’t immediately understand that it doesn’t actually send real emails—it just simulates the process by writing the notification messages into a text file (observer_emails.txt) inside the output directory. Because of that, I spent quite a while trying to figure out why “no notification” seemed to appear, when in fact, the results were quietly being written into a file.

After understanding this, everything made sense:

BankAccount (as a Subject) tracks its observers and notifies them when certain conditions occur (like a large transaction or low balance).

Client (as an Observer) receives those notifications through its update() method, which uses simulate_send_email to log the messages.

This part taught me how the Observer Pattern helps separate responsibility between data changes and how those changes are communicated.

## Assignment 4


Assignment 4: [Indicate the name and description of the current assignment]