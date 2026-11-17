"""Shopdora-style stats from a Shopify store's public data: catalog size, price range,
store age (oldest product), sold-out share, top best-sellers.

Usage: python -I shopify_stats.py laviergeofficial.com [global.brand.com ...]
"""
import json, re, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode("utf-8", "ignore")


def stats(domain):
    products, page = [], 1
    while True:
        batch = json.loads(get(f"https://{domain}/products.json?limit=250&page={page}"))["products"]
        products += batch
        if len(batch) < 250:
            break
        page += 1
    prices = sorted(float(p["variants"][0]["price"]) for p in products)
    sold_out = sum(1 for p in products if not any(v.get("available") for v in p["variants"]))
    print(f"\n=== {domain}")
    print(f"products: {len(products)} · price ${prices[0]:.0f}–{prices[-1]:.0f} · median ${prices[len(prices) // 2]:.0f}")
    print(f"oldest product: {min(p['created_at'] for p in products)[:10]} (≈ store start) · newest: {max(p['created_at'] for p in products)[:10]}")
    print(f"sold out: {sold_out}/{len(products)} ({sold_out * 100 // len(products)}%)")
    # best-selling order is only exposed on the collection page, not in products.json
    html = get(f"https://{domain}/collections/all?sort_by=best-selling")
    handles = []
    for h in re.findall(r"/products/([a-z0-9-]+)", html):
        if h not in handles:
            handles.append(h)
    by_handle = {p["handle"]: p for p in products}
    print("best-sellers:")
    for i, h in enumerate([h for h in handles if h in by_handle][:10], 1):
        p = by_handle[h]
        print(f"  {i}. {p['title']} ${float(p['variants'][0]['price']):.0f}")


if __name__ == "__main__":
    for d in sys.argv[1:]:
        try:
            stats(d.replace("https://", "").strip("/"))
        except Exception as e:
            print(f"\n=== {d}\nfailed (not Shopify or blocked): {e}")
