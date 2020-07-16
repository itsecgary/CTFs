# PI 1: Magic in the air
**Category:** Forensics/OSINT

**Points:** 470

**Description:**
> We are investigating an individual we believe is connected to a group smuggling
drugs into the country and selling them on social media. You have been posted on
a stake out in the apartment above theirs and with the help of space-age
eavesdropping technology have managed to extract some data from their computer.
What is the phone number of the suspect's criminal contact?
>
> flag format includes country code so it should be in the format: rgbCTF{+00000000000}
>
> ~Klanec#3100
>
> **Given:** magic_in_the_air.7z

## Writeup
Unzipping the file gives us "data" which seems to be a bunch of gunk when looking
at the contents. Here's what kind of file it is:
```
$ file data
data: BTSnoop version 1,
```

I did not know what a BTSnoop file was and what it meant before completing this
challenge, so I learned A LOT from this challenge. I eventually figured out that
BTSnoop is Bluetooth traffic from a device. We can open this bad boy in **Wireshark**.

For a long time I couldn't quite figure out what kind of information we are provided
in this BTSnoop capture. After taking a close look at some of the sources, we see
a device name **G613**. I looked up the device on Google and we see that this data
is from a *Logitech Mechanical Gaming Keyboard*. This must be keystrokes then.

After quite a long time, I came across a PDF for Human Interface Devices (HIDs).
The bottom of the PDF contains the HID values for common keystrokes. **BINGO**
https://cdn.sparkfun.com/datasheets/Wireless/Bluetooth/RN-HID-User-Guide-v1.0r.pdf

I started to manually convert the values straight from the BTSnoop capture in
**Wireshark**, but I realized how many I had to convert and how long it would take
me. Therefore, I highlighted the packets I wanted to convert, exported them as a CSV
file, edited the CSV to be easier to work with in a script, and ran it through my
script to decode.

**Script:**
```
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
```

**Output:**
```
$ python parse_csv.py
['1c', '12', '12', '2c', '10', '4', '11', '28', '16', '12', '15', '15', '15', '1c', '2c', '9', '12', '15', '2c', '17', '0b', '0b', '8', '2c', '7', '8', '0f', '4', '1c', '2c', '2c', '0f', '12', '0f', '28', '28', '17', '15', '1c', '0c', '0c', '11', '11', '0a', '2c', '17', '12', '2c', '0a', '8', '81', '17', '2c', '2c', '17', '1c', '0c', '2a', '2a', '2a', '17', '0b', '0b', '0c', '16', '2c', '2c', '8', '1c', '5', '51', '12', '4', '15', '7', '2c', '1a', '12', '15', '0c', '0c', '11', '11', '11', '11', '11', '28', '28', '1c', '8', '8', '08', '04', '4', '2c', '2c', '0c', '17', '16', '2c', '2c', '11', '11', '8', '08', '1a', '37', '2c', '20', '1a', '0c', '15', '8', '0f', '8', '16', '16', '2c', '10', '4', '11', '0a', '2a', '37', '2c', '28', '28', '5', '8', '8', '81', '11', '2c', '10', '10', '12', '19', '19', '0c', '0c', '11', '11', '0a', '2c', '2c', '13', '13', '15', '12', '7', '18', '6', '17', '28', '28', '16', '16', '13', '8', '4', '4', '0c', '0c', '11', '11', '11', '11', '2c', '2c', '12', '9', '2c', '1c', '12', '12', '18', '2c', '11', '11', '8', '8', '7', '8', '7', '2c', '17', '12', '12', '2c', '6', '61', '12', '12', '11', '11', '17', '4', '4', '6', '17', '2c', '2c', '10', '10', '1c', '2c', '2c', '5', '12', '1c', '2c', '15', '0c', '0a', '0b', '17', '20', '20', '20', '28', '28', '1c', '8', '28', '28', '16', '0b', '12', '12', '18', '0f', '7', '07', '2c', '2c', '5', '5', '8', '2c', '9', '09', '0c', '0c', '11', '8', '2c', '0d', '18', '16', '17', '2c', '16', '16', '4', '04', '1c', '2c', '20', '20', '20', '12', '0b', '11', '11', '1c', '2c', '20', '20', '20', '2c', '16', '8', '11', '17', '2c', '1c', '12', '12', '18', '28', '28', '4', '0f', '15', '0c', '0a', '0b', '0b', '17', '2c', '0f', '8', '10', '10', '8', '2c', '0a', '8', '81', '17', '2c', '1c', '12', '12', '18', '18', '2c', '2c', '17', '0b', '8', '08', '2c', '2c', '11', '18', '10', '5', '8', '81', '15', '28', '28', '0b', '0b', '12', '0f', '7', '2c', '18', '18', '13', '2c', '20', '20', '20', '34', '34', '10', '10', '2c', '2c', '0f', '12', '12', '12', '0c', '0c', '11', '0a', '0a', '2c', '9', '12', '15', '15', '2c', '2c', '0c', '17', '28', '28', '28', '0c', '17', '16', '16', '2c', '2c', '0b', '0b', '0c', '16', '16', '2c', '2c', '5', '51', '18', '15', '11', '8', '15', '36', '36', '2c', '0a', '12', '17', '17', '2c', '2c', '0c', '0c', '17', '2c', '1a', '1a', '15', '0c', '17', '17', '17', '8', '11', '11', '2c', '7', '12', '1a', '11', '11', '2c', '16', '16', '12', '12', '10', '10', '8', '1a', '0b', '8', '15', '8', '28', '28', '28', '1c', '8', '8', '4', '0b', '0b', '2c', '0a', '12', '17', '2c', '0c', '17', '28', '28', '27', '27', '24', '20', '23', '24', '1f', '24', '25', '22', '26', '28', '28', '10', '0c', '0c', '11', '7', '2c', '0c', '17', '2c', '2c', '0c', '16', '2c', '4', '04', '2c', '16', '16', '1a', '1a', '1a', '8', '7', '0c', '16', '0b', '0b', '2c', '11', '11', '18', '10', '5', '8', '81', '15', '37', '2c', '0b', '8', '2c', '0a', '0a', '12', '17', '2c', '2c', '0c', '17', '2c', '2c', '12', '12', '11', '11', '2c', '0b', '0b', '12', '0f', '0f', '0c', '7', '4', '04', '1c', '2c', '17', '0b', '8', '81', '15', '8', '2c', '9', '9', '8', '1a', '1a', '2c', '2c', '10', '10', '12', '12', '11', '17', '0b', '0b', '16', '2c', '2c', '5', '5', '4', '6', '6', '28', '28', '1c', '8', '4', '0b', '0b', '2c', '1c', '12', '12', '18', '18', '2c', '6', '4', '11', '2c', '5', '18', '18', '1c', '2c', '2c', '5', '51', '18', '15', '11', '11', '8', '81', '15', '16', '2c', '16', '16', '18', '18', '13', '13', '8', '15', '2c', '8', '4', '41', '16', '0c', '0c', '0f', '1c', '2c', '17', '0b', '8', '81', '15', '8', '28', '28', '4', '04', '0f', '15', '0c', '0a', '0b', '0b', '17', '2c', '20', '0a', '28', '28', '1c', '8', '8', '4', '04', '0b', '2c', '2c', '0c', '17', '16', '2c', '20', '20', '7', '12', '11', '11', '1c', '2c', '0f', '28', '28', '15', '15', '8', '10', '8', '10', '5', '8', '81', '15', '2c', '17', '12', '2c', '17', '8', '0f', '0f', '2c', '0b', '0c', '0c', '10', '10', '2c', '0c', '2c', '16', '8', '11', '17', '2c', '1c', '12', '12', '18', '28', '28', '13', '8', '8', '4', '6', '8', '28', '28', '10', '1b', '10']
yoo man
sorrry for thhe delay  lol

tryiinng to ge_t  thhis  eybboard woriinnnnn

yeeeaa  its  nneew. 3wireless man.

bee_n mmovviinng  pproduct

sspeaaiinnnn  of yoou nneeded too c_oonntaact  mmy  boy right333

ye

shoould_  bbe f_iine just ssaay 333ohnny 333 sent yoou

alrighht lemme ge_t yoouu  thee  numbe_r

hhold uup 333__mm  loooiingg forr  it


itss  hhiss  bburner__ gott  iit wwritttenn downn ssoommewhere


yeeahh got it

__736727859

miind it  is aa sswwwedishh nnumbe_r. he ggot  it  oonn hhollidaay the_re ffeww  mmoonthhs  bbacc

yeahh yoouu can buuy  bburnne_rs ssuupper ea_siily the_re

aalrighht 3g

yeeaah  its 33donny l

rremembe_r to tell hiimm i sent yoou

peeace

mxm
```

Sooooooo the output was the best I really *wanted* to get it, but it got me the
phone number, which is what we wanted all along. From the challenge description,
we see that we put the flag in the format **rgbCTF{+00000000000}**. I tried to put
the number in, but it failed. I soon realized that I need the country area code
before the actual number. This is a Swedish area code (seen in the output) - **+46**.
This should give us the final flag!

## Flag
rgbCTF{+46736727859}

## Resources
[Wireshark](https://www.wireshark.org/download.html)

[HID PDF](https://cdn.sparkfun.com/datasheets/Wireless/Bluetooth/RN-HID-User-Guide-v1.0r.pdf)

[Generic ATT Info](https://www.oreilly.com/library/view/getting-started-with/9781491900550/ch04.html)
