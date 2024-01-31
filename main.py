import csv
import Customer
import pandas as pd
import os
import warnings

def main():
    '''Export Excel data into seperate CSV files based on Excel sheets'''
    while True:
        excel_file_path = input('Enter Forge file path: ')
        if os.path.exists(excel_file_path):
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
            break
        else:
            print(f'No such file or directory: {excel_file_path}')

    '''Finds correct CSV file, collects data, and stores it in the Customer object'''
    directory_path = 'csv_files'
    files = os.listdir(directory_path)
    dataArr = []
    dataArr.clear()
    for file in files:
        if file == 'Input New Customer.csv':
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

    '''Clear csv_files directory'''
    csv_files_to_delete = os.listdir('csv_files')
    for file in csv_files_to_delete:
        file_path = os.path.join('csv_files', file)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Error deleting {file_path}: {e}')

if __name__ == '__main__':
    main()