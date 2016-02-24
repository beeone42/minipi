import serial
import io

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=20, parity=serial.PARITY_NONE)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
ser.write(u'Login:')
ser.flush()
s = ser.read()
print s
ser.close()
