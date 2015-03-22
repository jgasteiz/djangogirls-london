# Djangogirls Blog

This is a sample Djangogirls blog. It's been built following [their tutorial](http://tutorial.djangogirls.org/en/django_start_project/README.html).

Before continue reading, make sure you feel comfortable using the Terminal or Command Line, it'll be important for understanding what's going on here. Remember you can always go back to the tutorial and practice some more with [Introduction to the command-line interface] chapter(http://tutorial.djangogirls.org/en/intro_to_command_line/README.html).

Now, some instructions on how you can download this code so you can play with it in your computer.

1. In your computer to the `djangogirls` directory you created during the tutorial and clone (means "download" in _git_ words) this project in it. If you deleted the djangogirls directory, you might want to create a new one.
```
[Go to the directory that contains the djangogirls directory]
$ cd djangogirls
$ git clone https://github.com/jgasteiz/djangogirls-london.git djangogirls-solution-javi
```

2. Go into the project directory and create a new virtualenv.
```
$ cd djangogirls-solution-javi
$ python3 -m venv myvenv
```

3. Activate the environment, install Django and other dependencies.
```
$ source myvenv/bin/activate
(myvenv) $ pip install django==1.7.7
(myvenv) $ pip install dj-database-url gunicorn whitenoise
```

4. Create the database by creating and running the migrations.
```
(myvenv) $ python manage.py makemigrations blog
(myvenv) $ python manage.py migrate
```

5. Create a superuser. Remember this is just for playing locally, there's no need for entering a complicated password here.
```
(myvenv) $ python manage.py createsuperuser
```

6. Run the server!
```
(myvenv) $ python manage.py runserver
```

7. Login. Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the user and password you just created. After that, you should be able to go to http://127.0.0.1:8000/, create a new post by clicking the **+** sign you should see on the top right.

## Extras

Although this blog is pretty much what the tutorial explain, it has a couple of small extras:

- Buttons, urls and views for publishing and unpublishing posts in the `post_detail.html` template.
- In the `post_detail.html` and `post_list.html` templates, the post content is rendered like this: `<div>{{ post.text|urlize|linebreaks }}</div>`. That means that if you paste a link in the post, the link will be clickable. The filter `urlize` included there, gives us that functionality.
- Unpublished posts appear in the post list for signed in users.
- This code has been added to `mysite/settings.py` to check if a user is logged in or not.
```
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)
```
- Not signed in users are not allowed to create or edit a post.
