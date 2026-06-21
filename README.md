PRODIGY_CS_02
Encryption and Decryption of image

Description
A Python program that encrypts and decrypts images using a secret key.
The program changes the RGB values of each pixel using the XOR operation. Using the same key again restores the original image.
Features
Select an image (JPG, PNG, BMP)
Encrypt image using a secret key
Decrypt image using the same key
Save the output image
Simple GUI using Tkinter
How It Works
Every image is made of pixels.
Each pixel has Red, Green, and Blue (RGB) values.
The program applies XOR (^) between each RGB value and the secret key.
Applying the same key again decrypts the image.
Code Explanation
Image.open() opens the image.
img.load() accesses pixel values.
r ^ key, g ^ key, b ^ key encrypt the RGB values.
Using the same key again decrypts the image.
filedialog.asksaveasfilename() saves the output image.
Technologies Used
Python 3
Tkinter
Pillow
How to Run
Bash
py -m pip install Pillow
Open Image_Encryption.py
Run the program
Select an image
Enter a key
Encrypt or decrypt the image
Save the result
Example
Original Pixel: (100, 150, 200)
Key: 66
Encrypted Pixel: (38, 212, 138)
Using key 66 again:
Decrypted Pixel: (100, 150, 200)
