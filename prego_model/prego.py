from playwright.sync_api import sync_playwright, Playwright


class Prego:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_url(self, url: str):
        def handler():
            self.page.get_by_role("button", name="Так").click()
        self.page.goto(url)

        return self

    def open_login_form(self):
        self.page.locator("#personal-name .lk").click()
        return self

    def phone(self, phone: str):
        self.page.locator("#signinForm").get_by_placeholder("+38(___) ___-__-__").fill(phone)
        return self

    def email(self, phone: str):
        self.page.locator(".my_details").get_by_placeholder("Електронна пошта").fill(phone)
        self.page.locator(".my_details").get_by_placeholder("Електронна пошта").press("Enter")
        return self

    def password(self, password: str):
        self.page.locator("#signinForm").get_by_placeholder("Пароль").fill(password)
        return self

    def click_login_button(self):
        self.page.get_by_role("button", name="Увійти", exact=True).click()
        return self

    def authorization(self):
        self.open_login_form()
        self.phone('073123456789')
        self.password('1234567890qwerty')
        self.click_login_button()

    def check_menu_button(self, button, text):
        self.page.get_by_role("banner").get_by_role("link", name=button).click()
        body_text = self.page.content()
        assert text in body_text

    def go_to_blog(self, text):
        self.page.get_by_role("link", name="РЕКОМЕНДУЄМО Скільки пар взуття потрібно жінці для щастя 15 липня 2020").click()
        body_text = self.page.content()
        assert text in body_text

    def shoes_catalog(self,):
        self.page.locator(".header-bottom__nav-list").get_by_role("link", name="ЖІНОЧЕ ВЗУТТЯ").hover()
        self.page.get_by_role("link", name="ЖІНОЧІ ТУФЛІ").click()
        return self

    def filter_result(self):
        self. page.get_by_text("Туфлі на низькому ходу", exact=True).click()
        self.page.get_by_role("checkbox", name="38").check()
        self.page.get_by_text("ОСІНЬ", exact=True).click()
        self.page.get_by_text("Чорний", exact=True).click()
        self.page.locator(".x4x4").click()
        self.page.locator(".x3x3").click()
        return self

    def open_page_shoes(self):
        self.page.locator("article").filter(has_text="#031374 NEW").get_by_role("link").click()
        return self

    def photo_owerview(self):
        self.page.get_by_label("Next").click()
        self.page.get_by_label("Next").click()
        self.page.get_by_label("Next").click()
        self.page.get_by_label("Next").click()
        self.page.get_by_label("Next").click()
        return self

    def check_bonus(self):
        self.page.get_by_text("Отримати бонус").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("#button_cross").click()
        return self

    def add_to_cart(self):
        self.page.get_by_role("button", name="Купити").nth(1).click()
        return self

    def view_cart(self):
        self.page.get_by_role("button", name="оформити замовлення").click()
        self.page.wait_for_load_state()
        body_text = self.page.content()
        assert "РЕКОМЕНДУЄМО" in body_text

    def open_recommended_product(self):
        max_attempts = 10
        for _ in range(max_attempts):
            recommended_link = self.page.get_by_role("link", name="Сумка-почтальонка - Фото №").first
            if recommended_link:
                recommended_link.click()
                return self

            # Натискати кнопку "Next", якщо продукт не знайдено
            self.page.get_by_role("button", aria_label="Next").click()

    def open_action_page(self):
        (self.page.locator("li").filter(
        has_text="АКЦІЇ УСІ АКЦІЇ РОЗПРОДАЖ ЖІНОЧОГО ВЗУТТЯ РОЗПРОДАЖ ЧОЛОВІЧОГО ВЗУТТЯ РОЗПРОДАЖ ").locator(
            "div").first.click())
        self.page.get_by_text("До -30% НА ВЗУТТЯ ТА СУМКИ", exact=True).click()
        self.page.get_by_role("navigation").get_by_role("link", name="АКСЕСУАРИ").click()
        self.page.locator("span").filter(has_text="ПАРАСОЛЬКИ").click()
        self.page.get_by_role("button", name="Оплатити замовлення").click()
        return self


    def check_error_message_email_field(self, message: str):
        locator = self.page.locator("#Email-error").nth(0)
        page_text = locator.inner_text()
        assert message in page_text, f"Очікуване повідомлення '{message}' не знайдено у тексті: '{page_text}'"
        return self

    def check_error_message_for_empty_phone_field(self, message: str):
        locator = self.page.locator("#signinForm .error span").nth(0)
        page_text = locator.inner_text()
        assert message in page_text, f"Очікуване повідомлення '{message}' не знайдено у тексті: '{page_text}'"
        return self

    def check_error_message(self, message: str):
        page_text = self.page.inner_text('.sc-gYhhMS.hDYNz')
        assert message in page_text
        return self

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
