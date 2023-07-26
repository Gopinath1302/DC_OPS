# Pet Adoption

This application named Adams Pet Shop invites a user to create a account before visiting the pet shop.

## Version 1.0:

### Database Connectivity:

The database creation is currently at this Python code. Later the code will be sent to the Database and
This is the initial stage of the application.

![Table Creation and Database Connectivity](https://i.ibb.co/3T7dyhX/User-Login.png)

### Credential Validation:

In this application, the credentials validation does not take place.
It accepts every character possible that is input but, it cannot contain duplicate values.

### Program Flow:

After successful account creation, the user can login.
If they are already existing customer, they can press Enter in username and move on to login.

After login, the application shows the list of pets available.

After showing the details, it redirects to booking page and makes the user to enter the day number that is remaining in this month.
After booking completes, it voluntarily logs out and makes user to quit the application.
During logout, the application sends the data containing Username with Timestamp to the database.

## Version 2.0:

### Updates:

- Login Page Reworked
- Admin Login Added
- Connection with List and Booking has been removed.
- These are created without OOPs concept
