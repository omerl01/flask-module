import requests
url = "https://jsonplaceholder.typicode.com/"
# posts section get all posts
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
# print(len(data), response.status_code)

# # specific post
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# data = response.json()
# print(data)

# posts by user
# repsonse = requests.get(f"{url}posts?userId=1")
# data = repsonse.json()
# print(data)

# create post
# body = {
#     "title": "mr bean",
#     "body": "hi there"
# }
# response = requests.post(f"{url}/posts",json=body)

# data = response.json()
# print(data)

# update post
# data = {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "this is a change"
# }
# response = requests.put(f"{url}/posts/1", json=data)
# data = response.json()
# print(data)

# patch post change
# response = requests.patch(f"{url}posts/1", data={"title": "changed title"})
# data = response.json()
# print(data)

# delete post
# response = requests.delete(f"{url}posts/1")
# data = response.json()
# print(data, response.status_code)

# get comments for post
# response = requests.get(f"{url}posts/1/comments")
# data = response.json()
# emails = [item["email"] for item in data]
# print(emails)


# part 2 comments

# get all comments
# response = requests.get(f"{url}comments")
# data = response.json()
# print(data)

# get commetn by id
# response = requests.get(f"{url}comments/1")
# data = response.json()
# print(data)

# filet comment by post
# response = requests.get(f"{url}comments", params={"postId": 1})
# data = response.json()
# print(data)

# create commment
# comment = {
#     "postId" : 1,
#     "id" : 5,
#     "name" : "omer",
#     "email" : "gdg",
#     "body": "this is a comment"
    
# }

# response = requests.post(f"{url}comments", json=comment)
# data = response.json()
# print(data)


# delete comment
# response = requests.delete(f"{url}comments/1")
# data = response.json()
# print(data)

# part 3 albums

# get all albums
# response = requests.get(f"{url}albums")
# data = response.json()
# print(data)

# get album by id
# response = requests.get(f"{url}albums/1")
# data = response.json()
# print(data)

# get photos titles
# response = requests.get(f"{url}albums")
# data = response.json()
# titles = [item["title"] for item in data]
# print(titles)

# create an album
# album = {
#     "title": "mr jones",
    
# }
# response = requests.post(f"{url}albums", json=album)
# data = response.json()
# print(data)


# delete album
# response = requests.delete(f"{url}albums/2")
# data = response.json()
# print(data)

# part 4 photos

# get all photos
# response = requests.get(f"{url}photos")
# data = response.json()
# print(data)

# get photo by id
# response = requests.get(f"{url}photos/1")
# data = response.json()
# print(data)

# filter photos by albums
# response = requests.get(f"{url}photos", params={"albumId": 1})
# data = response.json()
# print(data)

# create a photo
# photo = {
#     "albumId": 50,
#     "id": 50,
#     "title": "mr jones",
#     "thumbnailurl": "httpsmvdm"
# }
# response = requests.post(f"{url}photos", json=photo)
# data = response.json()
# print(data)

# delete a photo
# response = requests.delete(f"{url}photos/1")
# data = response.json()
# print(data)


# part 5 - todos

# get all todos
# response = requests.get(f"{url}todos")
# data = response.json()
# print(data)

# get todo by id
# response = requests.get(f"{url}todos/1")
# data = response.json()
# print(data)

# filter todo by user
# response = requests.get(f"{url}todos", params={"userId": 1})
# data = response.json()
# print(data)

# filter by competion
# response = requests.get(f"{url}todos", params={"completed": "true"})
# data = response.json()
# print(data)

# create a todo
# todo = {
#     "userId": 5,
#     "id": 2,
#     "title": "clean",
#     "completed": False,
# }
# response = requests.post(f"{url}todos", json=todo)
# data = response.json()
# print(data)

# update completed
# response = requests.patch(f"{url}todos/1", json={"completed": True})
# data = response.json()
# print(data)

# delete todo
# response = requests.delete(f"{url}todos/1")
# data = response.json()
# print(data)


# part 6 - users

# get all users
# response = requests.get(f"{url}users")
# data = response.json()

# users_and_emails = [(item["name"], item["email"]) for item in data]
# print(users_and_emails)
 
# get user by id
# response = requests.get(f"{url}users/1")
# data = response.json()
# print(data["address"]["city"])

# get posts by user
# response = requests.get(f"{url}posts", params={"userId": 1})
# data = response.json()
# titles = [item["title"] for item in data]
# print(titles)

# get todos by user titles
# response = requests.get(f"{url}todos", params={"userId": 1})
# data = response.json()
# titles = [item["title"] for item in data]
# print(titles)

# get albums by user titles
# response = requests.get(f"{url}albums", params={"userId": 1})
# data = response.json()
# titles = [item["title"] for item in data]
# print(titles)

# create a user
# user = {
#     "name": "Joe",
#     "company": "puzzle"
# }
# response = requests.post(f"{url}users", json=user)
# data = response.json()
# print(data)


# delete user
response = requests.delete(f"{url}users/1")
data = response.json()
print(data, response.status_code)
