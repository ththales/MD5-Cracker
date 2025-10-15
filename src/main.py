import hashlib

hash_alvo = input("Type the hash: ").strip()

try:
    with open("wordlist.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            palavra = linha.strip()
            if not palavra:
                continue

            if hashlib.md5(palavra.encode()).hexdigest() == hash_alvo:
                print(f"Hash quebrado: {hash_alvo} = {palavra}")
                break
        else:
            print("No one password was found!")
except FileNotFoundError:
    print("Error: 'wordlist.txt' not found.")
except UnicodeDecodeError:
    print("Error: encoding problem while reading 'wordlist.txt'. Try another encoding.")
