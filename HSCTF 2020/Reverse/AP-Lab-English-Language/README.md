# AP Lab: English Language
**Category:** Reverse

**Points:** 100

**Description:**
> The AP English Language activity will ask you to reverse a program about
  manipulating strings and arrays. Again, an output will be given where you
  have to reconstruct an input.
>
> **Author:** AC
>
> **Given:** EnglishLanguage.java & a pdf

## Writeup
We can see right away that we have a .java file. I loaded up Eclipse and
opened the .java file there.

Here's what I found:
```
import java.util.Scanner;
public class EnglishLanguage
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.nextLine();
        if (inp.length()!=23) {
            System.out.println("Your input is incorrect.");
            System.exit(0);
        }
        for (int i = 0; i<3; i++) {
            inp=transpose(inp);
            inp=xor(inp);
        }
        if (inp.equals("1dd3|y_3tttb5g`q]^dhn3j")) {
            System.out.println("Correct. Your input is the flag.");
        }
        else {
            System.out.println("Your input is incorrect.");
        }
    }
    public static String transpose(String input) {
        int[] transpose = {11,18,15,19,8,17,5,2,12,6,21,0,22,7,13,14,4,16,20,1,3,10,9};
        String ret = "";
        for (int i: transpose) {
            ret+=input.charAt(i);
        }
        return ret;
    }
    public static String xor(String input) {
        int[] xor = {4,1,3,1,2,1,3,0,1,4,3,1,2,0,1,4,1,2,3,2,1,0,3};
        String ret = "";
        for (int i = 0; i<input.length(); i++) {
            ret+=(char)(input.charAt(i)^xor[i]) ;
        }
        return ret;
    }
}
```

Doesn't seem too bad. Looks like it runs the *transpose* function then the *xor*
after the first one three total times. I guess we gotta put it in reverse.

For the **xor**, we know that if we XOR each char again, it will reverse that
sequence.

For the **transpose**, it mixes the data up a little more. I took the index of
the value of the index of my new array. For example, my first index for my new
array is 0 and the index of 0 in the Java array was 11. For 1, the index was 19,
for 2 it was 7, and so on...

You can find my script in this repo or right here:
```
def transpose(data):
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
```

## Flag
flag{n0t_t00_b4d_r1ght}
