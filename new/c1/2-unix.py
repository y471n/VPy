import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]
    dicFile = open('dictionary.txt', 'r')
    for word in dicFile.readlines():
        word = word.strip("\n")
        cryptWord = crypt.crypt(word, salt=salt)
        if cryptPass == cryptWord:
            print ("[+] Found Password: " + word+"\n")
            return
    print ("[-] No Password Found")

def main():
    passFile = open('passwords.txt')
    for line in passFile:
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(' ')
            print ("[*] Cracking Password for: "+user)
            testPass(cryptPass)

if __name__ == "__main__":
    main()