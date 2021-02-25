[:rewind: Back](/README.md)

# :two: Design

- [Chosen Tech Stack](#chosen-technology-stack)
	- [Backend](#backend)
	- [Databases](#databases)
	- [Frontend](#frontend)
	- [Deployment](#deployment)
	- [Devops](#devops)
	- [Tools](#tools)

# Chosen Technology Stack

Behind every good webapp is a complicated stack of software and hardware. The goal of creating a good tech-stack is choosing the software and hardware that is the most efficient, usable and least expensive, whilst still retaining quality.

---

### Backend

To build the backend API for this app, I'd like to use a Python environment. This is because I favour Flask's extensive usability and support in the modern world.

**NGINX WSGI**

To manage instances running on the same server, NGINX will be used. It's simple to use and implement. It just requires an installation and simple understanding of its syntax.

This will be used to proxy and compile the Backend and Frontend into one domain. e.g:

Backend/API: https://myapp.com/api/

Frontend/UIUX: https://myapp.com/

**Py/Flask**

I LOVE Flask. It's great for building responsive API's, and can use Pythons expandability in order to integrate with other services.
In this instance, Flask will be used purely for API endpoints. It won't serve any html or web files. Ideally, it would have a documentation page to assist with development, and allow clients to utilise it. However, this may become time consuming. Worth checking out in future.

**Flask-Socket.IO Server**

To enable realtime communication and updates between the server and client, S.IO can be used. This will allow for different datasets to be updates in realtime, automatically, within scheduling and setting up requests to the API, which also may be pointless. All end-users can connect to one S.IO instance, further decreasing the load on the API.

### Databases

We will need a way to access, manage and store all of our data that will be used on the platform. Accessing data quickly and efficiently is a must, and these connections should also be secure, and be designed with security in mind.

**Redis - High Speed K:V**

Whenever we want to access data quickly and efficiently, we'd use Redis. This is a Key: Value store that operates entirely in memory - this is why it's so fast.

**MySQL - Simple & Neat Relational**

Within our application, we'll have many pieces of data that will need to be relational or integrate with eachother. MySQL is great at doing this! I prefer MySQL over PostgreSQL, purely because of its support and usability - especially with database management - MySQL Workbench is much better than PostgreSQL Admin - in my own opinion.

**MongoDB - JSON-like syntax**

This is a great database system, and can be used in the same way as MySQL - *however*, MongoDB is a closed source database, and isn't relational. This means that some rules that we may wish to implement with our application may cause errors with some components, and may make it more difficult to interface with some details.

### Frontend

**HTML5**

At some point, we'll need to use HTML. This is the syntax that is used in order to display/show information to an end-user via a browser.

**CSS3**

HTML is pretty boring on its own, so it'll need styling and changing to be more interesting. Queue CSS! Using stylesheets, we can customise the look/UI of the frontend.

**Bootstrap**

CSS is very useful. However, it can be very time consuming to create stylesheets for commonly made UI elements, like buttons. Bootstrap is very useful for this. It defines boilerplate code in a very easy-to-use manner.

**React**

React is very new to me. However, React is becoming more widespread, and this gives me a chance to properly learn. As the name suggests, React *reacts* to changes to elements within the DOM, this could be very useful with real-time updates. As well as this, React allows you to define commonly used code for reuse later. This could prove very useful for this use-case.

**jQuery?**

Simple to use and set up, jQuery is a great tool for indexing, referencing and manipulating different elements within the DOM. It also makes AJAX requests much easier.

**Socket.io Client (js)**

In order to interface with the backend S.IO, we must have a client side. This will allow us to have real-time communications between the server and the client, so that updates and much more will be instantaneous.

### Deployment

When we're ready, we'll want to host the application on a remote server. This will give the application proper resource allocation, faster and more reliable connection, and much more.

**DigitalOcean**

I'm a massive fan of DigitalOcean's VPS hosting. Their packages are extremely competitive and is very expandable. You're able to receive $100 free credit when referred from a friend. 

**Ubuntu**

This is my favourite Linux distribution. It's easy to implement, manage and understand. I intend to run a pure CLI interface, and won't need a desktop manager.

### Devops

**Visual Studio Code**

My favourite IDE.

**Windows Terminal**

One of the best tools available on Windows for developers! Looks stunning and has a lot of capabilities. I'll also use WSL (Windows Subsystem for Linux) in order to run a local Ubuntu version to test code and connect to the remote server/VPS.

**TravisCI**

Integrated testing is a massive component of the DevOps chain. Deploying dysfunctional solutions can be very time consuming and very costly. Automated testing attempts to solve this, by testing applications within in a deployment environment.

**GitHub**

Open Source is the best. Time to give back.
This is a great tool for browsing source code, documenting features (just like this) and helping people out with examples. It also creates a centralised location for all the application's code.

### Tools

**Cloudflare**

In order to set up DNS and properly use domains, and create SSL certificates, Cloudflare will be used. It has a free plan and allows the usage of advanced features, such as caching, insights into visitors and activity, and more.

**Insomnia**

In order to test the RESTful API for this project, I'll use Insomnia. This is a great app built on Electron that allows easy viewing and manipulation of data being sent to a server. This will allow me to test different cases and construct truth tables based on results.