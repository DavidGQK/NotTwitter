# NotTwitter is a social blogger platform [It is a pet project!]

## How to transfer to your computer

1. Create folder "Project"
2. Clone GitHub repository
3. You are awesome!


## Quick local start [for Windows]

### Step 1
in path *Project/NotTwitter/NotTwitter*
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Step 2
Set the flat pages in the Admin Panel (these flat pages are connected with the footer of the main page)

Admin Panel path: http://127.0.0.1:8000/admin

New flat page about the author:
1. URL: /about-author/
2. Header: About author
3. Content: ***content***
4. Site: http://127.0.0.1:8000/ (or another local server for your system)
5. Save

New flat page about technologies:
1. URL: /about-spec/
2. Header: Technologies
3. Content: ***content***
4. Site: http://127.0.0.1:8000/ (or another local server for your system)
5. Save

### Step 3
Open http://127.0.0.1:8000 (or another local server for your system)

## Heroku deploy [for Windows]

Open **Settings.py** in *Project/NotTwitter/NotTwitter*

1. In **ALLOWED_HOSTS** set the name of the project on Heroku
2. Comment **Database** variable for local start
3. Uncomment **Database** variable for Heroku deploy
4. Change **Database** variable for your server settings by example
in path *Project/NotTwitter/NotTwitter*
5. Run ```waitress-serve --listen=*:8000 NotTwitter.wsgi:application```
6. If anything is alright you can start deploying with an official Heroku instruction
