# Deploy, run and test the sample application

We will build a simple express-based NodeJS application which responds to HTTP requests.

# Steps

* Clone the repository
* Go to the samplesDocker folder
* Run `docker build -t node-app .` to package the app to a container
* Run `docker images` to list and check the image
* Run `docker run -d -p 8080:8080 node-app` to invoke the container to run so that the application starts
* Run `docker ps` to check for the running container status
* Go to `http://localhost:8080/` from your favourite web browser
* You will see `Hello World` message!
* Run `docker stop {CONTAINER ID}` to stop the conatiner

# Note

* Internet must be connected

# Improvisations

* Create https instead of http
* Create certificates
