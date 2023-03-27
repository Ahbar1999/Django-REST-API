# RESTful API for a Blog Post

created with -> Django REST framework

endpoints -> 
1) GET - /all -> returns a list of all records
2) GET/POST - /create -> creates a new post with default data if GET otherwise with provided data in POST req
3) POST - /create/id -> updates a post with given id(if it exists) and returns it

features -> 
- Data is stored in a sqlite database
- JSON Serialization and deserialization is used to encode and decode data 

how to use ->
- make sure you have python 3.10 installed
- run: pip install pipenv
- cd into repo and create virtual env using pipenv, run: pipenv install to install all the deps
