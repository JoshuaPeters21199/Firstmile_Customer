import csv
import Customer

def main():
    with open('Book1.csv', newline='') as csvfile:
        arr = []
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            arr.append(row)

        # print(arr[0][0])
        customerName = arr[0][0].lstrip("ï»¿")
        print(customerName)

        customerObject = Customer.Customer('test')

if __name__ == '__main__':
    main()