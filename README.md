# DigitalMonsters

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/FEGranados/DigitalMonsters.git
$ cd DigitalMonsters
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p /usr/bin/python3 env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```bash
(env)$ cd DigitalMonsters
(env)$ python manage.py runserver
```
## Docker

The first thing to do is to clone the repository:

```bash
$ git clone https://github.com/FEGranados/DigitalMonsters.git
$ cd DigitalMonsters
```

Create a image and run:

```sh
$ docker image build -t monsters:v1 .
$ docker run -d -p 8000:8000 --name monsters monsters:v1
```


## App

Monsters: `http://127.0.0.1:8000/monsters/`


