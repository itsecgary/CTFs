# Ice Cream Bytes
**Category:** Reverse

**Points:** 100

**Description:**
> Introducing the new Ice Cream Bytes machine! Here’s a free trial:
  IceCreamBytes.java Oh, and make sure to read the user manual: IceCreamManual.txt
>
> **Author:** wooshi
>
> **Given:** IceCreamManual.txt & IceCreamBytes.java

## Writeup
We see right away that we have a Java program we can look at. I use Eclipse to
open up the program and this is what I find:
```
import java.io.*;
import java.nio.file.*;
import java.util.Scanner;

public class IceCreamBytes {
    public static void main(String[] args) throws IOException {
        Path path = Paths.get("IceCreamManual.txt");
        byte[] manualBytes = Files.readAllBytes(path);

        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter the password to the ice cream machine: ");
        String userInput = keyboard.next();
        String input = userInput.substring("flag{".length(), userInput.length()-1);
        byte[] loadedBytes = toppings(chocolateShuffle(vanillaShuffle(strawberryShuffle(input.getBytes()))));
        boolean correctPassword = true;

        byte[] correctBytes = fillMachine(manualBytes);
        for (int i = 0; i < correctBytes.length; i++) {
            if (loadedBytes[i] != correctBytes[i]) {
                correctPassword  = false;
            }
        }
        if (correctPassword) {
            System.out.println("That's right! Enjoy your ice cream!");
        } else {
            System.out.println("Uhhh that's not right.");
        }
        keyboard.close();
    }

    public static byte[] fillMachine(byte[] inputIceCream) {
        byte[] outputIceCream = new byte[34];
        int[] intGredients = {27, 120, 79, 80, 147,
            154, 97, 8, 13, 46, 31, 54, 15, 112, 3,
            464, 116, 58, 87, 120, 139, 75, 6, 182,
            9, 153, 53, 7, 42, 23, 24, 159, 41, 110};
        for (int i = 0; i < outputIceCream.length; i++) {
            outputIceCream[i] = inputIceCream[intGredients[i]];
        }
        return outputIceCream;
    }

    public static byte[] strawberryShuffle(byte[] inputIceCream) {
        byte[] outputIceCream = new byte[inputIceCream.length];
        for (int i = 0; i < outputIceCream.length; i++) {
            outputIceCream[i] = inputIceCream[inputIceCream.length - i - 1];
        }
        return outputIceCream;
    }

    public static byte[] vanillaShuffle(byte[] inputIceCream) {
        byte[] outputIceCream = new byte[inputIceCream.length];
        for (int i = 0; i < outputIceCream.length; i++) {
            if (i % 2 == 0) {
                outputIceCream[i] = (byte)(inputIceCream[i] + 1);
            } else {
                outputIceCream[i] = (byte)(inputIceCream[i] - 1);
            }
        }
        return outputIceCream;
    }

    public static byte[] chocolateShuffle(byte[] inputIceCream) {
        byte[] outputIceCream = new byte[inputIceCream.length];
        for (int i = 0; i < outputIceCream.length; i++) {
            if (i % 2 == 0) {
                if (i > 0) {
                    outputIceCream[i] = inputIceCream[i - 2];
                } else {
                    outputIceCream[i] = inputIceCream[inputIceCream.length - 2];
                }
            } else {
                if (i < outputIceCream.length - 2) {
                    outputIceCream[i] = inputIceCream[i + 2];
                } else {
                    outputIceCream[i] = inputIceCream[1];
                }
            }
        }
        return outputIceCream;
    }

    public static byte[] toppings(byte[] inputIceCream) {
        byte[] outputIceCream = new byte[inputIceCream.length];
        byte[] toppings = {8, 61, -8, -7, 58, 55,
            -8, 49, 20, 65, -7, 54, -8, 66, -9, 69,
            20, -9, -12, -4, 20, 5, 62, 3, -13, 66,
            8, 3, 56, 47, -5, 13, 1, -7,};
        for (int i = 0; i < outputIceCream.length; i++) {
            outputIceCream[i] = (byte)(inputIceCream[i] + toppings[i]);
        }
        return outputIceCream;

    }    
}
```

We can see above that we get our output text to be from the IceCreamManual.txt
file given to us. That output text has to equal our input text (the flag) ran
through the strawberryShuffle, vanillaShuffle, chocolateShuffle, and toppings
functions.

To reverse this, we will need to write functions to reverse each of these
functions. I wrote a script to help with that.

**My script:**
```
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
```

**My output:**
```
Correct Bytes: ['l', 'o', 'l', 'l', 'o', 'o', 'k', 'a', 't', 't', 'h', 'i', 's', 't', 'e', 'x', 't', 'i', 'g', 'o', 't', 'f', 'r', 'o', 'm', 't', 'h', 'e', 'm', 'a', 'n', 'u', 'a', 'l']
Before Toppings: ['d', '2', 't', 's', '5', '8', 's', '0', '`', '3', 'o', '3', '{', '2', 'n', '3', '`', 'r', 's', 's', '`', 'a', '4', 'l', 'z', '2', '`', 'b', '5', '2', 's', 'h', '`', 's']
Before Chocolate: ['t', 's', '5', '2', 's', 's', '`', '8', 'o', '0', '{', '3', 'n', '3', '`', '2', 's', '3', '`', 'r', '4', 's', 'z', 'a', '`', 'l', '5', '2', 's', 'b', '`', '2', 'd', 'h']
Before Vanilla: ['s', 't', '4', '3', 'r', 't', '_', '9', 'n', '1', 'z', '4', 'm', '4', '_', '3', 'r', '4', '_', 's', '3', 't', 'y', 'b', '_', 'm', '4', '3', 'r', 'c', '_', '3', 'c', 'i']
Before Strawberry: ['i', 'c', '3', '_', 'c', 'r', '3', '4', 'm', '_', 'b', 'y', 't', '3', 's', '_', '4', 'r', '3', '_', '4', 'm', '4', 'z', '1', 'n', '9', '_', 't', 'r', '3', '4', 't', 's']
Flag: flag{ic3_cr34m_byt3s_4r3_4m4z1n9_tr34ts}
```

## Flag
flag{ic3_cr34m_byt3s_4r3_4m4z1n9_tr34ts}
