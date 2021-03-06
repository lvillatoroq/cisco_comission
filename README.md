# Commissioning Tool 

This a python script that automatically collects a set of commands to validate configurations. All cisco platforms supported. Hirschmann support is limited to RSP devices. 

## Requirements

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/lvillatoroq/cisco_comission?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/netmiko?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/textfsm?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/xlsxwriter?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/openpyxl?style=for-the-badge)


## Instructions 

### Installing the packages

1. Verify that python version installed is Python 2.7
2. Clone repository: git clone https://github.com/lvillatoroq/cisco_comission.git
3. Create virtual enviroment: virtualenv cisco_comission
4. Install dependencies: pip install -r requirements.txt

### Running the Script

Before running the script the following files need to be modified with the requested information:

* T-All.txt >> File that contains the ip address of the devices
* config.txt >> File that contains the credentials for the devices
* commands.xlsx >> excel sheet with the commands to be run on the devices **( For ping commands be sure to change the IP address to the proper destination address you want to test) (RSP sheet contains commands for Hirschmann devices and Cisco sheet contains commands for Cisco Devices)**

1. Modify the input/T-All.txt file with the IP address of the switches to be scanned.
2. Modify the input/config.txt file with the username and password of the switches to be scanned. 
3a. Run the command python cisco_collect.py if you are collecting Cisco Devices
3b. Run the command python rsp_collect.py if you are collecting Hirschmann RSP Devices. 

