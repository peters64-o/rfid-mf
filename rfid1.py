"""
Python code that reads RFID fobs/cards
"""
import serial
import binascii
import string
ser=serial.Serial('/dev/ttyUSB0',9600,timeout=1)
cmd1="\xAA\x00\x02\x03\x26\x27\xBB"
cmd2="\xAA\x00\x01\x04\x05\xBB" # Anticol
cmd3="\xAA\x00\x01\x86\x87\xBB" # Version
cmd4="\xAA\x00\x01\x83\x82\xBB" # Get serial
cmd5="\xAA\x00\x03\x85\x01\x78\xFF\xBB" # User information
cmd6="\xAA\x00\x02\x03\x26\x27\xBB"     # Req
cmd7="\xAA\x00\x0A\x20\x01\x01\x10\xff\xff\xff\xff\xff\xff\x3A\xBB"     # MF Read
ser.write(cmd7)
x=ser.read()
y=binascii.b2a_hex(x)
s=[x]
z=[y]
while y != 'bb':
        x=ser.read()
        y=binascii.b2a_hex(x)
        s.append(x)
        z.append(y)
# print string.join(s, '')
# print string.join(z, ' ')
if len(z)>7:
	print string.join(["%s" % el for el in z[20:24]],'')
else:
	print 1
ser.close()
