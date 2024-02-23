# Bitcoin Python Codes

Bitcoin is a decentralized digital currency that enables online payments between parties without going through a central authority like a bank or government. Created by Satoshi Nakamoto in 2008.

This repository includes Python scripts demonstrating different technical aspects of Bitcoin.

Bitcoin is the money of the future.

Bitcoin is today's hope.

***

Besides the Python codes, I have also written several articles related to Bitcoin:

1. Elliptic Curve in Bitcoin

  > #### English Version: https://estudiobitcoin.com/elliptic-curve-in-bitcoin/
  > #### Spanish Version: https://estudiobitcoin.com/curva-eliptica-en-bitcoin/



## ECDSA Simple Signing and Verifying Flow
[ECDSA-simple-flow.py](https://github.com/SalvaZaraes/bitcoin/blob/main/ECDSA-simple-flow.py)

This Python script showcases the ECDSA process for signing plaintext messages and verifying their authenticity using a public-private key pair. It unfolds each step transparently, unlike comprehensive library modules. It generates key pairs, hashes messages with SHA-256, signs messages, and enables interactive signature verification.


## secp256k1 Elliptic Curve Generator Point Multiplier Visualizer

[secp256k1-elliptic-curve-generator-point-multiplier-visualizer.py](https://github.com/SalvaZaraes/bitcoin/blob/main/secp256k1-elliptic-curve-generator-point-multiplier-visualizer.py) 

The script provides a step-by-step visualization of multiplying a generator point on an elliptic curve by a scalar value. This is done through a series of point duplications and additions, as used in ECC cryptography.

The script allows inputting a desired multiple of the secp256k1 generator point. It calculates the sequence of point operations required to arrive at this multiple through analitic geometry.

The steps are shown graphically on the secp256k1 curve plotted with Matplotlib. Each point duplication is marked with a red line and each point addition with a green line. The points are labeled clearly as multiples of the generator "G".

This provides an intuitive understanding of how private key scalars derive public keys on an elliptic curve.

### 3G Example
![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/91db238e-e635-4e46-a03c-0a13d5c4d439)
### 4G Example
![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/5201269b-488a-41f0-b858-c804f610bcf3)
### 6G Example
![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/a7b11f0e-eb01-4390-921c-7ffa8ff4c7c9)


## Elliptic Curve Field P Chart

The [elliptic-curve-field-p-chart.py](https://github.com/SalvaZaraes/bitcoin/blob/main/elliptic-curve-field-p-chart.py) script generates an interactive visualization of an elliptic curve plotted over a finite field.

![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/34e31466-7f09-44f6-8c63-b54829261254)


## Elliptic Curve a+b=c labels

The [elliptic-curve-a+b=c-labels.py](https://github.com/SalvaZaraes/bitcoin/blob/main/elliptic-curve-a%2Bb%3Dc-labels.py) script provides a visual demonstration of elliptic curve point addition. It graphs the secp256k1 elliptic curve used in Bitcoin and marks sample points A, B, and C.

![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/90f5f503-18f6-4c17-be88-5606f375937c)


## Elliptic Curve Secp256k1 Simple Plot

The [elliptic-curve.py](https://github.com/SalvaZaraes/bitcoin/blob/main/elliptic-curve.py) script generates a simple plot of the secp256k1 elliptic curve, the one used in Bitcoin, over the real numbers.

![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/41781107-10fb-45d7-9855-0f6baf8f97b9)


## RSA vs ECC keys security chart comparison

The [RSA-vs-ECC-keys-security-chart-comparison.py](https://github.com/SalvaZaraes/bitcoin/blob/main/RSA-vs-ECC-keys-security-chart-comparison.py) script generates a chart comparing the security levels of ECC and RSA keys of equivalent strength.

![image](https://github.com/SalvaZaraes/bitcoin/assets/153385473/73c6fc0a-8768-4c1c-bbaa-7d9c7f2a702f)


