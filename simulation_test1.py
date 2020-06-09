# coding:utf-8
import json
import random
import time
import urllib2


def bootstrap(address, seeds):
    data = {
        "seeds": seeds
    }
    req = urllib2.Request("http://" + address + "/bootstrap",
                          json.dumps(data),
                          {"Content-Type": "application/json"})
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res


def run():
    node1 = get_node_info("127.0.0.1:5000")
    node2 = get_node_info("127.0.0.1:5001")
    node3 = get_node_info("127.0.0.1:5002")
    node4 = get_node_info("127.0.0.1:5003")
    node5 = get_node_info("127.0.0.1:5004")

    node1_seeds = [
        {"node_id": node2["node_id"], "ip":node2["ip"], "port":node2["port"]},
        {"node_id": node3["node_id"], "ip": node3["ip"], "port": node3["port"]},
        {"node_id": node4["node_id"], "ip": node4["ip"], "port": node4["port"]},
        {"node_id": node5["node_id"], "ip": node5["ip"], "port": node5["port"]}
    ]
    bootstrap("127.0.0.1:5000", node1_seeds)

    node2_seeds = [
        {"node_id": node1["node_id"], "ip": node1["ip"], "port": node1["port"]},
        {"node_id": node3["node_id"], "ip": node3["ip"], "port": node3["port"]},
        {"node_id": node4["node_id"], "ip": node4["ip"], "port": node4["port"]},
        {"node_id": node5["node_id"], "ip": node5["ip"], "port": node5["port"]}
    ]
    bootstrap("127.0.0.1:5001", node2_seeds)

    node3_seeds = [
        {"node_id": node2["node_id"], "ip": node2["ip"], "port": node2["port"]},
        {"node_id": node1["node_id"], "ip": node1["ip"], "port": node1["port"]},
        {"node_id": node4["node_id"], "ip": node4["ip"], "port": node4["port"]},
        {"node_id": node5["node_id"], "ip": node5["ip"], "port": node5["port"]}
    ]
    bootstrap("127.0.0.1:5002", node3_seeds)
    
    node4_seeds = [
        {"node_id": node1["node_id"], "ip": node1["ip"], "port": node1["port"]},
        {"node_id": node3["node_id"], "ip": node3["ip"], "port": node3["port"]},
        {"node_id": node2["node_id"], "ip": node2["ip"], "port": node2["port"]},
        {"node_id": node5["node_id"], "ip": node5["ip"], "port": node5["port"]}
    ]
    bootstrap("127.0.0.1:5003", node4_seeds)

    node5_seeds = [
        {"node_id": node2["node_id"], "ip": node2["ip"], "port": node2["port"]},
        {"node_id": node1["node_id"], "ip": node1["ip"], "port": node1["port"]},
        {"node_id": node3["node_id"], "ip": node3["ip"], "port": node3["port"]},
        {"node_id": node4["node_id"], "ip": node4["ip"], "port": node4["port"]}
    ]
    bootstrap("127.0.0.1:5004", node5_seeds)
    
    
    print "ok"
    time.sleep(1)

    node1_wallet = node1["wallet"]
    node2_wallet = node2["wallet"]
    node3_wallet = node3["wallet"]
    node4_wallet = node4["wallet"]
    node5_wallet = node5["wallet"]

    while True:
        # node1 发送给node2 node3 node4 node5
        node1_balance = get_balance("127.0.0.1:5000", node1_wallet)
        node1_balance = node1_balance['balance']
        if node1_balance > 0:
            amount = random.randint(1, node1_balance)/10
            print 'send from node1 to node2 with amount:'+str(amount)
            simulate_tx("127.0.0.1:5000", node1_wallet, node2_wallet, amount)
            time.sleep(random.randint(4,5))

        node1_balance = get_balance("127.0.0.1:5000", node1_wallet)
        node1_balance = node1_balance['balance']
        if node1_balance > 0:
            amount = random.randint(1, node1_balance)/10
            print 'send from node1 to node3 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5000", node1_wallet, node3_wallet, amount)
            time.sleep(random.randint(4,5))

        node1_balance = get_balance("127.0.0.1:5000", node1_wallet)
        node1_balance = node1_balance['balance']
        if node1_balance > 0:
            amount = random.randint(1, node1_balance)/10
            print 'send from node1 to node4 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5000", node1_wallet, node4_wallet, amount)
            time.sleep(random.randint(4,5))

        node1_balance = get_balance("127.0.0.1:5000", node1_wallet)
        node1_balance = node1_balance['balance']
        if node1_balance > 0:
            amount = random.randint(1, node1_balance)/10
            print 'send from node1 to node5 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5000", node1_wallet, node5_wallet, amount)
            time.sleep(random.randint(4,5))

        # node2 发送给node1 node3 
        node2_balance = get_balance("127.0.0.1:5001", node2_wallet)
        node2_balance = node2_balance['balance']
        if node2_balance > 0:
            amount = random.randint(1, node2_balance)/10
            print 'send from node2 to node1 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5001", node2_wallet, node1_wallet, amount)
            time.sleep(random.randint(4,5))

        node2_balance = get_balance("127.0.0.1:5001", node2_wallet)
        node2_balance = node2_balance['balance']
        if node2_balance > 0:
            amount = random.randint(1, node2_balance)/10
            print 'send from node2 to node3 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5001", node2_wallet, node3_wallet, amount)
            time.sleep(random.randint(4,5))
        #
        # node3 发送给node1 node4
        node3_balance = get_balance("127.0.0.1:5002", node3_wallet)
        node3_balance = node3_balance['balance']
        if node3_balance > 0:
            amount = random.randint(1, node3_balance)/10
            print 'send from node3 to node1 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5002", node3_wallet, node1_wallet, amount)
            time.sleep(random.randint(4,5))

        node3_balance = get_balance("127.0.0.1:5002", node3_wallet)
        node3_balance = node3_balance['balance']
        if node3_balance > 0:
            amount = random.randint(1, node3_balance)/10
            print 'send from node3 to node2 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5002", node3_wallet, node4_wallet, amount)
            time.sleep(random.randint(4,5))
        

        #node4 发送给 node2 node5
        node4_balance = get_balance("127.0.0.1:5003", node4_wallet)
        node4_balance = node4_balance['balance']
        if node4_balance > 0:
            amount = random.randint(1, node4_balance)/10
            print 'send from node4 to node2 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5003", node4_wallet, node2_wallet, amount)
            time.sleep(random.randint(4,5))

        node4_balance = get_balance("127.0.0.1:5003", node4_wallet)
        node4_balance = node4_balance['balance']
        if node4_balance > 0:
            amount = random.randint(1, node4_balance)/10
            print 'send from node4 to node5 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5003", node4_wallet, node5_wallet, amount)
            time.sleep(random.randint(4,5))
        #node5 发送给 node4
        node5_balance = get_balance("127.0.0.1:5004", node5_wallet)
        node5_balance = node5_balance['balance']
        if node5_balance > 0:
            amount = random.randint(1, node5_balance)/10
            print 'send from node5 to node4 with amount:' + str(amount)
            simulate_tx("127.0.0.1:5004", node5_wallet, node4_wallet, amount)
            time.sleep(random.randint(4,5))
        time.sleep(5)


def simulate_tx(address, sender, receiver, amount):
    data = {
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }

    req = urllib2.Request(url="http://" + address + "/transactions/new",
                          headers={"Content-Type": "application/json"}, data=json.dumps(data))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return res


def get_balance(address, wallet_addres):
    req = urllib2.Request(url="http://" + address + "/balance?address=" + wallet_addres,
                          headers={"Content-Type": "application/json"})

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return json.loads(res)


def get_node_info(address):
    req = urllib2.Request(url="http://" + address + "/curr_node",
                          headers={"Content-Type": "application/json"})

    res_data = urllib2.urlopen(req)
    res = res_data.read()
    return json.loads(res)


run()