# LogInSystem
Python Log In System with GUI

# Login Application

This project is a Python-based graphical user interface (GUI) application for user login and signup, built using the Tkinter library. It allows users to register and log in with their credentials, storing user data in a local file. This application is suitable for learning purposes and small-scale projects.

# Features

User Login: Users can log in using their username and password.

User Signup: New users can register by providing a username and password, which are stored locally in a datasheet.txt file.

Data Persistence: User credentials are stored in a text file using Python's ast module to handle dictionary serialization.

Graphical Interface: Intuitive and user-friendly GUI designed with Tkinter.

----------------------------------------------------------------------------

The main window will display a login screen.

If you don't have an account, click on "Sign up" to register.

After registering, you can log in with your credentials.

File Structure

app.py: Main Python script containing the application logic.

datasheet.txt: File to store user data (created automatically upon first signup).

login.png: Image used in the GUI (ensure this is in the same directory as app.py).

Screenshots

Login Screen

A clean and simple interface for users to enter their credentials.

Signup Screen

Allows new users to register by entering a username and password.

# Code Overview

Login Functionality

Validates user input.

Checks if the provided username and password match stored credentials in datasheet.txt.

Displays an error message for invalid credentials.

Signup Functionality

Ensures all fields are filled and passwords match.

Stores new user credentials in datasheet.txt.

Creates the file if it doesn't already exist.

# Important Notes

Security: This application is for educational purposes. Do not use it for real-world applications without implementing proper security measures like password hashing and encryption.

Error Handling: Basic error handling is implemented. Ensure datasheet.txt is not manually edited to prevent application crashes.

# Contributing

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss your ideas.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Author

Triñanes, Tristan Jay
# 
Thank you for using this login application! If you have any feedback or issues, please feel free to open an issue on GitHub.
