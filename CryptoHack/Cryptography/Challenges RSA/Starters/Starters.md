# Starters

I found most of the levels except for the last one i.e. RSA signature t be easy and straightforward, hence I am just going to put their codes here.

## Modular Exponentiation

``` python
val = pow(101,17,22663)

print(val)

```
## Public Keys

``` python

encrypted = pow(12,65537, 17*23)

print(encrypted)

```

## Euler's totient

``` python

totient = 857504083339712752489993810776*1029224947942998075080348647218
print(totient)

```

## Private Keys

``` python

totient = 857504083339712752489993810776*1029224947942998075080348647218
e=65537
d = pow(e,-1,N)
print("Private Key", d)

```

## RSA Decryption

``` python


N = 882564595536224140639625987659416029426239230804614613279163 #p*q
totient = 882564595536224140639625987657529300394956519977044270821168 # From previous levels
e = 65537
d = pow(e,-1,totient)
c = 77578995801157823671636298847186723593814843845525223303932
m = pow(c,d,N)
print(m)

```

## RSA Signature

OK so this level was the one that I found to be slightly challenging.

First to Import the Crypto.Util.Number library, I had to install pycryptodome :
`pip install pycryptodome`

Now let's take a look at the code 

``` python
import Crypto.Util.number as crypto
import hashlib

N = 15216583654836731327639981224133918855895948374072384050848479908982286890731769486609085918857664046075375253168955058743185664390273058074450390236774324903305663479046566232967297765731625328029814055635316002591227570271271445226094919864475407884459980489638001092788574811554149774028950310695112688723853763743238753349782508121985338746755237819373178699343135091783992299561827389745132880022259873387524273298850340648779897909381979714026837172003953221052431217940632552930880000919436507245150726543040714721553361063311954285289857582079880295199632757829525723874753306371990452491305564061051059885803
d = 11175901210643014262548222473449533091378848269490518850474399681690547281665059317155831692300453197335735728459259392366823302405685389586883670043744683993709123180805154631088513521456979317628012721881537154107239389466063136007337120599915456659758559300673444689263854921332185562706707573660658164991098457874495054854491474065039621922972671588299315846306069845169959451250821044417886630346229021305410340100401530146135418806544340908355106582089082980533651095594192031411679866134256418292249592135441145384466261279428795408721990564658703903787956958168449841491667690491585550160457893350536334242689

flag = b"crypto{Immut4ble_m3ssag1ng}"

h = hashlib.sha256()
h.update(flag)
hashed_flag = h.digest()

hashed_val = crypto.bytes_to_long(hashed_flag)

m = pow(hashed_val,d,N)

print(m)

```

So first we're importing Crypto.Util.Number and hashlib libraries.

The hashlib module contains files and algorithms which provide efficient hashing.

We are already given the flag "crypto{Immut4ble_m3ssag1ng}" and we convert it into byte format by prefixing a "b" before it.

We are using SHA256 to hash the flag.

`h.hashlib.sha256()` - This creates an object `h` which can implement SHA256 hashing

`h.update(flag)` - This line takes the "Flag" and converts it using the SHA256 hashing scheme

`h.digest()` - This line provides the resulting hash as raw bytes.

However to decrypt the message, we need it in terms of an integer or long format.

Hence, we convert it into a long number using this : `hashed_val = crypto.bytes_to_long(hashed_flag)`

Then, we finally retrieve the message using the RSA decyption scheme we used in the previous level.

``` python
m = pow(hashed_val,d,N)

print(m)
```

## My learning

Through the Starters coursepath, I learn about the working of 
- Euler's totient
- Public and Private Key cryptography
- RSA decryption
- Hashing algorithms like SHA256
- How to combine hashing and RSA to create a very secure encryption
- The difference between hashing and encryption

#### Some Important Formulas

phi(totient) = (p-1)*(q-1)
private key(d) = e^-1 mod N
RSA Encryption -  c = m^e mod N
RSA Decryption - m = c^d mod N

