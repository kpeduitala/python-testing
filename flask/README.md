# Flask CRUD

## Description

This project is a Flask web application that allows users to sign up, log in, and manage data through CRUD (Create, Read, Update, Delete) operations. The application uses an SQLite database to store user credentials and data entries.

## Features

- User Authentication:
  - Sign up: Users can create a new account.
  - Log in: Users can access their account.
  - Log out: Users can sign out of the application.
- Data Management:
  - Create: Add new data entries.
  - Read: View a list of existing data entries.
  - Update: Modify existing data entries.
  - Delete: Remove data entries.
- Responsive UI with Bootstrap.

## Configuration

1. Create a `.env` file in the root directory.
2. Add your secret key to the `.env` file:
   ```
   SECRET_KEY=your_secret_key_here
   ```

## Database Setup

To set up the database, run the `db_setup.py` script:

```sh
python db_setup.py
```

This script will create an SQLite database file named `database.db` with the required tables.

```
Database: database.db

Table: users
+------------+-------------+
| Column     | Type        |
+------------+-------------+
| id         | INTEGER     |
| username   | TEXT        |
| password   | TEXT        |
+------------+-------------+

Table: data
+------------+-------------+
| Column     | Type        |
+------------+-------------+
| id         | INTEGER     |
| product    | TEXT        |
| quantity   | INTEGER     |
| price      | REAL        |
+------------+-------------+
```

## Running the Application

To run the application, use the following command:

```sh
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Note on Application Flaws

Intentional Flaws: This application intentionally contains certain flaws or areas that may require improvement or bug fixes. These have been left as part of the project to encourage users to identify and document them as part of their testing and documentation process.

These intentional flaws might include, but are not limited to:

- Potential security vulnerabilities.
- Inefficiencies in code logic.
- User experience issues.
- Error handling deficiencies.

Users are encouraged to thoroughly test the application and document any identified flaws or improvement areas in the test documentation or issue tracker.
