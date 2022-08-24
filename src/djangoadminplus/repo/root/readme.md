# PROJECTNAME

## Clone From The GitHub

First we get the code files from the GitHub.

```bash
$ git clone ...
```

## Create And Activate Virtualenv

Create a virtual environment based on Python > 3.9\* and activate it.

```bash
$ virtualenv venv
$ source venv/bin/activate
```

## Install Requirements

```bash
$ mkdir -p files
$ mkdir -p uploads
$ pip install -r requirements.txt
$ mv my/path/.env .
```

## Migrate

```bash
$ python manage.py migrate
```

## Collect Static

```bash
$ python manage.py collectstatic
```

## Create Super User

```bash
$ python manage.py createsuperuser
```

## Run Server

```bash
$ python manage.py runserver 8000
```

## License

