import requests

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=inauthor:Jake+VanderPlas")

if response.status_code == 200:
    response_dict = response.json()

    books = response_dict["items"]

    for book_dict in books:
        info_dict = book_dict["volumeInfo"]
        print(info_dict["title"])
else:
    print("Error: unable to retrieve books.  Server responded with status code", response.status_code)