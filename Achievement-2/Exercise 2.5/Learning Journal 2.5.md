# Exercise 5

## Frontend Inspirations

- 

- Link to recipe app: https://cookbookmanager.com/

## Reflection Questions

1. In your own words, explain Django static files and how Django handles them.

    - Static files are generally files that style and enhance the functionality of a Django web application. If you have static files specific to a particular app, Django expects to find them in a static directory within that app. Static files typically consist of images, stylesheets, and scripts that are available to the apps throughout your project. To access static files from your various apps, you must call the {% load static %} command, which is delimiter tag at the top of a Django template that gives pre-instructions to the HTML execution.

2. Look up the following two Django packages on Django’s official documentation and/or other trusted sources. Write a brief description of each.
   

    - ListView:
      - ListView is one of the most commonly used views in Django projects--it lists objects in a view for users to be able navigate through and interact with. In our recipe app, I used ListView to list the name and image of each object from my Recipes table. To use ListView in a Django project, you create a view class(RecipeListView) for a specific model (Recipe) by inheriting from the ListView class.

    - DetailView:
      - This is also a class-based view. It displays a single instance of a model. It takes the provided URL parameters, often a primary key, and renders the details of the object. In the recipe app, it showed the full recipe and all of the attributes featured in the model. 


3. You’re now more than halfway through Achievement 2! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? You can use these notes to guide your next mentor call.
   
    - I feel the course is going well. It is taking much longer than expected, but at the same time I do think I have learned a ton from this course, and my learning from this course has prompted me to go out and learn beyond the text. I have researched a ton of things beyond what the exercises required. There has been plenty that I haven't fully understood, but I have gotten so much exposure to more complicated aspects of Python and Django: using custom managers for a model with the get_queryset method to order recipes randomly using order_by('?'), I used context data to build a paginator and paginate listview results to 10, I imported Q for complex queries that made use of icontains for the search functionality, etc. I don't feel like the Python or Django expert by any means (definitely still quite the noob!), but I think I have pushed myself in a good direction. My downfalls, I would guess, are probably mostly the same as everyone else in my shoes... I need WAY more practice with basic algorithm skills. I still shutter a little bit when having to roll up my sleeves with for loops--Ijust really don't like the syntax and prefer js syntax with for loops, but... that just shows I need more practice. I fully anticipate doing all of the algorithm challenges at freecodecamp once I finish this course. Additionally, I am still just not seamless with my mvt understanding and navigation. Still find myself making silly mistakes like forgetting to path urls and not understanding why my view isn't working... Things like that. I know what the problem is, but it takes me a while to remember that basic step in the overall process. I just think a lot of it will become way easier as I work with it more. Overall, I am very proud of my Recipe app, and I think it will just get better and better.

- frontend inspiration: I provided this in the journal.doc via pdf, so I could include screen shots--please see journal.doc
  