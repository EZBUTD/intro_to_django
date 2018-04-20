# Form_testing
Code based from Pretty Printed tutorial on introduction to Django.

The goal of Form_testing is to create a flexible form meant to be used as a workaround for User input in an embedded Tableau webpage, so users can leave a comment on a row. This is useful for updating the status of an issue that won't be reflected in the datasource and providing feedback for others.

By creating a URL action within Tableau, the user can create a link that passes a unique key in the URL field.
For example, www.Server.com/Form_testing/Apple_Pie_Recipe would create a form with Apple_Pie_Recipe as the key.

For a key with no input, the user would comment and this form would create an entry in a database.
For a key with a previous input made, the form would query that previous entry from the database and load it into the form. Saving that comment would update the previous entry in the database.
A simple modification can be done to also create a new row for every entry on the form, on the same unique key. 

Tableau can then join the original dataset with the comments table that contains the users entries, displaying the user input in a column or tooltip. For a live connection, this comment would display whenever the page is refreshed or datasource is synced.

For deployment, I configured an Apache server to host python scripts, and left it running on an applications server that was accesible by users in the same network. 
