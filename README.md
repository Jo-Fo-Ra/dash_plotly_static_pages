# Static (Web)pages for Dash Plotly

This repository can be understood as a template for static multi web-paging. The template is especially useful if there is a 
need to generate reports in an automated manner and outputted within a browser printer. With a functionality like this, 
it can be shown that Dash Plotly not only is usable for dynamic websites but static properties as well.

### How does it work?

#### Styles.css
The cascading style sheet establishes the formal structure in the browser's current view and printing mode. In this
example, the paper is of size 'US Letter' but can be changed for all pages by changing the respective page width and height.

#### App.py 
In app.py, the explicit structure of the pages is defined by referring to the classes defined in the styles.css. 
This is done by wrapping elements of a page with the className 'page'.

###How to run the template
 - Make sure that you have all relevant packages installed (see requirements.txt)
 - Choose a port/route in app.py and run the application
 - Open the Chrome browser on the specified address
