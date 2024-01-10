from btc.btc_rpc_client import BtcJsonRpcClient


if __name__ == '__main__':
    client = BtcJsonRpcClient("btc", "", "host", 8000)
    print(client.get_block(""))