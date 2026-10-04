import requests

cfg = {}
with open("creds.env", encoding="utf-8") as f:
    for line in f:
        if "=" in line and not line.startswith("#"):
            k, v = line.strip().split("=", 1)
            cfg[k] = v


def ask_llm(prompt):
    r = requests.post(
        cfg["RELAY_URL"],
        headers={"x-relay-key": cfg["RELAY_KEY"]},
        json={"prompt": prompt},
        timeout=60,
    )
    if r.status_code != 200:
        raise RuntimeError(f"Worker error {r.status_code}: {r.text[:200]}")
    return r.text.strip()


if __name__ == "__main__":
    print(ask_llm("پایتخت ایران کجاست؟ یک کلمه جواب بده"))