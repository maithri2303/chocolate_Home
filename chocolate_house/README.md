Introduction: This application is designed for a chocolate house to manage
Seasonal flavor offerings
Ingredient inventory
Customer suggestions and allergy concerns

clone the repository
navigate to project directory
install dependencies which is in requirements.txt
run the application at main.ty

build the docker image by navigating to docker file
or using below command
"docker build -t chocolate-house ."

run the container using below command
"docker run -p 5000:5000 chocolate-house"

before building docker file you can use the url for test
http://192.168.31.18:5000/flavors

after building dockeer file
you can test in 
http://localhost:5000/flavors

postman collection for your reference
https://elements.getpostman.com/redirect?entityId=39785201-d52f7cb6-4fd1-40f1-b940-d98cfe6edd5b&entityType=collection