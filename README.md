A minimal demo of Eve and Restangular.
======================================

I am trying to come to grips with Eve and Restangular.

I will report my progress in this repository so it can help others following my same path.

First I went through all the steps to quick-start Eve: http://python-eve.org/quickstart.html

To be able go through the quickstart I have completed these steps:

  - I downloaded mongodb on my computer. Inside, there was a bin folder.
  - I got a running daemon of mongodb. For that I had to do this: 
      - I had to create a database folder: ~/Documents/mongodatabase
      - Under bin I have to run this command:  ./mongod --dbpath ~/Documents/mongodatabase
  - I installed Eve on my computer.
  - Along the quickstart, Eve created a "table" named people.
  - I read a few things about http.
  - I read about curl.
  - Using curl, I created two "documents" inside people: Obama and Romney. 
    It felt like magic.

So what then?

Then I wanted to develop an basic CRUD app, using Restangular.


The making of a static web server
----------------------------------

But I am not too skilled with web servers, Flask, etc, so the html had to be served by Eve itself. How? I had to read a bit about flask and finally came across this little trick! https://groups.google.com/d/msg/python-eve/Ay9sYD_V23Q/BmxweQUeWX8J

It works! Eve is serving my html.

OK, to continue with the Restangular part, I learned a bit about angular.js here: http://www.w3schools.com/angular/

And now I am dabbling with https://github.com/mgonto/restangular

So far I have managed to list all the people and add new people, BUT I AM STILL FIGURING OUT HOW TO DELETE AND EDIT. 


Making a verbose log.
---------------------

I need to understand Restangular a little further, for that I need Eve to show in console the http request from Restangular. I asked [Nicola Iarocci](https://github.com/nicolaiarocci), the creator of Eve, and he just answered me:

> "You should probably give a look at Flask logging tutorial at 
>  http://flask.pocoo.org/docs/0.10/errorhandling/  
>
>  Eve is just a Flask application so whatever works with Flask works 
>  with Eve’s app too.
>
>  HTH"

That logging is what I am studying now, so I submitted a question to flask@librelist.com. And [David Nieder](https://github.com/davidnieder?tab=repositories) gave a quick and dirty trick:

http://librelist.com/browser//flask/2015/3/14/show-full-http-request-and-response-on-console/

Now I have Eve logging the requests, great!

Next thing I need is to show the resource if it is json.



If you want to run this demo
-----------------------------

Try the following steps:

  - Get the quickstart running.
  - Stop the quickstart run.py, but leave mongodb running
  - Fork this project onto your computer.
  - Run this demo:   python run-demo.py 
  - In your browser, go to http://127.0.0.1:5000/static/index.html


