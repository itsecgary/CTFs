import csv

def main():
    with open('test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line = 0
        output = ''
        for row in csv_reader:
            if line != 0:
                if row[0] == "Not set":
                    output += '0'
                else:
                    output += '1'
            line += 1
        print(output)
    csv_file.close()

if __name__ == "__main__":
    main()
