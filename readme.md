
<br>Build the docker image 
<br>    docker build -t my_app . --no-cache
<br>Prior to building the image, please make sure the device_data.json is modified with servers accessible from your network.
<br>Run the image
<br>    docker run -it my_app

<br>Once you are in, goto /usr/src/app. You will find all the code in that location.
<br>Please run with python3.6 instead of python