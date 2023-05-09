
# URL Shortener

![Pytest-cov Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen)
![Read the docs](https://img.shields.io/badge/Documentation-Yes-green)
[![Beerware License](https://img.shields.io/badge/License-Beerware-blue)](https://github.com/AdiQ777/url_shortener/blob/master/LICENSE)

A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.



## Demo

[URL Shortener Heroku](https://heroku.com)

## Tech Stack


**Server:** Python, Django, Django Rest Framework, Poetry, Postgres


## Run Locally

Clone the project

```bash
  git clone https://github.com/AdiQ777/url_shortener
```

Go to the project directory

```bash
  cd url_shortener
```

Set environment variables

```bash
  cp ./envs/api.default.env ./envs/api.env
  cp ./envs/postgres.default.env ./envs/postgres.env
  # set variable values
```

Start the Docker containers

```bash
  docker compose up
```

Go to your Client and type:

```bash
  http://127.0.0.1:8000/api/schema/swagger-ui/
```
## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file:

`DJ_SECRET_KEY` - Django secret key for CSRF [gist](https://gist.github.com/AdiQ777/761ccf7cadc6cd885776623576cb593c)

`DJ_DEBUG` - Production development mode

`DJ_ALLOWED_HOSTS` - Allowed hosts for Django

`LOGGING_LVL` - Python logging package levels

`DJ_SU_NAME` - Default superuser name

`DJ_SU_EMAIL` - Default superuser email

`DJ_SU_PASSWORD` - Default superuser password

Also variables to your ./envs/postgres.env file:

`POSTGRES_USER` - Postgres root user

`POSTGRES_PASSWORD` - Postgres root password

`POSTGRES_DB` - Postgres root database name

`POSTGRES_HOST` - Database host name (docker compose service name)

`POSTGRES_PORT` - Database port
## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/AdiQ777/url_shortener/e566805d2a8868f821378e06d2959fa5cbfef6c3/screenshots/Screenshot%202023-05-09%20at%2021.44.58.png?token=GHSAT0AAAAAACBM3CKUM6P5POXMUNEULQHAZC2UT5A)



## Author

- [@AdiQ777](https://github.com/AdiQ777)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/AdiQ777?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adrian-balicki-22095b8b/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

