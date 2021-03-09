#!/usr/bin/env python3
import os
import sys
import hashlib

def read_file(file):
    # Read en entire file and returns file bytes.
    os.system('cls' if os.name == 'nt' else 'clear')

    BUFFER_SIZE = 16384 # 16 Kilo Bytes.
    b = b""
    with open(file, 'rb') as f:
        while True:
        # Read 16 Kilo Bytes from the file.
            bytes_read = f.read(BUFFER_SIZE)
            if bytes_read:
                # If there is bytes, append them.
                b += bytes_read
            else:
                break
    
    return b

if __name__ == "__main__":
    # Read some file.
    file_content = read_file(sys.argv[1])
    # Some chksums:
    # Hash with MD5 (not recommended).
    print("MD5:", hashlib.md5(file_content).hexdigest())

    # Hash with SHA-2 (SHA-256 & SHA-512).
    print("SHA-256:", hashlib.sha256(file_content).hexdigest())
    print("SHA-512:", hashlib.sha512(file_content).hexdigest())

    # Hash with SHA-3.
    print("SHA-3-256:", hashlib.sha3_256(file_content).hexdigest())
    print("SHA-3-512:", hashlib.sha3_512(file_content).hexdigest())

    # Hash with BLAKE2.
    # 256-bit BLAKE2 (or BLAKE2s).
    print("BLAKE2c:", hashlib.blake2s(file_content).hexdigest())
    # 512-bit BLAKE2 (or BLAKE2b).
    print("BLAKE2b:", hashlib.blake2b(file_content).hexdigest())