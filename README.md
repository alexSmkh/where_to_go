# Where to go

This service helps people find interesting places to spend a weekend. Here is a map with locations, clicking on which will open a description.

![](sample.gif)

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
5. Create the database: `./manage.py migrate`
6. Create the admin: `./manage.py createsuperuser`
7. Run server: `./manage.py runserver`
8. [Enjoy](http://127.0.0.1:8000)

### How do you load test places?
You can load a place from a json file, which should be:
```text
{
    "title": "...",             # max = 100 symbols
    "imgs": [
        "https://url/to/image.jpg",
        "...",
        "...",
        "..."
    ],
    "description_short": "...", # max = 1000 symbols
    "description_long": "...",  # max = 10000 symbols
    "coordinates": {            # float values
        "lng": "...",           
        "lat": "..."
    }
}
```

Run command: `./manage.py load_place --path [path]`, `path` - the path to file or directory containing the json files.

Test places data located in the `seed_place_data` directory.
