# Mercury Banking API

This repository integrates with Mercury Bank's API, to offer an easy and seemless way for interacting with your accounts. 

### Prerequisites 

- [x] An account with mercury.
- [x] An API Key (Token), ready for consumption.
- [x] Python 3.*

## Usage

First update the `self.token` string value to the token you got from mercury 

### Get Balance Overview

```python
## Initialise the class.
mercury = Mercury()

## Get summary data. 
summary = mercury.accountOverview()

## Outout the account summary.
print("[+] Total Balance is ${:.2f} over {} accounts".format(summary['balance'], summary['accounts']))
```
