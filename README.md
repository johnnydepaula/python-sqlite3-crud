Developing a simple CRUD class to
manipulate a small Calendar database,
that will follow the schema bellow:

     _______________________________________________
    | id | first_name | last_name | email | number |
    -----------------------------------------------
                                            v1.0.0

We'll use SQLite to create and manipulate
the database tables. This could be leveraged
to a larger database, for example: MySQL, Postgres...
    Now that we have created this database schema, it's
a good practice to think about the Normalization and
relationship between the tables. With some thinking we
should be considering move email and phone numbers
to another tables, since our user could benefit from
having multiple emails and phone numbers.
    We shal end with a schema like this:

         ______________________________
        | id | first_name | last_name |
        ------------------------------
        id       -> PRIMARY KEY

         _______________________________
        | id_email | email_adress | id |
        -------------------------------
        id_email -> PRIMARY KEY
        id       -> FOREIGN KEY

         _______________________________
        | id_phone | phone_number | id |
        -------------------------------
        id_phone -> PRIMARY KEY
        id       -> FOREIGN KEY
                                v1.0.1,

where Agenda has a 1:N relationship with both
Email and Phone tables.