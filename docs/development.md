[:rewind: Back](/README.md)

# :three: Development

- [The Client](#the-client)
    - [Getting Started](#getting-started)
- [The API](#the-api)
    - [Structure](#structure)

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

The end goal for this API will be to be fast, and efficient.