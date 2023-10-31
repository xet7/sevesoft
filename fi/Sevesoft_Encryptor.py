import random
import string
from tkinter import *

def Encrypt():
    plain_text = text_edit.get("1.0", "end-1c")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("1.0", cipher_text)
    result_text.config(state="disabled")

def Decrypt():
    cipher_text = text_edit.get("1.0", "end-1c")
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    result_text.config(state="normal")
    result_text.delete("1.0", "end")
    result_text.insert("1.0", plain_text)
    result_text.config(state="disabled")

window = Tk()
window.resizable(False, False)
window.title("Sevesoft Encryptor")
window.geometry("500x500")

font_tuple = ("consolas", 15)

text_edit = Text(window, height=10, width=40, font=font_tuple)
text_edit.pack(pady=10)

Encrypt_Button = Button(window, text="Encrypt", font=font_tuple, command=Encrypt)
Encrypt_Button.pack(pady=10)

Decrypt_Button = Button(window, text="Decrypt", font=font_tuple, command=Decrypt)
Decrypt_Button.pack()

result_text = Text(window, height=10, width=40, font=font_tuple)
result_text.pack(pady=10)
result_text.config(state="disabled")

############

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

window.mainloop()
