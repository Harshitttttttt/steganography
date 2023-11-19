import cv2
import os
import secrets

img = cv2.imread("C:/Files/OCDSE/ibm/237-200x300.jpg") # Replace with the correct image path

# Define the encryption and decryption functions
def encrypt(message, key):
    encrypted = ""
    for char in message:
        num = ord(char) # convert character to number
        num += key # add the shift value
        if num > 255:
            num -= 256
        encrypted += chr(num) # convert number back to character
    return encrypted

def decrypt(message, key):
    decrypted = ""
    for char in message:
        num = ord(char) # convert character to number
        num -= key # subtract the shift value
        if num < 0:
            num += 256
        decrypted += chr(num) # convert number back to character
    return decrypted

# Ask the user to enter the message, the key, and the passcode
msg = input("Enter secret message:")
key = secrets.randbelow(25) + 1
password = input("Enter a passcode:")

# Encrypt the message using the Caesar cipher
msg = encrypt(msg, key)

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

# Embed the encrypted message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

# Ask the user to enter the passcode for decryption
pas = input("Enter passcode for Decryption:")
if password == pas:
    # Extract the encrypted message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    # Decrypt the message using the Caesar cipher
    message = decrypt(message, key)
    print("Decrypted message:", message)
    print("Key:", key)
else:
    print("YOU ARE NOT AUTHORIZED")
