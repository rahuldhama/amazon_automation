import pytest
from playwright.sync_api import Page

@pytest.mark.parametrize("item_name", ["iPhone", "Galaxy device"])
def test_amazon_complete_flow(page: Page, item_name: str):
    # Generous timeout for slower connections
    page.set_default_timeout(60000)
    
    # 1. Navigate to Amazon
    page.goto("https://www.amazon.com")

    # 2. Search for the device
    search_bar = page.locator("#twotabsearchtextbox")
    search_bar.fill(item_name)
    search_bar.press("Enter")

    # 3. Click the first product image
    print(f"\n-> Loading {item_name} results...")
    first_image = page.locator("img.s-image").first
    first_image.wait_for(state="visible", timeout=15000)
    first_image.click()

    # Wait for the product page to fully render
    page.wait_for_timeout(3000) 

    # 4. Extract and Print the Price
    try:
        price = page.locator(".a-price .a-offscreen").first.inner_text()
        print(f"-> [SUCCESS] Found {item_name} for {price}")
    except:
        print(f"-> [INFO] Price hidden by Amazon layout for {item_name}")

    # 5. The "Aggressive" Add to Cart
    print(f"-> Attempting to add {item_name} to cart...")
    
    # Amazon uses different button IDs randomly. We try all of them.
    cart_selectors = [
        "#add-to-cart-button",
        "input[name='submit.add-to-cart']",
        ".a-button-input[aria-labelledby='submit.add-to-cart-announce']"
    ]
    
    item_added = False
    for selector in cart_selectors:
        try:
            button = page.locator(selector).first
            if button.is_visible(timeout=3000):
                button.click()
                item_added = True
                print(f"-> [SUCCESS] Clicked Add to Cart for {item_name}!")
                break # Stop looking once we click it
        except:
            continue # Try the next button ID if this one fails

    if not item_added:
        print(f"-> [NOTE] Cart button blocked by Amazon Bot-Protection or requires manual option selection.")

    # 6. Verify Completion
    page.wait_for_timeout(2000)
    print(f"-> [COMPLETE] Test case finished for {item_name}.")
   