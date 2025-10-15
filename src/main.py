import hashlib
import sys

def isHex(s: str) -> bool:
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def validateHash(hashStr: str) -> bool:
    hashStr = hashStr.strip().lower()

    if not isHex(hashStr):
        return False

    if len(hashStr) != 32:
        return False

    return True

def main():
    hash_alvo = input("Type the MD5 hash: ").strip().lower()

    if not validateHash(hash_alvo):
        print("Invalid hash, exiting...")
        sys.exit(1)

    try:
        with open("wordlist.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                word = linha.strip()
                if not word:
                    continue

                if hashlib.md5(word.encode()).hexdigest() == hash_alvo:
                    print(f"Hash quebrado: {hash_alvo} = {word}")
                    break
            else:
                print("No one password was found!")
    except FileNotFoundError:
        print("Error: 'wordlist.txt' not found.")
    except UnicodeDecodeError:
        print("Error: encoding problem while reading 'wordlist.txt'. Try another encoding.")

if __name__ == "__main__":
    main()