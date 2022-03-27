# local-ca

Create a local Certificate Authority with python

1. Clone this repo
2. Generate the CA with this command
```bash
python3 generate-ca.py
```
3. Prepare your CSR file
4. Signing the CSR file with this command
```bash
python3 register-crt.py
```


Note:
Root CA cert in ca-cert/ca.crt
Server cert in server.crt
