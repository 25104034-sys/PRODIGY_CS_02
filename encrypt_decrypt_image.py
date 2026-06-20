from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path="encrypted.png"):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)
    
    # XOR each pixel with the key
    encrypted_array = img_array ^ key
    
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_path)
    print(f"✅ Image encrypted and saved as '{output_path}'")


def decrypt_image(image_path, key, output_path="decrypted.png"):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img, dtype=np.uint8)
    
    # XOR again with same key to reverse
    decrypted_array = img_array ^ key
    
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_path)
    print(f"✅ Image decrypted and saved as '{output_path}'")


# ---------- MAIN ----------
print("🔐 Image Encryption Tool")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Choose (1/2): ")

path = input("Enter image path: ")
key = int(input("Enter key (0-255): "))

if choice == "1":
    encrypt_image(path, key)
elif choice == "2":
    decrypt_image(path, key)
else:
    print("Invalid choice!")
