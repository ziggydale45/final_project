import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.write('0')
ser.close()


