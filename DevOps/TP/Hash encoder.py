from cryptography.hazmat.primitives import hashes
import time

nonce = 0
minzeroes = 2

start_time = time.time()

while True:
    
    digest = hashes.Hash(hashes.SHA256())
    digest.update(b"Alice->Bob 5BTC  Carol->Dave, 2BTC ...")
    s = bytearray(str(nonce), encoding = 'ISO-8859-1')
    digest.update(s)
    b = digest.finalize()
    h = b.hex()
    print("Iteration: %3d" %nonce, "Hash: %s" %h)
    
    nonce += 1
    
    if str(h)[:minzeroes] == '0' * minzeroes:
        print(f"Hash starting starting with atleast {minzeroes} zeroes found !!!")
        break
    
end_time = time.time()
    
elapsed_time = end_time - start_time
print(f"Elapsed Time:", elapsed_time, "seconds")