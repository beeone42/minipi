import serial, io, urllib, string, os, subprocess, time

def sprint(ser, txt):
    ser.write(txt)
    ser.flush()

def goto_top_left(ser):
    sprint(ser, "\r")
    sprint(ser, chr(27) + '[40A');

def erase_scr(ser):
    sprint(ser, chr(27) + '[2J')

def reverse(ser):
    sprint(ser, chr(27) + '[7m')

def print_text(ser, content):
    lines = content.splitlines(True)
    for line in lines:
        sprint(ser, string.replace(line, "\n", ""))
        sprint(ser, "\r")
        sprint(ser, chr(27) + '[1B');

def print_file(ser, fname):
    with open(fname, 'r') as content_file:
        content = content_file.read()
        print_text(ser, content)

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=20, parity=serial.PARITY_NONE)
#sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

erase_scr(ser)

last_nb = 1
while True:
    response = urllib.urlopen('http://enroll.42.fr/usage.php/')
    nb = response.read()
    if (nb != last_nb):
        if (int(nb) >= 1000):
            font = "bigascii9"
        else:
            font = "bigascii12"
        output = subprocess.Popen(["figlet", nb, "-f", font, "-w", "40", "-c" ], stdout=subprocess.PIPE).communicate()[0]
#        print output

#        erase_scr(ser)
        goto_top_left(ser)
        print_file(ser, '42.txt')
#        print_file(ser, 'figlet.txt')
        print_text(ser, output)
        last_nb = nb
    time.sleep(10)

ser.close()
