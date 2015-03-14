A minimal demo of eve and restangular.
======================================

I am trying to get to grips with eve and restangular, I will report my porgress in this repository so it can help others and maybe to get help myself.

I went through all the steps to quick start eve: http://python-eve.org/quickstart.html

To be able go through the quickstart I have completed these steps:

  - I downloaded mongodb on my computer. Inside, there was a bin folder.
  - I got a running daemon of mongodb. For that I had to do this: 
      - I had to create a database folder: ~/Documents/mongodatabase
      - Under bin I have to run this command:  ./mongod --dbpath ~/Documents/mongodatabase
  - I installed eve on my computer.
  - Along the quickstart, Eve created a table named people.
  - I read a few things about http.
  - I read about curl.
  - Using curl, I created two "documents" inside people: Obama and Romney. 
    It felt like magic.

So what now?

Now I want to develop an basic CRUD app, using restangular.

But I am not too skilled with web servers, wgi, etc so...

The html, css, and js will be served by eve itself. How? I had to read a bit about flask and finally came across this little trick! https://groups.google.com/d/msg/python-eve/Ay9sYD_V23Q/BmxweQUeWX8J

This is a work in progress, so far I have managed to list all people and add new people, I am still figuring out how to delete and edit. 


To run the demo:

- Get the quickstart running.
- Stop the quickstart run.py, but leave mongodb running
- Clone or fork this project on your computer.
- Run this demo:   python run-demo.py 
- In your browser, go to http://127.0.0.1:5000
