# final_project

# What is it
boxes that turn round! When someone walks in the room, my boxes look at them!

I've downloaded a motion sensing program, called Motion, to my Raspberry Pi. When someone walks into the camera frame, I've used a built in Motion function, called Event On, to turn the block towards that person. When the person walks out of the frame, the Event Off function turns the blocks back to their base state.

The Event On function calls a shell script which, in turn, runs a Python script which activates a serial session and sends a "1" to the Arduino. The Arduino interprets the "1" as a high state and turns the servos (on which the blocks are mounted) to a defined position until it recieves a "0".  To send the "0", Motion behaves in a similar manner. When that person leaves the frame, the Event Off function will call a shell script, which then calls a Python script, which sends the "0" via serial to the Arduino. Once the "0" is recieved, the Arduino will turn the servos back to their starting position. 

# Problems

1) Segmentation Faults

  Motion works by continually taking pictures at a specified rate. It saves the photos to a location and compares the most recent photo with the last photo. If there are changes, Motion runs the Event On function. This method takes up a ton of space on my Pi and was triggering seg faults. I worked around this by saving the pictures to a folder on my desktop called stinky_pics which I clear out after every session.

2) Serial Mysteries

The python file alone cannot initiate a serial session, despite having `serial.Serial('/dev/ttyUSB0', 9600)` written in. I've tried debugging this, but found a functional workaround by opening a serial monitor manually in Arduino.

3) Servo Trouble

  We initially wanted to use larger blocks mounted on larger servos. Unfortunately, the servos we found were propietary Meccano servos, so we were unable to find relevant data sheets. When we plugged them into our circuits, they knocked the Arduino's offline. We were ultimately unable to resolve this, so opted to go with the smaller servos and laser cut/origami boxes.


# Printing the Boxes
[servo mount](https://www.youtube.com/watch?v=YtCwzTg-Wek)

[box no fit](https://www.youtube.com/watch?v=iaxFFt6FpS0)




# Code Vids

[Final project success!](https://youtu.be/HbOEPSdQ5ss)

[3 servo success](https://www.youtube.com/watch?v=TaTb5RKhFxs)

[raspberry pi to arduino to servo success](https://www.youtube.com/watch?v=B6R78sFvO4M)

# Reaction Vids
[Vid 1](https://youtu.be/kg2Wc3Oz3Ic)

[Vid 2](https://youtu.be/xynTfQRb8lw)

[Vid 3](https://youtu.be/n70Gojgj8r4)

[Vid 4](https://youtu.be/e8Hx_xIOZo8)

[Vid 5](https://youtu.be/qFUbc_twAZQ)

[Vid 6](https://youtu.be/yMtPaqgF0y4)

# Sources

1. Motion Sensing https://motion-project.github.io/motion_config.html

2. Serial Communication Between Arduino and Rasp Pi https://classes.engineering.wustl.edu/ese205/core/index.php?title=Serial_Communication_between_Raspberry_Pi_%26_Arduino
