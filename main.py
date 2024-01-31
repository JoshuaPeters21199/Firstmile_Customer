import csv
import Customer
import pandas as pd
import os
import warnings

def main():

    '''Export Excel data into seperate CSV files based on Excel sheets'''
    excel_file_path = 'Piccard Pet Supplies_FullFile_Xparcel_01-26-24.xlsm'
    xls = pd.ExcelFile(excel_file_path)
    warnings.simplefilter(action='ignore', category=UserWarning) # prevents UserWarnings from being output to terminal
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_file_path, sheet_name)
        csv_file_path = f'csv_files/{sheet_name}.csv'
        if os.path.exists(csv_file_path):
            pass
            # print("File already exists")
        else:
            df.to_csv(csv_file_path, index=False)
            # print(f'CSV file saved: {csv_file_path}')

    '''Finds correct CSV file, collects data, and stores it in the Customer object'''
    directory_path = 'csv_files'
    files = os.listdir(directory_path)
    for file in files:
        if file == 'Input New Customer.csv':
            dataArr = []
            with open('csv_files/Input New Customer.csv', newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    dataArr.append(row)

                customerName = dataArr[1][1]
                customerTerminal = dataArr[4][1]
                customerState = dataArr[5][1]
                customerZip = dataArr[6][1]
                customerAgent = dataArr[7][1]

                customerObject = Customer.Customer(
                    customerName,
                    customerTerminal,
                    customerState,
                    customerZip,
                    customerAgent
                )

                print(customerObject)

if __name__ == '__main__':
    main()