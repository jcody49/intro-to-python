# Learning Journal

## Achievement 1: Intro to Python 

### Exercise 1

- Talk a little about your coding experience so far, even prior to taking this course... 

  -  First I went through the full stack development course via CareerFoundry. I started by learning the very basics to frontend development with mostly html structuring, and a little bit of css styling to create the basic verion of my portfolio site. 
  -  After that, I went through the first course that introduced Javascript. I learned the basic JS syntax with simple functions. I learned how to integrate Bootstrap in with my JS and style everything in the app that way (buttons, modals, navbar, etc). I think the biggest skill I learned from this achievement was looping over arrays.
  -  After that, I completed my first backend Achievement/project, where I learned how to build a server and an api and implement security measures for app users.
  -  Following that, I built the frontend of the app and linked it up to the back. The frontend is an IMDB-like app that shows the movies from the database with movie images, movie details, and information about the directors. In this project, I learned to implement the React library for and build a suite of components with loads of javascript and html (jsx) as well as scss styling. I learned to use hooks to manipulate the state. I learned to link up the authentication measures from the back, and by doing so, users were able to log in, edit their profile details, add/remove movies to/from their favorites, add/remove movies to/from their watchlist, and delete their account. 
  - After, that I learned how to make an app that used data from a Google Calender API and create a search engine that sifted through events in different cities, and users could meet up based on the available events. Also, I utilized  chart visualizations to help illustrate what places had a lot of events and what types of events were occuring via scatterplot and bar graph
  - Next, I learned to build a chat app where users could share text messages as well as images, videos, and GPS location. This was my first native app I learned to build, and it taught me how to use emulators and simulators.
  - My last project I did for the full-stack program was the same clientside movie app, but built via Angular. Through this process, I learned about typescript, static typing, two-way data binding, directives, services, and the Angular CLI.


- **Now, note down what you’ve learned in this Exercise and what you wish to learn in the long run...

  - In this exercise, I learned: 
    - how to download and install Python
    - how to make a virtual environment and activate it
    - how to generate a requirments.txt file
    - how to use basic syntax to create variables and run a basic addition function

  - What I want to learn:
    -  the Python language in general for the simple fact that it is versatile and can be used with so many types of code.
       -  Python syntax and vocabulary
    -  how to take advantage of Python's symplicity and maintainability
    -  how to use the Django Unchained framework (I want to get as many of those under my belt for potential future employment)
  

### Exercise 2

1. Imagine you’re having a conversation with a future colleague about whether to use the iPython
Shell instead of Python’s default shell. What reasons would you give to explain the benefits of
using the iPython Shell over the default one?

  - I would recommend using the iPython Shell over the default one because it offers enhanced features like tab completion and syntax highlighting--it is a lot easier to see and increases efficiency.

2. Python has a host of different data types that allow you to store and organize information. List 4
examples of data types that Python recognizes, briefly define them, and indicate whether they are
scalar or non-scalar.

  - Tuples:
    - Tuples are non-scalar data structures that are immutable and store multiple values of any type. They are used when there is a lot of data that pertains to one object.
  - Lists:
    - Lists are non-scalar data structures that are mutable and can store multiple values of any type. They are defined using square brackets and are used when dealing with collections of related data.
  - Strings:
    - Strings are immutable, non-scalar structures that are enclosed by quotes.
  - Dictionaries:
    - Dictionaries are mutable, non-scalar structures that are made up of unordered key-value pairs.

3. A frequent question at job interviews for Python developers is: what is the difference between
lists and tuples in Python? Write down how you would respond.
  - Tuples are immutable, so they cannot be changed; whereas, lists are mutable and can be changed. Also, tuples use parentheses and lists use brackets.
  
4. In the task for this Exercise, you decided what you thought was the most suitable data structure
for storing all the information for a recipe. Now, imagine you’re creating a language-learning app
that helps users memorize vocabulary through flashcards. Users can input vocabulary words,
definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz
themselves by flipping through the flashcards. Think about the necessary data types and what
would be the most suitable data structure for this language-learning app. Between tuples, lists,
and dictionaries, which would you choose? Think about their respective advantages and
limitations, and where flexibility might be useful if you were to continue developing the languagelearning app beyond vocabulary memorization.
  - For a language-learning app with flashcards storing vocabulary words, definitions, and categories, I would choose dictionaries. Dictionaries offer a natural way to represent each flashcard, with keys for words, definitions, and categories. This choice provides flexibility for easy retrieval, updates, and expansion of information. Lists might be suitable for managing a sequence of flashcards, while tuples, being immutable, might limit modifications in a dynamic learning app.


### Exercise 3

1. In this Exercise, you learned how to use if-elif-else statements to run different tasks based on
conditions that you define. Now practice that skill by writing a script for a simple travel app using
an if-elif-else statement for the following situation:
● The script should ask the user where they want to travel.
● The user’s input should be checked for 3 different travel destinations that you define.
● If the user’s input is one of those 3 destinations, the following statement should be
printed: “Enjoy your stay in ______!”
● If the user’s input is something other than the defined destinations, the following
statement should be printed: “Oops, that destination is not currently available.”
Write your script here. (Hint: remember what you learned about indents!)

- [Link to travel_script](./travel_script.py)


2. Imagine you’re at a job interview for a Python developer role. The interviewer says “Explain
logical operators in Python”. Draft how you would respond.

- Logical operators are used for compairsons using 'and', 'or', and 'not'. They help to create conditions and perform operations that adhere to certain conditions.

  and: Returns True if both operands are True.
  or: Returns True if at least one operand is True.
  not: Returns True if the operand is False, and vice versa.


3. What are functions in Python? When and why are they useful?

- Functions are actions you can program within your code. Functions can perform a wide variety of tasks, and they are extremely helpful in that they can be reused throughout your app or website. 

4. In the section for Exercise 1 in this Learning Journal, you were asked in question 3 to set some goals for yourself while you complete this course. In preparation for your next mentor call, make some notes on how you’ve progressed towards your goals so far.

 - Here is what I wrote for my goals:
    - What I want to learn:
      -  the Python language in general for the simple fact that it is versatile and can be used with so many types of code.
         -  Python syntax and vocabulary
      -  how to take advantage of Python's symplicity and maintainability
      -  how to use the Django Unchained framework (I want to get as many of those under my belt for potential future employment)

    - My Reflection:
      - I have made some progress on the Python language in general. I have learned about manipulating data in the forms of tuples, lists and dictionaries. I have learned how to use operators and construct algorithms for efficiently accomplishing small tasks. Also, I have learned how to define and call functions in Python. These have been my first steps into cementing Python's syntax and vocabulary. I still have a lot of learning ahead of me, so I don't think I can really take advantage of the simplicity and maintainability until I have learned more and see Python's bigger picture. Also, I believe we learn Django in Achievement 2? So, I won't know much about that until then.


### Exercise 4


#### Reflection Questions

1. Why is file storage important when you're using Python? What would happen if you didn't 
store local files?

  - File storage is important because the data will disappear at the end of execution if it isn't stored somewhere.
  
2. In this Exercise you learned about the pickling process with the pickle.dump() method.
What are pickles? In which situations would you choose to use pickles and why?

  - Pickles are used for storing complex data as a binary file of bytes, so pickles are ideal for dictionaries since they carry key-value pairs that aren't transferrable in their normal format. Pickles make it so that complex data can be transferred between files.
  
3. In Python, what function do you use to find out which directory you're currently in? What if you wanted to change your current working directory?
   
  - os.getcwd() will tell you your current working directory
  - os.chdir(<path>) will change to another directory, taking the path of the directory you'd like to change to as an argument

4. Imagine you're working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

  - To comb for errors, you can use a try-except block. The programmer needs to put the code to be "tried" in the try block, and the potentially error-prone code should go in the except block, so that if an error occurred your script would identify it as well as still run.   

5. You're now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What's something you're proud of so far? Is there something you're struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call.
   
  - Python is going okay. It's dense. I'm working on my javascript algorithm skills as well, and I am seeing all of these ways I can solve the same problems I have solved with javascript, but with Python. For instance, I just learned how to split a string and reverse it with Javascript--I can definitely do that with Python as well. There are a few algorithm problems on freecodecamp that I now know how to solve with Python. I am, struggling with file storage--1.4 was ROUGH! I don't fully understand how I got everything to work. I wish there were more visuals to go along with the exercise at the end. I felt extremely in the dark, and I desperately needed to enlist the help of the examples and Google. I do feel like I'm picking this up a little better and more thoroughly than I did Javascript, so it has been good to feel that comfort. One exception to that , however... There are a lot of striking similarities between Python and JS... I think it helps me to grasp new concepts with Python; however, at the same time, I think it might cause extra confusion sometimes because they are so alike in so many ways, but they look SO different! Can't tell you how many times I go to write "let ="... There's a strong mixture of confusion, but also empowerment that I have experienced since I have begun my Python journey. 
  
  I need more practice with...
  ALL OF IT!!!



### Exercise 5

#### Reflection Questions

1.	In your own words, what is object-oriented programming? What are the benefits of OOP?
    
  - In Python, Object-Oriented Programming (OOP) uses classes to make objects. Classes act as templates. Each object can be defined with different attributes and functionalities. This approach simplifies software development by structuring code into elements that are reusable and easy to maintain.



2.	What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.
  - In Python, classes are like blueprints that define how to create objects. Objects, on the other hand, are instances of these classes, representing specific things with unique attributes and behaviors.

  - A real world example could be the class: "Animal". Each object you design with that class would represent a different animal. You could program them to have different attributes such as sounds, vertibrate, eating habits, etc.
  

3.	In your own words, write brief explanations of the following OOP concepts; 100 to 200 words per method is fine. 

Method	Description

Inheritance:
  - Inheritance is when you have a child class that inherits all of the attributes and functionalities that furnish its parent class.


Polymorphism:

  - Polymorphism is when you have a method or function that can perform differently with different objects. The '+' operator is an example because it can concatenate strings as well as add numbers.


Operator Overloading:

 - Operator overloading allows you to program custom behaviors with the different operators. By overloading operators, you can specify the actions performed when these operators are used with different class objects.



### Exercise 6

#### Reflection Questions

1.	What are databases and what are the advantages of using them?
  -	Databases are essentially organized, electronic filing systems for information. They help keep data neat, make it easy to find, and ensure it's accurate. Users can perform queries on databases to retrieve specific information and perform various operations with the stored data. Databases act as digital organizers, making it easier and more efficient to manage and interact with information.

2.	List 3 data types that can be used in MySQL and describe them briefly:

  - DATE: Used for storing dates in the format 'YYYY-MM-DD'.
  - INT: Stands for Integer. It is used to store whole numbers without any decimal points.
  - VARCHAR: Stands for Variable Character. It is a variable-length string data type that can store alphanumeric characters. A maximum length is specified at the end in brackets [].


3.	 In what situations would SQLite be a better choice than MySQL?
    - Use SQLite for small-scale projects due to its simplicity and that it is self-contained within a program, not requiring a separate server process. MySQL is better for larger projects requiring a robust client-server database setup.

4.	Think back to what you learned in the Immersion course. What do you think about the differences between JavaScript and Python as programming languages?
  - To my understanding, JavaScript is mainly used for web development, which allows for interactive and dynamic content on the client side. It works well HTML and CSS, and it is great for building web apps. Python, on the other hand, seems like it can be used for more types of projects, such as building websites, analyzing data, and automating tasks. Python is still pretty new to me, so this is a hard question to answer. I used JS on several projects and am much more experienced with it; I'm still learning the basics of Python, so I can only answer this question generally. Once I actually start building out the recipe app a bit more, I will be able to compare a lot more accurately.

5.	Now that you’re nearly at the end of Achievement 1, consider what you know about Python so far. What would you say are the limitations of Python as a programming language?
  - In my limited experience with Python, I have learned that Python is an interpreted language, which makes it slower. Python is not as friendly for mobile development. It uses up a lot of memory.





### Exercise 7

#### Reflection Questions


1. What is an Object Relational Mapper and what are the advantages of using one?

  - An ORM converts the contents and structure of your database into classes and objects that can be interacted with directly It reduces the amount of code for making queries on a database considerably.

2. By this point, you’ve finished creating your Recipe app. How did it go? What’s something in the app that you did well with? If you were to start over, what’s something about your app that you would change or improve?
   
  - The app was good--pretty difficult. I wish the exercises were broken down a little more. The reading is dense and there is so much of it, and then the exercises at the end are so robust. It's just a lot for one section--I personally, could have benefitted from making the exercises smaller, so the content is easier to digest. I feel like I learned a lot, and I feel decently competent; however, I also feel like I learned just enough with certain concepts due to the rapid nature of this course. I definitely had to go through a lot of extra lengths to understand the code I needed to implement, which isn't a bad thing, but it just shows I'm not quite confident in my Python skills just yet. I drew heavily on Google and the sample work, I had to go back and re-read everything several times, and I had to comment my understanding on just about every nook and cranny of all of my code... It's overall fine, and I think the confidence will come more and more as I learn throughout the next achievement.



3. Imagine you’re at a job interview. You’re asked what experience you have creating an app using Python. Taking your work for this Achievement as an example, draft how you would respond to this question. 
  
  - I recently developed a command-line Recipe app in Python, leveraging SQLAlchemy for database management. Within the project, I worked with all kinds of data types: strings, lists, tuples, integers, dictionaries, functions, and loops. I used object-oriented programming to build classes that served as blueprints. The app features a Recipe class with some basic attributes: name,cooking time, ingredients, and difficulty. I built a menu that loops until the user wants to exit. The cli boasts functionalities for creating, viewing, searching, editing, and deleting recipes from the sql database. The menu provides a user-friendly interface. Additionally, I have grown adept with testing Python code with ipython. In short, the project has not only showcased my proficiency in Python and database management, but has also emphasized error handling for a robust user experience. 
  
  

4. You’ve finished Achievement 1! Before moving on to Achievement 2, take a moment to reflect on
your learning in the course so far:

  a. What went well during this Achievement?

   - For this achievement, I think I was able to pay attention to new vocabulary better. With that, I think I did a better job of slowing down my learning. With some of the previous courses and Achievements, I definitely got ahead of myself a few times--sometimes skimming sections that I didn't necessarily think were as important at the time, and then lo and behold, I'd get pretty confused with the tasks at the end and not even understand why. I also think when I start to get tired, my mind wanders while I'm reading more complicated content, which I don't always catch--this time around, I really forced myself to take notes during those times, to keep my mind active as I'm reading. That, and I'm better at taking small breaks.

  b. What’s something you’re proud of?

   - I'm proud that I was able to learn so much and not have to ask as many questions as I did before (which I'm certainly not afraid to do). I think my grasp on code in general from my previous learning served me quite well, and I wasn't really getting stuck. Definitely had some hiccups and some speed bumps, but I didn't really get stuck much.

  c. What was the most challenging aspect of this Achievement?

   - The most challenging apect of this achievement was getting enough time to learn in detail. In some cases, I barely got my app to work and didn't totally understand why. I understood everything in isolation, but when everything started to come together, and you needed to start troubleshooting. I, personally, wish there were more mini-exercises that combined skills and that the course were broken down a little bit more. The assignments felt like a slog--just kind of a lot to take in as your learning for the first time.

  d. Did this Achievement meet your expectations? Did it give you the confidence to start
  working with your new Python skills?

   - I would say, yes, more or less. Again, some more practice would have been nice, but I think there are plenty of free practice work at freecodecamp, so I think that should work out just fine. Other than that, yes, I'm glad to have gotten my app working pretty well and that it is pretty thoroughly commented. Also, the review of SQL was nice.

  e. What’s something you want to keep in mind to help you do your best in Achievement 2?

   - Keep commenting. Just keep breaking things down into digestable chunks and comment to solidify understanding as well as provide myself with notes for the next time I sit down with the code.



