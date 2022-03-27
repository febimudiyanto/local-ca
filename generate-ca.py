
import subprocess as sp
import os


# check if folder "ca-cert" exists
# if not, create it
# if yes, delete it
if os.path.exists("ca-cert"):
    sp.call(["rm", "-rf", "ca-cert"])
sp.call(["mkdir", "ca-cert"])

# 0. create config file
open ("ca-cert/ca.cnf", "w").write(
"""
[req]
default_bits = 2048
prompt = no
default_md = sha256
encrypt_key = no
distinguished_name = dn

[dn]
C = ID
O = Local Digital Cert Authority
OU = www.ca.local
CN = Self-Signed Root CA
"""
)
# 1. generate a root CA certificate and private key
sp.call(['openssl', 'genrsa', '-out', 'ca-cert/ca.key', '2048'])
# 2. generate CSR with config file
sp.call(['openssl', 'req', '-new', '-key', 'ca-cert/ca.key', '-out', 'ca-cert/ca.csr', '-config', 'ca-cert/ca.cnf'])
# 3. create a self-signed CA certificate
validDate = input("Enter the expiration (days) of the certificate: ")
sp.call(['openssl', 'x509', '-req', '-days', validDate, '-in', 'ca-cert/ca.csr', '-signkey', 'ca-cert/ca.key', '-out', 'ca-cert/ca.crt'])
print("CA certificate and private key generated")