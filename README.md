# IoTBlockchain
## introduction

This is a block chain demo for 5G-Vehicular networking, which adopts self-designed consensus protocol and distribution network to meet the two characteristics of high reliability and low lantency time.

## how to simulate the blockchain in your computer

### step1: start nodes

Execute the following command:

```shell
python run.py -p 5000
python run.py -p 5001
python run.py -p 5002
```

### step2: simulate trading

run simulation_test.py：

```shell
python simulation_test.py
```

### step3: check simple information

open your browser, and visit the following links:

- http://127.0.0.1:5001/height：get the height of blockchain
- http://127.0.0.1:5001/block_info?height=1：get the information of certain block
- http://127.0.0.1:5000/transactions/new：create a new transaction
