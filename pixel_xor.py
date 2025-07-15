from PIL import Image

def xor_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    for i in range(img.size[0]):  
        for j in range(img.size[1]):  
            r, g, b = pixels[i, j]

           
            r ^= key
            g ^= key
            b ^= key

            
            pixels[i, j] = (r, g, b)


    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    print("🖼️ Image Encryption Tool (XOR Encryption)")
    print("1. Encrypt an Image")
    print("2. Decrypt an Image")
    choice = int(input("Enter your choice (1 or 2): "))

    input_path = input("Enter the input image path: ")
    output_path = input("Enter the output image path: ")
    key = int(input("Enter encryption/decryption key (integer 0-255): "))

   
    if key < 0 or key > 255:
        print("❌ Key must be between 0 and 255")
    else:
        xor_image(input_path, output_path, key)
