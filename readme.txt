INITIALIZATION:

#install python 3.8

#create environmrnt
python3 -m venv appnameenv

#activate environment
source appnameenv/bin/activate (linux)
appnameenv\Scripts\activate (windows)

#install dependencies
pip install -r requirements.txt

#launch app
python3 manage.py runserver

#install your OS version MongoDB 4.4

#test postman endpoints on local prior to deploying production

#Follow DigitalOcean manual on deploying the app on Ubuntu 18/20/22 and Nginx using uwsgi/gunicorn.





INSTRUCTION:

#auth and payments prints for pesapal included, add ecommerce backend api function with product view counts.

#ensure the Flask and React API functions for the corporate ecommerce (as shared) and retail product (Figma based) are well modulated in the ecommerce blurpints.




##Hint: Add your main methods to the mainModules folder under a new sub directory for each new class/method, to easen asbtraction.
##Hint: Create new subfolders under prints/ecommerce to microservice the ecommerce function better to allow for easierConitnous Deployment and Continous Advantage.







ADDENDUM:
#the various prints are in print folder (models,views, api, minor methods)
#model in models.py, controller in api.py and jinja #templating service (view) in views.py
#methods in mainModules folder
#templates or static files in <static or templates>/<prints namee> subfolder
create new prints, static, and templates folder for each microservice.
#postman json in docs/technicals/postmanCollections
