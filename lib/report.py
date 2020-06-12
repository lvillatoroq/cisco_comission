#!/usr/bin/python

import os, sys, re
import datetime
import xlsxwriter

##### REPORT MODULE ############

class Report():

    def __init__(self,report_name):
        """
        Creates a report object
        :param report_name - used for heading and xls file name
        :return: nothing
        """
        
        # color scheme for coloring the cells in the xls
        self.green = '#99CC44'
        self.red = '#FF0000'
        self.yellow ='#FFFF00'
        self.grey = '#DDDDDD'
        self.white = '#FFFFFF'

        self.report_name = report_name
        self.sheet_name = 'Switch General Task'
        self.categories = ['None']
        
        self.report={}
        self.color={}

    def add_to_report(self, test_name, device, result, color):
        """
        Add the result of one test for one device to the report object
        :param test_name - name of test - used for rows in the xls        
        :param device - name of device - used for columns in the xls
        :param result - result to store for this test for this device
        :param color - color to store for this test for this device, indicates if test was successful or not
        :param category - category to which this should be written - e.g. U18
        :return: nothing
        """

        if not test_name in self.report:
            self.report[test_name] = {}
        if not test_name in self.color:
            self.color[test_name] = {}
        if not device in self.report[test_name]:
            self.report[test_name][device] = result
        else:
            self.report[test_name][device] += result
        self.color[test_name][device] = color

    def write_xls(self, test_names, test_report_names, hostnames, categories):
        """
        Prints information for each command for each device.
        Set the color for each cell.
        :param test_names - list of tests, to keep the order when reporting
        :param test_report_names - dictionary: key = test, value = output to xls for this test
        :param device_list - list of actual devices to write report for
        :param hostnames - dict - key:device, value:hostname
        :     all parameters must match with what is added to the report
        :return: nothing
        """
        workbook = xlsxwriter.Workbook("%s_%s.xlsx"%(self.report_name, datetime.datetime.now().strftime("%Y%m%d")))

        text_format = {'heading':workbook.add_format({'text_wrap': False, 'valign':'top',
                                                      'bold': True, 'font_size': 14}),
                       'white_no_border':workbook.add_format({'text_wrap': True, 'valign':'top'}),
                       'white':workbook.add_format({'text_wrap': True, 'valign':'top','border': 1}),
                       'grey_heading':workbook.add_format({'bg_color':self.grey, 'text_wrap': True, 'valign':'top',
                                                           'left': 1, 'right': 1, 'top': 2, 'bottom': 2}),
                       'grey_bold_heading':workbook.add_format({'bg_color':self.grey, 'text_wrap': True, 'valign':'top',
                                                                'bold': True, 'left': 1, 'right': 1, 'top': 2, 'bottom': 2}),
                       'grey_bold':workbook.add_format({'bg_color':self.grey, 'text_wrap': True, 'valign':'top',
                                                   'bold': True, 'border': 1}),
                       'red':workbook.add_format({'bg_color':self.red, 'text_wrap': True, 'valign':'top', 'border': 1}),
                       'yellow':workbook.add_format({'bg_color':self.yellow, 'text_wrap': True, 'valign':'top', 'border': 1}),
                       'green':workbook.add_format({'bg_color':self.green, 'text_wrap': True, 'valign':'top', 'border': 1})} 

        for key, value in categories.items():
            if key is 'Default':
                worksheet = workbook.add_worksheet(self.sheet_name)
            else:
                worksheet = workbook.add_worksheet(key)
            device_list = value
            # set column widths
            worksheet.set_column(0, 0, 16)
            for i in range(1, 50):
                worksheet.set_column(i, i, 13)

            worksheet.write('A1:E1', self.report_name+" switches", text_format['heading'])
            worksheet.write('A3', "Legend:", text_format['white_no_border'])
            worksheet.merge_range('B3:H3', "Requirement in the project, Green is OK. No change needed.", text_format['green'])
            worksheet.merge_range('B4:H4', "Requirement in project. Red is NOT OK. Change needed.", text_format['red'])
            worksheet.merge_range('B5:H5', "Manual analysis. Verifying network setup as documented. Possible change needed.",
                                  text_format['yellow'])
            worksheet.merge_range('B6:H6', "Added for documentation purposes only. For operations. Can be ignored by supplier",
                                  text_format['white'])

            row = 7
            col = 0
            worksheet.write(row, col, "Device Hostname", text_format['grey_bold_heading'])
            for ip_address in device_list:
                col += 1
                worksheet.write(row, col, hostnames[ip_address], text_format['grey_heading'])

            row += 1
            col = 0
            worksheet.write(row, col, "Device IP-address", text_format['grey_bold_heading'])
            for ip_address in device_list:
                col += 1
                worksheet.write(row, col, ip_address, text_format['grey_heading'])


            for report_item in test_names[key]:
                row += 1
                col = 0
                worksheet.write(row, col,
                                test_report_names[key][report_item],
                                text_format['grey_bold'])
                for ip_address in device_list:
                    col += 1
                    if ip_address in self.report[report_item]:
                        worksheet.write(row, col,
                                        self.report[report_item][ip_address],
                                        text_format[self.color[report_item][ip_address]])
                    else:
                        worksheet.write(row, col,
                                        'Missing device',
                                        text_format['red'])
            worksheet.hide_gridlines(option=1)
        workbook.close()
