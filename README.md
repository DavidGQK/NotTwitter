# NotTwitter is a social blogger platform<br/>

## How to transfer to your computer

1. Create folder "Project"
2. Clone GitHub repository
3. You are awesome!

## Quick local start [for Windows]

### Step 1
in `Project/NotTwitter`
```
python -m venv venv
source venv/Scripts/activate
```
in `Project/NotTwitter/NotTwitter`
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Step 2 (optional)
Set the flat pages in the Admin Panel (these flat pages are connected with the footer of the main page)

- Go to Admin Panel (http://127.0.0.1:8000/admin or another local server in your system)

- Go to Sites

- Change click on `example.com` and change all fields to http://127.0.0.1:8000/

- Add a new flat page about the author:
  - URL: /about-author/
  - Header: About author
  - Content: ***content***
  - Site: http://127.0.0.1:8000/ (or another local server in your system)
  - Save

- Add a new flat page about technologies:
  - URL: /about-spec/
  - Header: Technologies
  - Content: ***content***
  - Site: http://127.0.0.1:8000/ (or another local server in your system)
  - Save

### Step 3
Open http://127.0.0.1:8000 (or another local server in your system)

## Heroku deploy [for Windows]

Open **Settings.py** in `Project/NotTwitter/NotTwitter`

1. In **ALLOWED_HOSTS** set the name of the project on Heroku
2. Comment **Database** variable for local start
3. Uncomment **Database** variable for Heroku deploy
4. Change **Database** variable for your server settings by example in code
5. Run ```waitress-serve --listen=*:8000 NotTwitter.wsgi:application```
6. If everything is alright you can start deploying with an official Heroku instruction
