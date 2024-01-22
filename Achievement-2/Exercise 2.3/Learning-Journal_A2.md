# Learning Journal

## Achievement 2: Web Development and Django

### Exercise 1

#### Reflection Questions

1. Suppose you’re a web developer in a company and need to decide if you’ll use vanilla (plain)
Python for a project, or a framework like Django instead. What are the advantages and drawbacks
of each?

   - If you're deciding whether to use vanilla Python or Django for a project, you'll want to consider the following advantages and disadvantages for each:
     - Django
       - Advantages:
         - Simplifies common web development tasks with all of its built in components
         - Reduces redundancy with DRY principals
         - massive community with thorough documentation
       - Drawbacks:
         - The learning curve is challenging because Django is very opinionated
         - Little flexibility due to the batteries-included nature of the platform
         - Server intensive
     - Vanilla Python
       - Advantages:
         - lightweight
         - full control over code
         - good for small projects
       - Drawbacks:
         - next to no built in features--common web dev tasks are more tedious
         - development altogether takes longer

    - It would be appropriate to use Django if the project were larger, with many users, and involved rapid development; otherwise, Python is fine for simple projects that don't interact with a database and allow for more code flexibility.

2. In your own words, what is the most significant advantage of Model View Template (MVT)
architecture over Model View Controller (MVC) architecture?

   - The most significant advantage of Model View Template (MVT) over Model View Controller (MVC) is that in MVT, the template is responsible for handling both presentation and controller logic, simplifying the code and making it more straightforward compared to MVC.

3. Now that you’ve had an introduction to the Django framework, write down three goals you
have for yourself and your learning process during this Achievement. You can reflect on the
following questions if it helps:

What do you want to learn about Django?

   - The text talked a lot about Django simplifying common development tasks--it sounds like a great way to automate time-consuming development tasks.

What do you want to get out of this Achievement?

   - I want to gain more tools for my web dev toolkit. I want to be fluent with another framework, another language, and be able to program robust apps with them.

Where or what do you see yourself working on after you complete this Achievement?

   - That is hard to answer, considering I don't really know what I will be learning exactly. I will say, what this first exercise has been making me think of is the Chat App we built with React Native and JS. I would be interested to rewrite that app in Python with the Django framework.



### Exercise 2

#### Reflection Questions

1. Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference.

  - For an application like iTunes, the entire music application is the project. From there, the project is broken down into apps that handle the various functionalities iTunes requires. Some of the apps that would be necessary would be for authentication, the user's library, the iTunes Store, the user's recommendations, etc.


2. In your own words, describe the steps you would take to deploy a basic Django application locally on your system.

  - The first thing I would do would be create the directory for your project. Within that directory, I would create then activate its virtual environment. From there, I would install Django with the 'pip' command and use 'django-admin startproject' to start a new project. Subsequently, I would run migrations (python manage.py migrate) to set up the database. After that, I would create a superuser for the project (python manage.py createsuperuser). And last, launch the server with 'python manage.py runserver' and access your app.  
  

3. Do some research about the Django admin site and write down how you’d use it during your
web application development.

  - In Django, when you define models (representing database tables) for your application, the Django admin site automatically generates an interface for managing these models. From there, you can view, add, edit, and delete individual records.
  - The admin site includes features for user authentication and authorization. Superusers have full access to all functionalities, while other users can be assigned specific permissions to restrict their access.
  - Filtering, sorting, and searching functionalities are available, making it easy to find specific records.
  - The admin site keeps track of changes made to records, providing a history of edits. This is valuable for auditing and tracking modifications to the data.



### Exercise 3

#### Reflection Questions


1. Do some research on Django models. In your own words, write down how Django models work and what their benefits are.

  - Django models are templates a developer defines to organize and modularize data so that it can be stored in a consistent format within your database. It keeps your data tidy, and it helps you to enforce data validation by requiring an exact type of value for each attribute. Another benefit is that Django automatically creates a table when you define and register a model. Last, Django's ORM system allows you to interact with the database using Python objects, making it more intuitive and reducing the need for direct SQL queries.
   
2. In your own words, explain why it is crucial to write test cases from the beginning of a project. You can take an example project to explain your answer.

  - It is crucial to write test cases for your project from the start for a variety of reasons. First, it helps catch bugs efficiently and early on in the development process. Additionally, tests provide documentation for your project. Also, when features are added to the code, tests will catch potentially code-breaking bugs. For example, in a web application project, if a developer adds a new form for user registration, having test cases from the start allows them to verify that the registration process works as intended and doesn't cause errors in other parts of the application.



### Exercise 4

#### Reflection Questions

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