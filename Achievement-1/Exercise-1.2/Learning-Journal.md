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