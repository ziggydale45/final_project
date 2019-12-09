# final_project

# What is it
boxes that turn round! When someone walks in the room, my boxes look at them!

I've downloaded a motion sensing program, called Motion, to my Raspberry Pi. When someone walks into the camera frame, I've used a built in Motion function, called Event On, to turn the block towards that person. When the person walks out of the frame, the Event Off function turns the blocks back to their base state.

The Event On function calls a shell script which, in turn, runs a Python script which activates a serial session and sends a "1" to the Arduino. The Arduino interprets the "1" as a high state and turns the servos (on which the blocks are mounted) to a defined position until it recieves a "0".  To send the "0", Motion behaves in a similar manner. When that person leaves the frame, the Event Off function will call a shell script, which then calls a Python script, which sends the "0" via serial to the Arduino. Once the "0" is recieved, the Arduino will turn the servos back to their starting position. 

# What is it

Segmentation Fault

Serial session not starting unless serial monitor manually opened in Arduino.

Big Servos not working


# Printing the Boxes
[servo mount](https://www.youtube.com/watch?v=YtCwzTg-Wek)

[box no fit](https://www.youtube.com/watch?v=iaxFFt6FpS0)


# Code Vids
[3 servo success](https://www.youtube.com/watch?v=TaTb5RKhFxs)

[raspberry pi to arduino to servo success](https://www.youtube.com/watch?v=B6R78sFvO4M)

# Sources

1. Motion Sensing https://motion-project.github.io/motion_config.html

2. Serial Communication Between Arduino and Rasp Pi https://classes.engineering.wustl.edu/ese205/core/index.php?title=Serial_Communication_between_Raspberry_Pi_%26_Arduino
