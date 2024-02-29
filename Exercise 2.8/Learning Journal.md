1. Explain how you can use CSS and JavaScript in your Django web application.
   
    - In a Django web application, you can use CSS for styling by creating a static folder in your app and placing your CSS files there. Then, link to the CSS file in your HTML templates.

    For JavaScript, include your script files in the static folder as well, and reference them in your HTML templates. Additionally, you can use the {% static %} template tag to dynamically generate the URLs for your static files.

        






2. In your own words, explain the steps you’d need to take to deploy your Django web application.

    - Make sure all dependencies are listed in requirements.txt.

    - Select a platform to host your application like Heroku, AWS, or DigitalOcean.

    - Configure your database settings, and if needed, migrate your database schema.

    - Set up proper configurations for handling static files (CSS, JS) and media files (uploads, images)--implement whitnoise for static files, and aws for media...

    - Enable HTTPS, keep sensitive information secure, and configure security settings--turn DEBUG to False and hide all sensitive information on Heroku as environment variables

    - Run the Heroku collectstatic command to gather all static files in one location.

    - Push your code to Heroku and make sure to apply any necessary migrations.

    - Ensure that your application is running smoothly in the production environment.

    - Construct a test suite to ensure your site is free of errors
   
3. (Optional) Connect with a few Django web developers through LinkedIn or any other network. Ask them for their tips on creating a portfolio to showcase Python programming and Django skills. Think about which tips could help you improve your portfolio.

    - Tried to reach out on Slack, but got no responses... Any other suggestions?
   
4. You’ve now finished Achievement 2 and, with it, the whole course! Take a moment to reflect on your learning:

    a. What went well during this Achievement?

        - I would say everything went more or less well because in the end, I have a pretty nice app and I have gained crucial knowledge and skills. I would have to say things went significantly smoother prior to 2.7... There were some hiccups in 2.6, and 2.7 and 2.8 were absolute monsters for me (I'll discuss more in the challenges)... Generally speaking, I mostly cruised through the Django setup, constructing the models (although it was hard to have an idea early on of what I wanted it to look like exactly), views and templates, and MVT. In general, I feel pretty good about adding Python and Django to my overall skillset--I am starting to see, more and more, how it's all coming together into the bigger picture of programming... one confusing acronym and one complicated vocabulary word at a time. One last colsing thought.. I did struggle immensely at the end of the Achievement, but I do think it forced me to comb through my code about a million times, so I do feel like I have gotten some great (although VERY frustrating) experience from rolling up the sleeves and wading deep into the muck.

    b. What’s something you’re proud of?

        - I'd say everything that I just mentioned, but to recap... I'm really happy with the way I have noticed my html, css, and js skills come back into the fold as a strength instead of a stumbling point. My css and js skills have empowered me with my recipe app, whereas they were, at one point, a struggle. One example... I could not for the life of me implement Bootstrap 5 (I think because I started styling with 4 and then went to make the navbar, which needed 5), so instead, I worked around that by writing custom js to get my navbar to display as expected via clicking on the toggle bar. That was one of the coolest experiences of this course: confidence in things I have already learned helping me to learn new things and gain confidence with those concepts.  

    c. What was the most challenging aspect of this Achievement?

        - The most challenging parts of this course are the things I have said plenty of times, and it has not changed. In general, I just wish there was more time to practice new skills in isolation as well as ore time to practice new skills in conjunction. I wish I was able to regularly communicate with my teachers--not just over an instant messenger. But, be able to talk about it, immerse myself in it, have to talk the talk and walk the walk. The vast majority my learning took place in my head... I never really got to verbally speak with my newly learned terminology and understanding, which is so important to the leanring process--struggling with the words and making myself fluent with everything. The times I did speak with teachers (not just in this course), I struggled to express myself proficiently and be able to ask smarter questions... All good, I have it now! I just would have LOVED picking the brains of my teachers more... I also would have loved to work with some PEERS... There's Slack.... Obviously, that can't replace day-to-day interactions with peers. So... in general... Remote learning is super hard... Especially, when you are only reading from an online text--I want to have a teacher deliver a finely tuned lesson...I understand that is just not the CareerFoundry paradigm, but in short.... it was by far, my greatest struggling point. I think if I had someone to talk to in person, I would have knocked all the exercises out pretty fast. I need to have that ability to get taken out of my own head and thoughts. When I think I am right, it is hard for me to see beyond that perspective... Anyways... rant over!



    d. Did this Achievement meet your expectations? Did it give you the confidence to start working with your new Django skills?

        - Most definitely! Although, it will not hurt to review 2.6 - 2.8 once or twice more! Otherwise, yes, see my massive answers to the other questions to see the ways my confidence has grown!
