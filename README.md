# DIS-finalproject

Note: This repository is part of the final submission of Rutgers course 198:553 Design of Internet Services.

The code files are used to setup a web application and test the performance of several EC2 Instance accross multiple regions.

The repo contains the following files/directories:
- Setup of web app:-
  - app.py : Python file that runs simple Flask web application and renders an HTML template file named form.html and an API to handle the login request by  calling an API to an existing DynamoDB table. (the code is well commented for understanding)
  - templates/: contains HTML file to be rendered.
  - form.html: HTML file that returns a form that accepts credentials
  - configure.sh : Bash file that can be used to install all dependencies, clone and run all commands needed to setup the webserver and application.
  - flaskapp : nginx configuration file to redirect traffic coming to the IP from given server to the local host where the app is running
  
- Test performance:-
  - testLatency.py: Python script to check and graph results of latency of all servers.
  - testRecoveryTime.py: Python script to test the recovery time of the server when the server fails completely

## To manually setup the application.
  - Step 1: Launch an EC2 instance. Make sure the security group allows all traffic from the internet to port 80 and 8080 from any IP.
  - Step 2: SSH into the instance and install all dependencies. Run the following commmands :
            - sudo apt-get update -y
            - sudo apt-get install -y git python3 nginx python3-pip gunicorn3
            - sudo pip3 install flask boto3
            
  - Step 3: clone this repo to get the app.py file and template folder. Go to the directory /etc/nginx/sites-enabled and copy the flaskapp file here. Since, the IP is this instance is not configued in my domain(shobhitsingh.com), add the public IP to line 3 of flaskapp file to be able to test the application using the IP.
  - Step 4: run "sudo service nginx restart" then switch present working directory to where app.py is located and then run "nohup gunicorn3 app:app &" command. This will ensure the WSGI keeps running in the backgroud.
  
  Congratulations! You now a web application running in cloud that can be accessed using the public IP of your instance.
  
## Setup the application using bash file
  
  To make it easy to test and setup, we have attached a bash file, configure.sh that can be run to replicate the entire process described above. This code works on Stand alone server. and the application be accessed using the public IP of the server to access the application.<br>
  This is the part that needs to be replicated for testing if needed. Please refer Demo video Part 1 for ease. Total time to run this code on server is about 1-2 minute.<br>
  Note: If you want to clone and replicate using git clone and then run the configure.sh file, make sure to copy the sh file outside or else it will mess up the flow by changing the paths.
  
  Also, we use the following code as userdata when launching the EC2 instance behind out load balancer. This works on our load balancer only because the server is directed to out doman which points to the static application load balancer. The server IP can change in stand alone server so the below code will not work for that.<br>
  
#!/bin/bash <br>
sudo apt-get update -y <br>
sudo apt-get install -y git python3 nginx python3-pip gunicorn3 <br>
sudo pip3 install flask boto3 <br>
git clone https://github.com/Shobhit29075/DIS-finalproject.git <br>
sudo cp DIS-finalproject/flaskapp /etc/nginx/sites-enabled/ <br>
sudo systemctl restart nginx <br>
cd DIS-finalproject <br>
nohup gunicorn3 app:app & <br><br>
  
Thank you.
