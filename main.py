#import fungsi enkripsi
import enrkipsi

#menjalankan enrkipsi
# plain_text = input("Masukkan teks yang akan dienkripsi: ")
# encrypted_text = enkripsi.encrypt(plain_text)
# print("Teks terenkripsi: ", encrypted_text)

#menjalankan dekripsi
encrypted_text = input("Masukkan teks terenkripsi: ")
decrypted_text = enrkipsi.decrypt(encrypted_text)
print("Teks terdekripsi: ", decrypted_text)
