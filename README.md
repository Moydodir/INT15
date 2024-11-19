# Project Overview

This project is a script that processes network device(Mikrotik RouterOS v6) configuration data from a text file and generates an XML file containing the parsed interface settings. The project includes several Python modules and utility functions to extract relevant information from the configuration data, model it using a SettingModel, and then write the results to an XML file.

<pre>
.
├── main.py                # Main script to parse configuration file and write XML output
├── model.py               # Defines SettingModel class for representing network interface settings
├── xml_writer.py          # Contains function to write settings data to an XML file
├── tests/                 # Test directory containing unit tests
│   ├── test_config_parser.py  # Tests for the config_parser function
│   ├── test_integration.py   # Tests for the integration of modules
│   ├── test_param_finder.py  # Tests for the param_finder function
│   ├── test_setting_model.py # Tests for the SettingModel class
│   ├── test_write_to_xml_file.py # Tests for writing to XML
│   ├── test_network_device_output.txt  # Sample text №1
│   └── int_test.txt       # Sample text №1
└── README.md              # Project documentation
</pre>

## How It Works
### main.py
This is the main entry point for the project. It does the following:

Accepts a file path as a command-line argument (sys.argv).
Reads the file and splits its content into blocks using a regular expression.
For each block, it calls the param_finder function to extract relevant network interface parameters (Id, Name, Description, MacAddress, and Status).
Creates instances of the SettingModel class for each interface.
Finally, it calls the write_to_xml_file function to generate an XML file containing all the interface settings.

### model.py
Contains the SettingModel class, which represents the configuration of a network device interface. The model includes the following attributes:

Id (str): The identifier of the interface.
Name (str): The name of the interface.
Description (str): The description of the interface (if available).
MacAddress (str): The MAC address of the interface.
Status (str): The status of the interface, either "up" or "down".
The SettingModel class also has a serialization method that converts an object instance into an XML element tree.

### xml_writer.py
This file contains a function write_to_xml_file that generates an XML file from a list of SettingModel objects. The XML file is written with a root element <device>, and each interface's data is encapsulated in <interface> elements. Each attribute of the SettingModel is written as a child element of <interface>.

### tests/
This directory contains several unit tests to ensure that the functions in main.py, model.py, and xml_writer.py work correctly.

Test Files: The tests use unittest framework to verify different parts of the code.
Test Data: There are test files that simulate device configurations and edge cases (e.g., empty files or files with missing data).

## Usage
To run the script and generate the XML file, execute the following command:
```python main.py <path_to_config_file>```

⚠️ File MUST look like a configuration of mikrotik interfaces (RouterOS v6)
