# Backstory:
After successfully implementing the initial Flask web application for displaying items, your project requirements have been updated. Now, you need to enhance the application by allowing users to submit new items through a form. This will involve creating new routes, handling form submissions, and updating the display accordingly.

# Objective:
Extend the existing Flask web application to include a form for users to submit new items. Implement the backend logic to handle form submissions and display the newly added items on the list.

# Tasks:
1) Create a new route (/add_item) that displays a form for users to submit new items.
2) Design an HTML form (add_item.html) with fields for the item name.
3) Implement a route (/submit_item) to handle form submissions. Update the list of items with the newly submitted item.
4) Display a confirmation message or redirect users to the /items page after successfully submitting a new item.

# Requirements:
- Flask installed (pip install Flask).
- Basic understanding of HTML forms.

# Test Case:
Access the /add_item route, fill out the form, and submit a new item.
Verify that the newly added item is displayed on the /items page.