import requests

cfg = {}
with open("creds.env", encoding="utf-8") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            cfg[k] = v
print(cfg)
# r = requests.post(
#     cfg["RELAY_URL"],
#     headers={"x-relay-key": cfg["RELAY_KEY"]},
#     json={"prompt": "یک جمله کوتاه سلام بگو"},
#     timeout=60,
# )
# print(r.status_code)
# print(r.text)