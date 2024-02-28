Modbus for Nibe Heat Pumps
This Python script facilitates communication with Nibe heat pumps over Modbus TCP/IP. It allows for reading and writing of Modbus registers specific to Nibe heat pumps to monitor and control various parameters. stored in a CSV file which your headpump can creat for you!

Features
Connect to Nibe heat pumps using Modbus TCP/IP.
Read and write to both Modbus input and holding registers.
Log detailed debug output for troubleshooting.
Automatically reconnect and continue operations in case of intermittent connectivity issues.
Requirements
Python 3
pandas
pymodbus
Nibe S line heatpump or SMO S series, or modbus 40 extension

Installation
Ensure you have Python 3 installed on your system. Then, install the required packages using pip:

Copy code
pip install pandas pymodbus
Usage
Modify the location od CSV file and adjust the IP adres  to match your heat pump's IP address
enable in menu 7.5.9 (installer settings,tools,modbus TCP/IP)

Update the CSV file path in the script to your list of Modbus registers.
Run the script:
Copy code
python Modbus_Nibe_S.py
CSV Format
Your CSV file should contain the following columns:

Register: The Modbus register address.
Type register: Specify as either MODBUS_INPUT_REGISTER or MODBUS_HOLDING_REGISTER.
Actual value: This column will be updated with the read values.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to adjust the content to better match your project's specifics or any additional features you might have implemented.
