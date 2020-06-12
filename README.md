Cisco Commissioning Tool 

This a python script that automatically collects a set of commands to validate configurations. 

Requirements

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/lvillatoroq/cisco_comission?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/netmiko?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/textfsm?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/xlsxwriter?style=for-the-badge)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/lvillatoroq/cisco_comission/openpyxl?style=for-the-badge)


Instructions 

1. Verify that python version installed is Python 2.7
2. Clone repository 
3. Create virtual enviroment 
4. Install dependencies

5. Modify the input/T-All.txt file with the IP address of the switches to be scanned.
6. Modify the input/config.txt file with the username and password of the switches to be scanned. 

7. Run the command python cisco_collect.py 

