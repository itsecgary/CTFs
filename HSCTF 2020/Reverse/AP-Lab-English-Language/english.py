

def transpose(data): 
    #trans = [11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9]
    trans = [11,19,7,20,16,6,9,13,4,22,21,0,8,14,15,2,17,5,1,3,18,10,12]
    trans_new = []
    
    for ind, val in enumerate(trans):
        trans_new.append(data[val])
    return ''.join(trans_new)

def xor(data): 
    xs = [4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3]
    new_data = []
    for i in range(len(data)):
        new_data.append(chr(ord(data[i]) ^ xs[i]))
    return ''.join(new_data)

if __name__ == '__main__':
    text = "1dd3|y_3tttb5g`q]^dhn3j"
    for i in range(3):
        text = xor(text)
        text = transpose(text)
    print("FLAG: {}".format(text))
