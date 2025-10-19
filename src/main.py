import hashlib
import sys
import argparse
import time
from typing import List

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

def common_variants(word: str, enable: bool) -> List[str]:
    if not enable:
        return [word]
    variants = [word]

    low = word.lower()
    up = word.upper()
    cap = word.capitalize()
    stripped = word.strip()

    for v in (stripped, low, up, cap):
        if v and v not in variants:
            variants.append(v)
    return variants

def parse_args():
    parser = argparse.ArgumentParser(description="Simple MD5 wordlist cracker.")
    parser.add_argument("--wordlist", "-w", default="wordlist.txt", help="Path to the wordlist file (default: wordlist.txt)")
    parser.add_argument("--encoding", "-e", default="utf-8", help="Encoding for reading the file and for .encode() (default: utf-8)")
    parser.add_argument("--no-stop", action="store_true", help="Do not stop at the first match (search for all matches)")
    parser.add_argument("--progress-interval", "-p", type=int, default=10000, help="Show progress every N lines (0 to disable). Default: 10000")
    parser.add_argument("--transforms", action="store_true", help="Try common variants of words (lower, upper, capitalize, strip)")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        hash_target = input("Type the MD5 hash: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Exiting...")
        sys.exit(1)

    if not validateHash(hash_target):
        print("Invalid hash, exiting...")
        sys.exit(1)

    start_time = time.time()
    checked = 0
    found_any = False
    try:
        with open(args.wordlist, "r", encoding=args.encoding) as f:
            try:
                for line_no, line in enumerate(f, start=1):
                    word = line.rstrip("\n")

                    word_stripped = word.strip()

                    if not word_stripped:
                        continue

                    variants = common_variants(word_stripped, args.transforms)

                    for candidate in variants:
                        checked += 1
                        try:
                            candidate_hash = hashlib.md5(candidate.encode(args.encoding, errors="ignore")).hexdigest()
                        except Exception:
                            continue

                        if candidate_hash == hash_target:
                            found_any = True
                            print(f"Hash cracked: {hash_target} = {candidate}  (line {line_no})")
                            if not args.no_stop:
                                elapsed = time.time() - start_time
                                print(f"Total checked: {checked} words. Time: {elapsed:.2f}s")
                                return

                    if args.progress_interval > 0 and (line_no % args.progress_interval == 0):
                        elapsed = time.time() - start_time
                        print(f"[progress] lines read: {line_no}, candidates checked: {checked}, time: {elapsed:.2f}s")

                if not found_any:
                    print("No password was found!")
                else:
                    print("Search completed. All entries in the wordlist have been verified.")
            except KeyboardInterrupt:
                elapsed = time.time() - start_time
                print(f"\nInterrupted by user. Checked: {checked} candidates in {elapsed:.2f}s")
    except FileNotFoundError:
        print(f"Error: '{args.wordlist}' not found.")
    except UnicodeDecodeError:
        print(f"Error: encoding problem while reading '{args.wordlist}'. Try another encoding (use --encoding).")

if __name__ == "__main__":
    main()