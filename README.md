gs
==

Installation
------------

# <- is comment

1. Remove *.db, if it found in your folder, remove folder migrations in each subfolder
2. Activate virtualenv

    source <path-to-virtualenv>/bin/activate    
    
    # you should found -> ( virtualenv-name ) in front of your prompt

3. Run commands below

    python manage.py syncdb

    # you should get prompt asking for setting stuff

4. Run server for testing

    python manage.py runserver

    # you can test server by access URL http://127.0.0.1:8000/admin (for administrator)


    
