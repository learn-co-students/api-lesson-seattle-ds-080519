# APIs Lesson

## Students Will Be Able To:
 - [] Describe the client-server model and request-response cycle
 - [] Identify examples of clients and servers, both on their local computers and remotely connected
 - [] Identify examples of requests and responses
 - [] Understand the basic concept of a web server, and the types of requests and responses it uses
 - [] Understand the difference between a request that returns HTML and an API request that returns JSON
 - [] Understand the basic pieces of making HTML and JSON requests
 - [] Use a browser to make HTML and JSON requests
 - [] Use Postman to make HTML and JSON requests
 - [] Use Python `requests` library to make HTML and JSON requests
 - [] Practice reading the documentation for an API

## Existing Code
1. Uses the Python [`requests` library](https://2.python-requests.org/en/master/)
2. Uses the [Google Books API](https://developers.google.com/books/docs/v1/using#WorkingVolumes)
3. Searches for author "Jake VanderPlas" (author of my go-to Python data science book)
4. Prints out a list of book titles that match this query

## Deliverables
 - [] Refactor the existing Google Books code so that it uses the [`params` argument](https://2.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls)
 - [] Write new code in a new file that queries the NASA ISS API and prints out the current latitude and longitude