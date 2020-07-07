# Static (Web)pages for Dash Plotly

This repository can be understood as a template for static multi web-paging. The template is especially useful if there is a 
need to generate reports in an automated manner and outputted within a browser printer. With a functionality like this, 
it can be shown that Dash Plotly not only is usable for dynamic websites but static properties as well.

### How does it work?
#### App.py 
In app.py, the explicit structure of the pages is defined by referring to the classes defined in the styles.css. 

#### Styles.css
The cascading style sheet establishes the formal structure in the browser's current view and printing mode. In this
example, the paper is of size 'US Letter' but can be changes for all pages by changing the width and height.
