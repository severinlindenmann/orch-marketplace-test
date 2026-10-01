import json, sys

req = json.loads(sys.stdin.readline())
key = req["params"]["ticket"]["key"]
print(json.dumps({"jsonrpc": "2.0", "id": req["id"], "result": {"set": {"greeting": "hello from " + key}, "sections": {}, "artifacts": []}}))
# a different tree than the one the entry digests
