"""Probe a brand's website: platform, company/legal info in the footer, socials, apps/pixels.

Usage: python -I probe.py https://brand.com [https://global.brand.com ...]
"""
import html, re, sys, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Mozilla/5.0"}
KEYS = ["MST", "GPKD", "Công ty", "CÔNG TY", "Legal Representative", "Company", "Copyright",
        "Address", "Địa chỉ", "Hotline", "Designed in", "Made in", "Ship", "DHL"]
PIXELS = ["tiktok", "pinterest", "googletagmanager", "gtag", "facebook.net", "klaviyo", "judge.me",
          "loox", "yotpo", "paypal", "shop pay", "afterpay", "klarna", "hotjar", "clarity"]


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return dict(r.headers), r.read().decode("utf-8", "ignore")


def probe(url):
    headers, page = fetch(url)
    low = page.lower()
    print(f"\n=== {url}")
    platform = ("Shopify" if "shopify" in str(headers).lower() or "cdn.shopify.com" in low else
                "Haravan" if "haravan" in low or "X-ShopId" in headers else
                "WooCommerce" if "woocommerce" in low else
                "Squarespace" if "squarespace" in low else "?")
    print("platform:", platform)
    m = re.search(r"Shopify\.theme = (\{[^;]*\})", page)
    if m:
        print("theme:", m.group(1)[:160])
    m = re.search(r"Shopify\.currency = (\{[^}]*\})", page)
    if m:
        print("currency:", m.group(1))
    apps = sorted(set(re.findall(r"cdn\.shopify\.com/extensions/[0-9a-f-]+/([a-z0-9-]+?)-\d", page)))
    if apps:
        print("apps:", apps)
    print("pixels/payments:", [k for k in PIXELS if k in low])
    socials = sorted(set(re.findall(r"https?://(?:www\.)?(?:instagram|facebook|tiktok|youtube|pinterest|threads|shopee|lazada)\.[a-z.]+/[^\"' <?]{2,60}", page)))
    print("socials/marketplaces:", socials)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", page, flags=re.S))))
    for k in KEYS:
        i = text.find(k)
        if i >= 0:
            print(f"[{k}] …{text[max(0, i - 60):i + 200]}")


if __name__ == "__main__":
    for u in sys.argv[1:]:
        try:
            probe(u)
        except Exception as e:
            print(f"\n=== {u}\nfailed: {e}")
