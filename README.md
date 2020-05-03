# heart_disease_prediction_webapp
This web application running on the docker container tells you about the prediction of heart disease in upcoming 10 years

# 1. yum install docker-ce
# 2. docker pull centos:latest
# 3. docker run -it --name yourcontainername --env=DISPLAY --volume=/tmp/.X11-unix -p 92:80 centos:latest
* (92 port is of baseOS which will transfer the traffic to 80 port of webserver inside container)

* I have created a machine learning model "HeartDiseasePrediction.py" with the help of dataset provided 
* Dumped the model in a file named as "heart_disease_prediction.pk1"

# 4. yum install httpd
# 5. /usr/sbin/httpd
* Created a webserver with httpd
* Make httpd webserver services persistent using bashrc file
* Created a webpage "index.html" having the form which will collect the data for prediction
* Ensure that firewall and selinux are disabled in baseOS

# 6. pip install scikit-learn
* ensure scikit-learn library of python should be installed on container
* Created a python CGI page "data.py" which will load our machine learning model and provide the prediction on another page
* The image which has been used in the background of webpage is "heart3.jpg" 
* Placed "heart3.jpg" and "index.html" in /var/www/html/ folder and "data.py" in /var/www/cgi-bin/ folder

# docker pull aditi03/heart_disease_detect:v1
If you wanna try the web application without the headache of building the whole infrastructure, just pull my image from hub.docker.com

