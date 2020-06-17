from pwn import *
import libnum
from Crypto.Util.number import *
import sys
from egcd import egcd
import binascii

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


c=16267540901004879123859424672087486188548628828063789528428674467464407443871599865993337555869530486241139138650641838377419734897801380883629894166353225288006148210453677023750688175192317241440457768788267270422857060534261674538755743244831152470995124962736526978165448560149498403762447372653982922113772190234143253450918953235222315161964539311032659628670417496174123483045439359846360048774164337257829398345686635091862306204455687347443958931441225500856408331795261329035072585605404416473987280037959184981453888701567175803979981461050532113072292714696752692872526424122826696681194705563391161137426703690900733706866842363055967856443765215723398555522126909749236759332964873221973970368877565410624895160438695006432021529071866881905134494489266801004903504121740435965696128048690741210812963902631391765192187570107372453917327060678806282122942318369245760773848604249664378721970318257356486696764545
q=338808278305491368568107597536870102903517054340801660200304926784154444523223906451699772927968482815828890482348342203845897909840260655384526983598744312581591533978845446602589686620835190303243711955190856932946979670202446096542521271004217036632261094082852110229243380763789393081471800046961479400329
p=462648222004918001013626929700851985161214529015962355517097297750332107059692278343607439888140451722661722449586909096508950271217838478793469222136256780856060573039970361424138955569021582604733404145398646735820327194382610835536537670219091779958808528053471059443883883244638910795974245528935198178697

log.info("Decrypting Schmidt-Samoa Ciphertext")

N=(p**2)*q

phi = lcm(p-1,q-1)
#phi = (p-1)*(q-1)
d = egcd(N, phi)[1]
if d < 0:
    d += phi
p = pow(c, d, p*q)
ph = (str(hex(p))).split('x')[1].split("L")[0]
flag = binascii.unhexlify(ph).decode("utf-8")
#flag = bytes(ph, encoding='hex').decode('ascii')

log.success("flag: {}".format(flag))
