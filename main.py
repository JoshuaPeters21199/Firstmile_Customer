# import csv
import pandas as pd
# import Customer

def main():
    # export Excel data into seperate CSV files
    excel_file_path = 'Piccard Pet Supplies_FullFile_Xparcel_01-26-24.xlsm'
    xls = pd.ExcelFile(excel_file_path)
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(excel_file_path, sheet_name)
        csv_file_path = f'csv_files/{sheet_name}.csv'
        df.to_csv(csv_file_path, index=False)
        print(f'CSV file saved: {csv_file_path}')

    # dataArr = []
    # with open('csvFiles/ground.csv', newline='') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter=',')
    #     for row in spamreader:
    #         dataArr.append(row)

    #     customerName = dataArr[0][0].lstrip("ï»¿")

    #     customerObject = Customer.Customer(customerName)

    #     print(customerObject)

if __name__ == '__main__':
    main()