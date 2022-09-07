# FLASK DEMO

This repo is about basics of flkask api and how to deploy a one on one machine learning web application in heroku.

- pip install gunicorn in our venv
- create procfile
- make requirements.txt file with command pip freeze > requirements.txt


## Common mistakes to avoid error in heroku
1 . check spelling
   - your app name should be in app.py only because its connected with gunicorn
   - spelling for requirements.txt not----------not requirement.txt ---missing's'
   - spelling for Procfile----------P should be in caps
   - spellings for templates----------lowercase for 't' and template ---missing 's'
   - 
2 . gunicorn mistakes
   - not installed gunicorn--------check your requirements.txt for gunicorn.
   - Procfile error
