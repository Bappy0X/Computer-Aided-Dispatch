[:rewind: Back](/README.md)

# :three: Development

- [The Client](#the-client)
    - [Getting Started](#getting-started)
- [The API](#the-api)
    - [Getting Started](#getting-started-2)

# The Client

The client will be the web accessible site that end-users will use in order to access their CAD dashboard. This will be built with React.js, a JavaScript framework for creating fast & "reactive" sites that will run on any modern browser.

---

## Getting Started

We must start from somewhere, we'll need to create our basic structure for our Client App.

With react, this is fairly simple.

First, we must ensure that Node.js is installed on our local machine and then run:

> npx create-react-app

This will take a couple mins or so, and will create a very basic structure for our application. From this, we'll be able to construct the app from this template.

---

# The API

This will be the powerful engine beneath the hood. The API will be used to transfer data between the server and the client, all requests for data will be submitted via this API.

For the API, I'd like to set out 3 requirements:

- **Versaility**

Alike a Swiss Army Tool, the API should be multi-functional. It should be able to adapt and be used in a wide variety of situations.

- **Speed**

Throughout its functionality, the API should be stable under heavy loads where user traffic may peak. With the importance of delivery of date from this API, this is an extremely important factor - deliverability is a must.

- **Existing Support and Documentation**

In order to deploy with ease, and have the end-user understand the workflow, functionality and purpose of the API - existing documentation should already exist. This will help the end user to debug and understand any issues that may arise, and become easier to replicate and fix.

I recently encountered FastAPI from DigitalOcean - my favourite server hosts, who covered the library in a tech talk, linked [here](https://www.youtube.com/watch?v=KVlqN0xNJxo). It fulfills every requirement on this list, and more. It's insanely fast, and incredibly versatile, outperforming Flask. It also supports Swagger for fast and easy documentation, and has great existing documentation and a great community.

---

## Getting Started