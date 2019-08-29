import requests

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=inauthor:Jake+VanderPlas")

if response.status_code == 200:
    response_dict = response.json()

    books = response_dict["items"]

    for book in books:
        info = book["volumeInfo"]
        print(info["title"])
else:
    print("Error: unable to retrieve books.  Server responded with status code", response.status_code)