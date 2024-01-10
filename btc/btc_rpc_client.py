import requests


class BtcJsonRpcClient:

    def __init__(self, username, password, host, port):
        self.base_url = f"http://{username}:{password}@{host}:{port}"

    def post(self, method, params):
        return requests.post(self.base_url, json={
            "jsonrpc": "1.0",
            "id": "",
            "method": method,
            params: params
        }).json()

    def get(self, method, params):
        return requests.get(self.base_url, json={
            "jsonrpc": "1.0",
            "id": "",
            "method": method,
            params: params
        }).json()

    def get_blockchain_info(self):
        return self.post("getblockchaininfo", [])

    def get_block_header(self, block_hash):
        return self.post("getblockheader", [block_hash])

    def get_block(self, block_hash):
        return self.post("getblock", [block_hash])

    def get_transaction(self):
        pass


if __name__ == '__main__':
    pass
