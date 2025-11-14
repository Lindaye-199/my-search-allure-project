from playwright.sync_api import Page ,expect
def test_baidu(page: Page):
    page.goto(url="https://www.baidu.com")
    #page.wait_for_timeout(5_000)
    page.locator('#chat-textarea').fill('playwright')
    page.wait_for_timeout(5_000)
    # page.get_by_text('百度一下').click()
    page.locator("#chat-submit-button").click()
    page.wait_for_timeout(5_000)
    expect(page.get_by_text("https://github.com/microsoft/playwright")).to_be_visible()