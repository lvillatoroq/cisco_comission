# Cisco Commissioning Tool 

This a python script that automatically collects a set of commands to validate configurations. 

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

1. Modify the input/T-All.txt file with the IP address of the switches to be scanned.
2. Modify the input/config.txt file with the username and password of the switches to be scanned. 
3. Run the command python cisco_collect.py 

