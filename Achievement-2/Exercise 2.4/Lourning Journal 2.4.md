
# Exercise 4

## Reflection Questions

1. Do some research on Django views. In your own words, use an example to explain how Django views work.

  - In a Django web application, a view is a Python function that takes a web request and returns a web response. A web request is sent via the user's browser, and the response sent back is what the user sees and consumes. Simply, it takes input from the user and displays content accordingly. When input is received, the view's template uses that data to generate the final html. To accomplish this, you must use urls to map the views, essentially putting together navigation framework.

2. Imagine you’re working on a Django web development project, and you anticipate that you’ll have to reuse lots of code in various parts of the project. In this scenario, will you use Django function-based views or class-based views, and why?

  - If I were working on a Django web development project, and I anticipated having to reuse lots of code, I would assume a CBV approach. It specializes in its modularity and being able to package redundant code, so that it can easily be reused across the project. Also, being class-based, code reuse is streamlined because of the inheritance capabilities CBV offers. Function-based views are usually for smaller projects. Class-based views are more scalable and organized for larger projects.

3. Read Django’s documentation on the Django template language and make some notes on its basics.
   
  - variables are placed in {{double curly braces}}
  - templates use control statements (like loops and conditionals)  called {% tags %}
  - you can filter the output of variables using filters: {{value|filter_name}}
  - You can extend content from a template to its child components
  - for loop looks like: {% for item in list %} ... {% endfor %}
  - if statements look like: {% if user.is_authenticated %} ... {% else %} ... {% endif %}
  - comment on code with {# comment #}