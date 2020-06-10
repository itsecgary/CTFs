import sys
import binascii

def getCorrect():
    ingredients = [27,120,79,80,147,154,97,8,13,46,31,54,15,112,3,464,116,
                   58,87,120,139,75,6,182,9,153,53,7,42,23,24,159,41,110]
    with open("IceCreamManual.txt", "r") as f:
        data = f.read()
        arr = [c for c in data]
        output_icecream = []
        for val in ingredients:
            output_icecream.append(ord(arr[val]))
        output = [chr(x) for x in output_icecream]
        print("Correct Bytes: {}".format(output))
    f.close()
    return output_icecream

def toppings(data):
    toppings = [8,61,-8,-7,58,55,-8,49,20,65,-7,54,-8,66,-9,69,
               20,-9,-12,-4,20,5,62,3,-13,66,8,3,56,47,-5,13,1,-7,]
    output_icecream = []
    for i in range(len(data)):
        output_icecream.append(data[i] - toppings[i])
    output = [chr(x) for x in output_icecream]
    print("Before Toppings: {}".format(output))
    return output_icecream

def chocolate(data):
    output_icecream = []
    for i in range(len(data)):
        val = 0
        if i % 2 == 0:
            if i < (len(data) - 2):
                val = data[i+2]
            else:
                val = data[0]
        else:
            if i > 1:
                val = data[i-2]
            else:
                val = data[len(data) - 1]
        output_icecream.append(val)
    output = [chr(x) for x in output_icecream]
    print("Before Chocolate: {}".format(output))
    return output_icecream

def vanilla(data):
    output_icecream = []
    for i in range(len(data)):
        if i % 2 == 0:
            output_icecream.append(data[i] - 1)
        else:
            output_icecream.append(data[i] + 1)

    output = [chr(x) for x in output_icecream]
    print("Before Vanilla: {}".format(output))
    return output_icecream

def strawberry(data):
    output_icecream = data[::-1]
    output = [chr(x) for x in output_icecream]
    print("Before Strawberry: {}".format(output))
    return output_icecream

if __name__ == '__main__':
    input1 = getCorrect()
    input2 = toppings(input1)
    input3 = chocolate(input2)
    input4 = vanilla(input3)
    output = strawberry(input4)
    output = ''.join([chr(x) for x in output])
    print("Flag: flag{" + "{}".format(output) + "}")



