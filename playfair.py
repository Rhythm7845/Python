import tkinter as tk

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def FillerLetter(text):
    k = len(text)
    if k % 2 == 0:
        for i in range(0, k, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else: new_word = text
    else:
        for i in range(0, k-1, 2):
            if text[i] == text[i+1]:
                new_word = text[0:i+1] + str('x') + text[i+1:]
                new_word = FillerLetter(new_word)
                break
            else: new_word = text
    return new_word

def Diagraph(text):
    Diagraph = []
    group = 0
    for i in range(2, len(text), 2):
        Diagraph.append(text[group:i])
        group = i
    Diagraph.append(text[group:])
    return Diagraph 

def generateTable(key, list1):
    table, keyLetters = [], []
    for i in key:
        if i not in keyLetters: keyLetters.append(i)
    compElements = []
    for i in keyLetters:
        if i not in compElements: compElements.append(i)
    for i in list1:
        if i not in compElements: compElements.append(i)
    while compElements != []:
        table.append(compElements[:5])
        compElements = compElements[5:]
    return table

def search(table, element):
    for i in range(5):
        for j in range(5):
            if table[i][j] == element: return i,j

def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1c == 4: char1 = matr[e1r][0]
    else: char1 = matr[e1r][e1c+1]
    char2 = ''
    if e2c == 4: char2 = matr[e2r][0]
    else: char2 = matr[e2r][e2c+1]
    return char1, char2

def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    if e1r == 4: char1 = matr[0][e1c]
    else: char1 = matr[e1r+1][e1c]
    char2 = ''
    if e2r == 4: char2 = matr[0][e2c]
    else: char2 = matr[e2r+1][e2c]
    return char1, char2

def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
    char1 = ''
    char1 = matr[e1r][e2c]
    char2 = ''
    char2 = matr[e2r][e1c]
    return char1, char2

def encryptByPlayfairCipher(Matrix, plainList):
    CipherText = []
    for i in range(0, len(plainList)):
        c1 = 0
        c2 = 0
        ele1_x, ele1_y = search(Matrix, plainList[i][0])
        ele2_x, ele2_y = search(Matrix, plainList[i][1])
        if ele1_x == ele2_x: c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        elif ele1_y == ele2_y: c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        else: c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
        cipher = c1 + c2
        CipherText.append(cipher)
    return CipherText

def main():
    root = tk.Tk()
    root.title("Playfair Cipher")
    root.geometry("320x200")
    plaintext_label = tk.Label(root, text="Enter Plain Text:")
    plaintext_label.pack(pady=1)
    plaintext_entry = tk.Entry(root, width=40)
    plaintext_entry.pack(pady=5)
    key_label = tk.Label(root, text="Enter Key:")
    key_label.pack(pady=1)
    key_entry = tk.Entry(root, width=40)
    key_entry.pack(pady=2)
    result_label = tk.Label(root, text="CipherText: ", wraplength=350)
    result_label.pack(pady=2)
    def encrypt_text():
        plaintext = plaintext_entry.get()
        key = key_entry.get()
        plaintext = plaintext.lower()
        temptext = ""
        for i in plaintext:
            if i == " ": continue
            else: temptext = temptext + i
        plaintext = temptext
        PlainTextList = Diagraph(FillerLetter(plaintext))
        if len(PlainTextList[-1]) != 2: PlainTextList[-1] = PlainTextList[-1] + 'x'
        matrix = generateTable(key, list1)
        cipherList = encryptByPlayfairCipher(matrix, PlainTextList)
        cipherText = "".join(cipherList)
        result_label.config(text=f"CipherText: {cipherText}")
    encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
    encrypt_button.pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    main()