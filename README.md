# APIs Lesson

## Students Will Be Able To:
 - [x] Describe the client-server model and request-response cycle
 - [x] Identify examples of clients and servers, both on their local computers and remotely connected
    - PostgreSQL is a server
    - `psql` in the command line is a client
    - `psycopg2` in Python is a client
    - Jupyter Notebook is a server
    - Google Chrome (like all web broswers) is a client
 - [x] Identify examples of requests and responses
    - If you're sending a request to PostgreSQL, that looks like "SELECT * FROM names;"
    - If you're sending a request to Jupyter Notebook, that looks like "http://localhost:8888/notebooks/APIs_exploratory_notebook.ipynb"
    - If you're sending a request GitHub to get their homepage, that looks like "github.com"
 - [x] Understand the basic concept of a web server, and the types of requests and responses it uses
 - [x] Understand the difference between a request that returns HTML and an API request that returns JSON
    - "API" technically can mean a lot more things, but usually it means an HTTP (web) interface that returns JSON
 - [x] Understand the basic pieces of making HTML and JSON requests
    - For simple requests, you only need 2 things: HTTP verb and URL
    - HTTP verb: this will almost always be `GET`, kind of like how a data scientist's SQL query will almost always be `SELECT`.  But there are other verbs, including `POST` and `PATCH`, which are like `INSERT INTO` and `UPDATE`
    - URL: this is the string representing the location of the resource.  It can also be called a "path", or an "endpoint"
 - [x] Use a browser to make HTML and JSON requests
    - This just means typing the URL into the browser.  It will always be a `GET` request.
    - The browser will show HTML or JSON depending on the URL.  So, `reddit.com` shows you HTML, whereas `reddit.com/.json` shows you JSON.
 - [x] Use Postman to make HTML and JSON requests
    - Postman has input fields where you can type the URL and select the HTTP verb from a drop-down
    - Remember that this is a good tool for exploration/figuring out how to use an API (better than Chrome), but it's not the final product
 - [x] Practice reading someone else's Python code that uses the `requests` library
    - We walked through the Google Books example (see "Existing Code" section below)
 - [x] Use Python `requests` library to make JSON requests
    - This looks like `requests.get("http://api.open-notify.org/iss-now.json")`
    - The HTTP verb is specified by the method name (`.get` for `GET`, `.post` for `POST`, etc.)
    - The URL is the first (and only required) parameter passed into the `.get` method
 - [x] Practice reading the documentation for an API

## Existing Code (`google_books.py`)
1. Uses the Python [`requests` library](https://2.python-requests.org/en/master/)
2. Uses the [Google Books API](https://developers.google.com/books/docs/v1/using#WorkingVolumes)
3. Searches for author "Jake VanderPlas" (author of my go-to Python data science book)
4. Prints out a list of book titles that match this query

## Deliverables
 - [] Refactor the existing Google Books code so that it uses the [`params` argument](https://2.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls) (we did not get to this in class)
 - [x] Write new code in a new file that queries the NASA ISS API and prints out the current latitude and longitude
    - This is in `APIs_exploratory_notebook.ipynb`, plus some fun mapping stuff.  You might need to run `conda install ipyleaflet` in the terminal to get it working.  If you run it again, expect a different map, since the ISS is constantly moving very quickly!
    - Currently the code in the notebook doesn't do any error checking.  That is pretty common for exploratory code in a notebook, but you almost always want to do error checking when you write actual code that uses an API