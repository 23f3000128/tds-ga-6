import re
from playwright.sync_api import sync_playwright

SEEDS = range(41, 51)

def main():
    total = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for seed in SEEDS:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Scraping {url}", flush=True)
            page.goto(url, wait_until="domcontentloaded")
            page.wait_for_selector("table", state="visible")

            text = page.locator("table").inner_text()
            nums = re.findall(r"-?\d+(?:\.\d+)?", text)
            total += sum(float(n) for n in nums)

        browser.close()

    total = int(round(total))
    print(f"SUM: {total}", flush=True)
    print(f"TOTAL_SUM={total}", flush=True)

if __name__ == "__main__":
    main()
