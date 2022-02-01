import serial

#for j in range(227):
#    for i in range(227):
#        img_pixels[j, i] = 150

def serial_ports():
    # produce a list of all serial ports. The list contains a tuple with the port number,
    # description and hardware address
    #
    ports = list(serial.tools.list_ports.comports())

    # return the port if 'USB' is in the description
    for port_no, description, address in ports:
        if 'USB' in description:
            return port_no
            
ser = serial.Serial(
    port=serial_ports(),
    baudrate=57600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()