def encrypt(input_string):
    # Layer 1: ASCII Decimal * 7
    layer1 = [ord(c) * 7 for c in input_string]
    layer1_string = ' '.join(str(num) for num in layer1)
    print("Layer 1:", layer1_string)
    
    # Layer 2: Layer 1 - 69
    layer2 = [num - 69 for num in layer1]
    layer2_string = ' '.join(str(num) for num in layer2)
    print("Layer 2:", layer2_string)
    
    # Layer 3: Layer 2 * 69
    layer3 = [num * 69 for num in layer2]
    layer3_string = ' '.join(str(num) for num in layer3)
    print("Layer 3:", layer3_string)
    
    # Layer 4: Layer 3 * 11
    layer4 = [num * 11 for num in layer3]
    layer4_string = ' '.join(str(num) for num in layer4)
    print("Layer 4:", layer4_string)
    
    # Mengembalikan hasil enkripsi sebagai string
    encrypted_string = ' '.join(str(num) for num in layer4)

    return encrypted_string

def decrypt(encrypted_string):
    # Mengubah string terenkripsi menjadi daftar angka
    encrypted_list = [int(num) for num in encrypted_string.split()]
    encrypted_list_string = ' '.join(str(num) for num in encrypted_list)
    print("Layer 4:", encrypted_list_string)

    # Layer 4: Layer 3 * 11
    layer3 = [num // 11 for num in encrypted_list]
    layer3_string = ' '.join(str(num) for num in layer3)
    print("Layer 3:", layer3_string)

    # Layer 3: Layer 2 / 69
    layer2 = [num // 69 for num in layer3]
    layer2_string = ' '.join(str(num) for num in layer2)
    print("Layer 2:", layer2_string)

    # Layer 2: Layer 1 + 69
    layer1 = [num + 69 for num in layer2]
    layer1_string = ' '.join(str(num) for num in layer1)
    print("Layer 1:", layer1_string)

    # Layer 1: ASCII Decimal / 7
    decrypted_list = [num // 7 for num in layer1]
    
    # Mengubah daftar angka menjadi string dekripsi
    decrypted_string = ''.join(chr(num) for num in decrypted_list)
    return decrypted_string

