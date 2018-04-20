# intro_to_django
Code based from Pretty Printed tutorial on introduction to Django.

The goal of Form_testing is to create a flexible form meant to be used as a workaround for User input in Tableau.
By creating a URL action, the user can create a link in tableau that passes a unique key in the URL to this deployed Django Application.
For a key with no input, the user would comment and create an entry in a database.
For a key with a previous input, the form would then query the entry from the database and load it into the form. Saving that comment would update the entry in the database.

Tableau can then join the original dataset with the comments table that contains the users entries, displaying the user input in a column or tooltip.

For deployment, I configured an Apache server to host python scripts, and left it running on an applications server that was accesible by all users in the same network.
