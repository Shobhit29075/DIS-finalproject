sudo apt-get update
sudo apt-get install git
yes '' | sudo apt-get install python3
yes '' | sudo apt-get install nginx
yes '' | sudo apt-get install python3-pip
sudo pip3 install flask
yes '' | sudo apt-get install gunicorn3 
sudo pip3 install boto3
git clone https://github.com/Shobhit29075/DIS-finalproject.git
cd DIS-finalproject
sudo chown "$(whoami)" flaskapp
python3 change_flaskapp.py
sudo cp flaskapp /etc/nginx/sites-enabled/
cd /etc/nginx/sites-enabled/
sudo service nginx restart
cd ~
cd DIS-finalproject
yes '' | nohup gunicorn3 app:app &
