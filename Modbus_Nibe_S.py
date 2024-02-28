# -*- coding: utf-8 -*-
import pandas as pd


from pymodbus.client import ModbusTcpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient # Use this for serial connection
import logging

# Enable logging for detailed debug output
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


# Modbus connection parameters
HOST = '192.168.0.145' # Example IP address, change to your device's IP
PORT = 502 # Default Modbus TCP port, change if different

# Example register address and count
REGISTER_COUNT = 1 # Number of registers to read

# Create a Modbus client
client = ModbusClient(HOST, PORT)

# Read Modbus list
df = pd.read_csv('C:\\Users\\..............\\Modbus_Nibe_S.csv')
#print(df)

try:
    # Connect to the client
    client.connect()

    # Read / wirte holding/input registers
    #client.read_input_registers(REGISTER_ADDRESS, REGISTER_COUNT)
    #client.write_register(REGISTER_ADDRESS, VALUE)
    #client.read_holding_registers(REGISTER_ADDRESS, REGISTER_COUNT)
    
    for index, row in df.iterrows(): 
        #print (index)
        #print(row)
        
        if row['Type register']=='MODBUS_INPUT_REGISTER':
            row['Actual value']=client.read_input_registers(row['Register'], REGISTER_COUNT).registers[0]
            print (row)
            df.at[index, 'Actual value'] = row['Actual value']
        elif row['Type register']=='MODBUS_HOLDING_REGISTER':
            row['Actual value']=client.read_holding_registers(row['Register'], REGISTER_COUNT).registers[0]
            print(row)
            df.at[index, 'Actual value'] = row['Actual value']
        else:
            pass
            
    client.close()
except:
    pass
    
# Save the DataFrame to a new CSV file
df.to_csv('C:\\Users\\...............\\Modbus_Nibe_S.csv', index=False)     
        
    
    
#    # result = client.read_input_registers(REGISTER_ADDRESS, REGISTER_COUNT)
#     #client.write_register(REGISTER_ADDRESS, 450)
#    # result2 = client.read_input_registers(REGISTER_ADDRESS, REGISTER_COUNT)

#     if not result.isError():
#         # Successfully read the register
#         print("Register values:", (result.registers,result2.registers))
#         # Process the data (conversion might be needed depending on the data format)
#     else:
#         # Handle error
#         print("Error reading register")
# finally:
    # Close the client connection



