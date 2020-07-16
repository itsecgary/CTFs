import csv
   
db = {'a': '4', 'b': '5', 'c': '6', 'd': '7', 'e': '8', 'f': '9', 'g': '0a', 'h': '0b', 'i': '0c', 'j': '0d', 'k': '0e', 'l': '0f', 'm': '10', 'n': '11', 'o': '12', 'p': '13', 'q': '14', 'r': '15', 's': '16', 't': '17', 'u': '18', 'v': '19', 'w': '1a', 'x': '1b', 'y': '1c', 'z': '1d', '0': '1d', '1': '1e', '2': '1f', '3': '20', '4': '21', '5': '22', '6': '23', '7': '24', '8': '25', '9': '26', '.': '37', ' ': '2c', '\n': '28', '+': '2E'}

# function to return key for any value 
def get_key(val): 
    for key, value in db.items(): 
        #print("Val: {}\nDB_Val: {}".format(val, value))
        if val == value: 
            return key 
        
    return "_"


with open('conversation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line = 0
    output = ''
   
    arr = []
    for row in csv_reader:
        if line != 0:
            val = row[0]
            if 'E+11' in val:
                val = str(int(float(val.split('E')[0][:3])*10))
            elif 'E+12' in val:
                val = val.split('E')[0] + '0'
            
            if val == '0.00':
                val = val
            elif val[0] == '0':
                val = val[2:4]
            else:
                val = val[0:2]
           
            if val == "40" or val == "50" or val == "60" or val == "70" or val == "80" or val == "90":
                val = val[0]
            if val != '0.00' and val != '0.00E+00':
                arr.append(val)
        line += 1
    
    print(arr)

    convo = ''
    for val in arr:
        if val == '2a':
            convo = convo[:-1]
        elif val == '04':
            convo += 'a'
        elif val == '08':
            convo += 'e'
        elif val == '51':
            convo += 'b'
        else:
            convo += get_key(val)
    print(convo)


