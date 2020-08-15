# See for protocol info: http://img.banggood.com/file/products/20180830020532SKU645408.pdf
# See for optimla reading with pyserial https://github.com/pyserial/pyserial/issues/216
import serial
from struct import *

'''
0x5a header
0x5a header
0x15 frame type
0x03 amount of data
data_h high 8 bits
data_l low 8 bits
mode mode 8 bits
chsm sum of data and truncated to lower 8 bits

'''

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    # make sure there are at least two pakets of data available
    while ser.in_waiting < 8:
        pass
    # read byte by byte until the start character is found
    fr = ser.read(8)
    # test frame for validating decoding
    #fr = b'\x5A\x5A\x15\x03\x04\x35\x02\x07' # exoect 1077mm and mode 2
    print(fr)

    if hex(fr[0]) == "0x5a" and hex(fr[1]) == "0x5a" and hex(fr[2]) == "0x15": #and hex(fr[3]) == "0x03":
        # expecting a valid frame
        distance, mode, chsm = unpack('>HBB', fr[4:])
        print(distance,mode,chsm)