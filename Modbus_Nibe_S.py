import pandas as pd


from pymodbus.client import ModbusTcpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient # Use this for serial connection
import logging

# Enable logging for detailed debug output
logging.basicConfig()
log = logging.getLogger()
#CRITICAL ERROR WARNING INFO DEBUG NOTSET
log.setLevel(logging.INFO)

PATH_Load='C:\\Users\.....................Modbus_Nibe_S.csv'
PATH_Save='C:\\Users\\....................Modbus_Nibe_S2.csv'


# Modbus connection parameters
HOST = '192.168.0.145' # Example IP address, change to your device's IP
PORT = 502 # Default Modbus TCP port, change if different

# Example register address and count
REGISTER_COUNT = 1 # Number of registers to read

# Create a Modbus client
client = ModbusClient(HOST, PORT)

# Read Modbus list
df = pd.read_csv(PATH_Load)
#print(df)

# try:
# Connect to the client
client.connect()

# Read / write holding/input registers
#client.read_input_registers(REGISTER_ADDRESS, REGISTER_COUNT)
#client.write_register(REGISTER_ADDRESS, VALUE)
#client.read_holding_registers(REGISTER_ADDRESS, REGISTER_COUNT)

for index, row in df.iterrows(): 
    if index % 50 == 0:  # Check if the current index is divisible by 10
        print(index, " OUT OF ", len(df))
        
    #print(row)
    if row['Type register']=='MODBUS_INPUT_REGISTER':
        row['Actual value']=client.read_input_registers(int(row['Register']), REGISTER_COUNT).registers[0]
        # print (row)
        df.at[index, 'Actual value'] = row['Actual value']
    elif row['Type register']=='MODBUS_HOLDING_REGISTER':
        row['Actual value']=client.read_holding_registers(int(row['Register']), REGISTER_COUNT).registers[0]
        # print(row)
        df.at[index, 'Actual value'] = row['Actual value']
   
# Close the client connection
client.close()

    
# Save the DataFrame to a new CSV file
df.to_csv(PATH_Save, index=False)     
        
    
    
# finally:
    



