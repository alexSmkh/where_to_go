# Where to go

This service helps people find interesting places to spend a weekend. Here is a map with locations, clicking on which will open a description.

![](https://dvmn.org/media/lessons/ezgif.com-gif-maker_4nWhtfQ.gif)

### You can see a demo app [here](https://alexsmkh.pythonanywhere.com/)
Login / password for the admin panel: `admin` / `123456`
    

### What you need to start this app locally
You must have the following installed:
```text
python >= 3.8
pip
virtualenv
```

1. Clone project: `git clone https://github.com/alexSmkh/where_to_go.git`
2. Create a virtual environment using virtualenv
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file in the root folder and write env variables in it:
```text
DEBUG=TRUE
SECRET_KEY=*** generate any secret key ***
ALLOWED_HOSTS=127.0.0.1,localhost
```
5. Create the database:
```text
python manage.py makemigrations
python manage.py migrate
```
6. Run server: `python manage.py runserver`
7. [Enjoy](http://127.0.0.1:8000)

    