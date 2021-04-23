import models

"""Known as the root page, homepage, landing page but will act as the Listing route."""
@app.route('/')
"""Also will act as the Listing route just like /"""
@app.route('/entries')
def index():
    """This view should render a listing page of all of the journal entries, where each entry displays the following fields:"""
    title="should be a linked title, clicking it routes user to the detail page for the clicked entry."
    date="Each entry should have a date created listed somewhere beneath the title."


"""The Create route"""
@app.route('/entries/new')
def create():
"""Create an add view with the route /entries/new that allows the user to add a journal entry with the following fields:"""
Title - string
Date - date
Time Spent - integer
What You Learned - text
Resources to Remember - text
The page should present a new blank Entry form that allows the user to Create a new entry that will be stored in the database.


"""The Detail route"""
@app.route('/entries/<id>')
def view_entry():
"""This view should render a detail page of a journal entry, it should display the following fields on the page:"""
Title
Date
Time Spent
What You Learned
Resources to Remember.
NOTE: This page should contain a link/button that takes the user to the Edit route for the Entry with this <id>.


"""The Edit or Update route"""
@app.route('/entries/<id>/edit')
def edit_entry():
"""Create an edit view with the route /entries/<id>/edit that allows the user to edit the journal entry with an id of the <id> passed in:"""
Title
Date
Time Spent
What You Learned
Resources to Remember
Ideally, you should prepopulate each form field with the existing data on load. So the form is filled out with the existing data so the User can easily see what the value is and make edits to the form to make the update.

NOTE: Updating an Entry should not result in a new Entry being created, this behavior would not be seen as editing this would be adding a new entry. To check this, you can simply make an edit and then reload the listing page to see if a duplicate record was created.


"""Delete route"""
@app.route('/entries/<id>/delete')
def delete_entry():
"""Create a delete route to delete the journal post from the database. When the delete button is clicked by the user, the post will be removed from the database and they will be redirected to the homepage."""


app.run(debug=True, port=8000, host='0.0.0.0')
