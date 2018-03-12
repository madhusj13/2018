
Build the docker image
    docker build -t my_app . --no-cache
Prior to building the image, please make sure the device_data.json is modified with servers accessible from your network.
Run the image
    docker run -it my_app

Once you are in, goto /usr/src/app. You will find all the code in that location.
Please run with python3.6 instead of python