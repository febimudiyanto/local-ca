import subprocess as sp
import os

# check ca-cert/ca.crt and ca-cert/ca.key
if os.path.exists("ca-cert/ca.crt") and os.path.exists("ca-cert/ca.key"):
    print ("CA is ready")
else:
    print("CA is not ready, generate it first")
    print("Run generate-ca.py")
    exit()

# input csr file
csrFile = input("Enter the CSR file name: ")

# print csr information
print("CSR information:")
# csr decoder and return the subject
csrInfo = sp.check_output(['openssl', 'req', '-in', csrFile, '-noout','-subject'])
print("".join(csrInfo.decode('utf-8').split("subject=")[1].replace(", ", "\n")))
# validate csr
print("Do you want to continue? (y/n)")
if input().lower() == "y":
    pass
else:
    exit()


# input expiration days
validDate = input("Enter the expiration (days) of the certificate: ")

# openssl x509 -req -in fabrikam.csr -CA  contoso.crt -CAkey contoso.key -CAcreateserial -out fabrikam.crt -days 365 -sha256
sp.call(['openssl', 'x509', '-req', '-in', csrFile, '-CA', 'ca-cert/ca.crt', '-CAkey', 'ca-cert/ca.key', '-CAcreateserial', '-out', 'server.crt', '-days', validDate, '-sha256'])
