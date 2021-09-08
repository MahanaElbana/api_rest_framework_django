# api_rest_framework_django
    ------- Django Backend ---------
       
        
                     /---------/---------- first step -----//----------/
                     
   1] " after create new folder " :- from inside folder open terminal and
        write the following command to open folder in vs code :- 
        
        ``` Shell
            code .
        ```    
   
   2] install virtual environment (venv) :- write the following command in terminal :-
    ``` Shell
           pip3 install virtualenv
    ```       
           
   3] you’ll set up a new virtual environment using your command line:  
           python3 -m venv 'the_name_of_virtual_environment'
                            or 
           virtualenv  'the_name_of_virtual_environment'   
           
   4] run or activate virtual enironment :- then install django :- using the following command line: 
           source ./name_of_virtual_environment/bin/activate                      
                 
   5] install django after activating venv :- by using the following command line 
           python3 -m pip install django  
           
   6] to update pip :- write the following command line :-
          python3 -m pip install --upgrade pip      
          
   7] to know version of [python] and [Django] inside venv :- after activating venv :- from following command line:-
          python3 --version
          python -m django --version
          
   8] if you want to update [Django] or [python] :- from command use :- selection version is optional :-
         pip install --upgrade django ==3.9.5    
         sudo apt upgrade python 
         
   9] Pin your dependencies :- write all packages or libraries in requirements.txt :- using line command :-
         python -m pip freeze > requirements.txt  
         
   10] to know libraries which installed on env :-
     - pip freeze 
     
   11] to save libraries in text file :- another method:=
     - pip freeze > requirements.txt   
                               
                               
                      /-------//---------- next step -----//---------/  
                      
   1] Set up a Django project  or create project of django :-  from command line :- 
          django-admin startproject  'the name of project '
           
   2] "--- for creating App ---" :- write the following command in terminal :-
          python manage.py startapp  name_of_app    
          
   3] " --- After create app ---" :- add App in [settings] in [INSTALLED_APPS]  
   
   4] should inside folder which contain file(manage.py) then :- write the following 2 commands
         python manage.py migrate
         pythin manage.py runserver   
         
   5] if you want change port :- write any port from 8000 to 8999 :- for example
         pythin manage.py runserver 8888   
   
   4] "--- to deactivate virtual environment ---":- write the following commend in terminal :- 
          deactivate
          
   5] to install rest framework :- write in command :- 
         pip install djangorestframework      
   
   6] after constructing admin ,model , urls ,serializer ,views for apps :- write the two commands :- 
         python manage.py makemigrations 
         python manage.py migrate 
         
   7] to create super user :- 
         python manage.py createsuperuser
   
   
   
   
   ////////////////// ----- recently , important links for rest frame work , django  ,and others ------------------//////////
   
   1] https://www.django-rest-framework.org/
   2] https://www.programcreek.com/python/example/71197/rest_framework.permissions.SAFE_METHODS
   3] https://data-flair.training/blogs/python-ordereddict/
   4] https://www.w3schools.com/python/default.asp
   5] https://docs.djangoproject.com/en/3.2/topics/db/models/ 
   1] Lorem Ipsum 
          
          
          
