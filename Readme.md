# Tasks

### Links to task Readme's 


[Task 1](apps/coffee_machine/Readme.md)

[Task 2](apps/boxed_and_dropped/Readme.md)

### Prerequisites

-[Docker](https://docs.docker.com/get-docker/)

### Build image

> With Docker running build the image

```sh
docker build .
```

### Start Docker

> The following command will run the django server and create a local postgres database.

```sh
 docker compose docker-compose up 
```
Depending on your docker version this may work for you instead(OPTIONAL)
```sh
 docker-compose -f docker-compose up  
```
Activate the virtual environment
```sh
 source venv/bin/activate 
```

    
### Code Formatting

Make sure code and test files are free of style errors by running flake8.
```sh
    flake8 tests/ src/
```
Tests
```sh
 python manage.py test apps

```

### Access on your browser
> The site should now be running at http://localhost:8000/