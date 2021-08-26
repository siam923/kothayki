## Pipenv setup
Setup in Mac

1. brew install pipenv ( OR ) pip3 install pipenv 
2. atom ~/.bash_profile  [ Opening bash profile in text editor ] (ONE TIME) 
piWrite the following statements in .bash_profile at the end 
export LC_ALL=en_US.UTF-8 
export LANG=en_US.UTF-8 
Setup in Windows

1. Run Windows PowerShell as Administrator 
2. pip install pipenv 
3. Execute the following command and change MAHMUD to your user name ( ONE TIME ) 

set PATH=%PATH%;set PATH=%PATH%;'c:\users\MAHMUD\appdata\local\programs\python\python36-32\Scripts' 

Usage 
pipenv install bs4  (Installing package) 
pipenv shell (Activate) 
pipenv exit  (Quit) 

Removing:
pipenv --rm

## Migrating database
1. Dump db contents to json

```
$ ./manage.py dumpdata > dump.json
```

2. Switch the backend in settings.py

```
DATABASES = {
    # COMMENT OUT:
    # 'default': dj_database_url.config(default='sqlite:////full/path/to/your/database/file.sqlite'),
    # ADD THIS INSTEAD:
    'default': dj_database_url.config(default='postgres://localhost:5432/postgres_db_name'),
}
```

3. Syncdb and migrate the new DB to the same table structure

```
$ ./manage.py syncdb
$ ./manage.py migrate
4. Load the json to the new db.

$ ./manage.py loaddata dump.json
```

5. Congrats! Now the new data is in your postgres db.


## APi links
User details:
- http://localhost:8000/api/v1/rest-auth/user/

## Resources

1. JWT: https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

2. JWT in frontend: https://auth0.com/blog/secure-your-react-and-redux-app-with-jwt-authentication/

3. Django Filter: https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-filtering-part-5/

