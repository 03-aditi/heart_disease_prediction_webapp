# heart_disease_prediction_webapp
This web application running on the docker container tells you about the prediction of heart disease in upcoming 10 years
# Step 1 : I have created a machine learning model with the help of dataset provided 
# Step 2 : Dumped the model in a file named as "heart_disease_prediction.pk1"
# Step 3 : Created a webserver with httpd on CentOS container having GUI enabled
# Step 4 : Created a webpage "index.html" having the form which will collect the data for prediction
# Step 5 : Created a python CGI page "data.py" which will load our machine learning model and provide the prediction on another page
# Step 6 : The image which has been used in the background of webpage is "heart3.jpg" 
# Step 7 : Placed "heart3.jpg" and "index.html" in /var/www/html/ folder and "data.py" in /var/www/cgi-bin/ folder

# docker installation
yum install docker-ce
# httpd installation
yum install httpd
# pulling image from hub.docker.com
docker pull centos:latest
# launch the container
docker run -it --name yourcontainername --env=DISPLAY --volume=/tmp/.X11-unix -p 92:80 centos:latest
# (92 port is of baseOS which will transfer the traffic to 80 port of webserver inside container)
# ensure scikit-learn library of python should be installed on container
pip install scikit-learn



# docker pull aditi03/heart_disease_detect:v1
If you wanna try the web application without the headache of building the whole infrastructure, just pull my image from hub.docker.com

