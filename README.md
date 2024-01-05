# BookLibrary Backend and Database

This project was developed using the following technologies:
- Python 3
- Python Flask
- Python Marshmallow
- SQLAlchemy
- SQlite
- Swagger
- Docker

## Notes
- I proposed a different model which is built around two tables: Authors and Users. Their relationships are as follows:

  ![entity-relation](https://github.com/Jhonier-Jimenez/flask-rest-api/assets/32853930/f232b04d-0f83-4a53-9812-45387eecef4b)
  
- I created all CRUD operations for both Books and Authors


## Instructions
- Install docker on your machine and run it
- `git clone` this repository or download it as a `Zip` file
- On the root folder, run `docker build -t backend-flask .` to create a docker image of the project
- Run `docker run -p 8000:8000 backend-flask` to start the image.
- Navigate to `http://localhost:8000/`. You should be able to see the home page of the backend application
- Navigate to `http://localhost:8000/api/ui/`. Here you can see the API's documentation built with Swagger and also try all of its endpoints
  
  ![image](https://github.com/Jhonier-Jimenez/flask-rest-api/assets/32853930/5e2b73a4-1e35-44c6-ad46-f7da152d2f8f)

- Run the [FrontEnd of the project ](https://github.com/Jhonier-Jimenez/book-app-frontend) by following the instructions there.
- Navigate to `http://localhost:4200` when you also get the frontend up and running to see and use the application on its full.

## Further development
- Since the backend is already providing all CRUD operations for Authors too, we should add the implementation for them in the frontend.
  
  ![image](https://github.com/Jhonier-Jimenez/book-app-frontend/assets/32853930/de0cf407-ff08-4e9b-ae6e-96cbd84c3ff6)
