Project Guide 
--------------
   
  Project Name - Simple Student Management System
  
    Project Overview : 

        - This project follows a 3-tier architecture with a React frontend, Flask-based application layer, and MongoDB as the data layer. The backend is organized using   controller, service, repository, and model layers, which makes it cleaner and closer to industry practices.
        
        Operation
            
            - Search Student
            - Fetch Student
            - Add Student
            - Edit Student 
            - Delete Student

        Architecture Overview
            
            - OOPs , MVC 
            - Flask 
            - 3 Tier Web Application

            - venv → for Python packages

            - npm / vite → for Node.js packages

        Good to Know 

             - axios ----- for api 
             - cros ------ for cross url     
            

     Tech Stack 
          
           Frontend - Css , React 

           Backend  - Flask , Python (Oops + MVC + Exception Handling) 

           Database - MongoDB 
                          - sudo systemctl start mongod


    Frontend Tools : 
            
            - cd ~/Videos/3-python/5.WebProjects/student_crud_react_flask_python_mongodb
            - npm create vite@latest frontend -- --template react

                 - some configuration need to - select

            - cd frontend
            - npm install
            - npm install axios


    Backend Tools : 

            - cd backend
            - python3 -m venv venv
            - source venv/bin/activate
            - pip install -r requirements.txt 

    
### How to Setup and Start the Project To Work


    - MongoDB 

       - sudo systemctl status mongod

       - sudo systemctl start mongod
     
    - Frontend 

          - cd frontend
          - npm install 
          - npm run dev 

          - open browser :- http://localhost:5174/   | http://localhost:5173/   # verify if it is working or not 

          - Always check the Console and Network tabs for any issues.
          

    - Backend 
       
          - cd backend
          - sudo apt install python3-venv
          - source venv/bin/activate
          - pip install -r requirements.txt
          - python3 app.py        


          - http://127.0.0.1:5000/                 # verify the backend 

          - http://127.0.0.1:5000/api/students/    # verify data


          - check if any application taking the same port   # lsof -i :5000
          - kill -9 port_ID


    - Postman 

        -       

                      