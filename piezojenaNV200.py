import numpy as np
import serial
import time
from matplotlib import pyplot as plt

class piezojenaNV200:
     def __init__(self, port='COM3', baudrate=115200, timeout=0.25):
         self.port = port
         self.baudrate = baudrate
         self.timeout = timeout
         self.connection = None

     # setting configuration for closed loop:
         
     def init_stage(self):
        self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout, xonxoff=True)
        self.connection.write(b'\r')  # Query device prompt response
        print(self.connection.readline().decode(), end='')  # Read and
        commands = [
            b'modsrc,0\r',
            b'reset\r',
            b'cl,0\r',
            b'set,0.0\r'
         ]
        for command in commands:
            self.connection.write(command)
            time.sleep(1)  # Wait for actuator to change position
        print('Initialized for the closed loop')

     # setting configuration for the open loop 
     def init_stage_ol(self):
        self.connection = serial.Serial(self.port, self.baudrate, timeout=self.timeout, xonxoff=True)
        self.connection.write(b'\r')  # Query device prompt response
        commands = [
            b'modsrc,0\r',
            b'reset\r',
            b'cl,1\r',
            b'set,0.0\r'
        ]
        for command in commands:
            self.connection.write(command)
            time.sleep(1)  # Wait for actuator to change position
        print("Initialized for the open loop")

        
     def query_position(self):
        self.connection.write(b'meas\r')
        response = self.connection.readline().decode()
        print(str(response))
        position_start = response.find(',') + 1  # Find the position
        position_end = response.find('\r')  # Find the position where
        position_value = response[position_start:position_end]
        return float(position_value)

     def set_position(self, target_position):
         command = f'set,{target_position}\r'
         self.connection.write(command.encode())
         time.sleep(0.2)  # Wait for actuator to change position

     def close_connection(self):
         if self.connection:
             self.connection.close()
         print('connection closed')


##
#nv200_instance = piezojenaNV200()
#nv200_instance.connect()

##
""" nv200_instance.set_configuration()
nv200_instance.set_position(0) """

##
#nv200_instance.set_position(1)

##
#nv200_instance.set_position(300)
#positions = np.zeros([100,1])
#for i in np.arange(0,100):
#     pos = nv200_instance.query_position()
#     positions[i] = pos

#plt.figure("Position accuracy test")
#plt.clf()
#plt.subplot(1,2,1)
#plt.plot(positions)
#plt.title("Setppoint: 100um, standard deviation: {:.2f}
#nm".format(np.std(positions*1e3)))
#plt.ylabel("Position (micro meter)")
#plt.xlabel("Number of position queries")

##
#move_to = np.linspace(200,200.5,100)
#read_positions=move_to*0.0
""" for ind, pos in enumerate(move_to):
     print(ind)
     nv200_instance.set_position(pos)
     current = nv200_instance.query_position()
     read_positions[ind] = current """
""" 
plt.subplot(1,2,2)

plt.plot(move_to,read_positions)
#plt.title("Setppoint: 1um, standard deviation: {:.2f}
nm".format(np.std(positions*1e3)))
plt.ylabel("Measured Position (um)")
plt.xlabel("Set position (um)")

plt.tight_layout()
##
nv200_instance.close_connection() """