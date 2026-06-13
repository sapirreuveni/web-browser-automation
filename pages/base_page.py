from playwright.sync_api import Page
import re
class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def fill_text(self, locator, txt: str) -> None:
            el = self.page.locator(locator)
            self._highlight_element(locator)
            el.scroll_into_view_if_needed()
            el.hover()
            el.fill(txt)


    def get_text(self, locator) -> str:
        return self.page.locator(locator).inner_text().strip()


    def click(self, locator, index: int = None):

        if index is not None:
            el = self.page.locator(locator).nth(index)

            el.evaluate("""e => {
                    e.style.outline = "3px solid yellow";
                    setTimeout(() => e.style.outline = "", 1000);
                }""")

            el.scroll_into_view_if_needed()
            el.hover()
            el.click()

        else:
            self._highlight_element(locator)
            el = self.page.locator(locator)
            el.scroll_into_view_if_needed()
            el.hover()
            el.click()

    def select_option(self, locator, value):
        el = self.page.locator(locator)
        self._highlight_element(locator)
        el.scroll_into_view_if_needed()
        el.select_option(value=value)



    # def _highlight_element(self, locator: str, color: str = "yellow"):
    #     element = self.page.locator(locator).first
    #     element.evaluate(f"""
    #         (el) => {{
    #             const origShadow = el.style.boxShadow;
    #             const origBackground = el.style.backgroundColor;
    #
    #             el.style.boxShadow = '0 0 10px 4px rgba(0, 150, 255, 0.7)';
    #             el.style.backgroundColor = '{color}';
    #
    #             setTimeout(() => {{
    #                 el.style.boxShadow = origShadow;
    #                 el.style.backgroundColor = origBackground;
    #             }}, 300);
    #         }}
    #     """)

    def _highlight_element(self, locator: str):
        try:
            self.page.eval_on_selector(
                locator,
                """el => {
                    el.style.outline = "3px solid yellow";
                    setTimeout(() => {
                        el.style.outline = "";
                    }, 1000);
                }"""
            )
        except:
            pass


    @staticmethod
    def clean_text(text: str) -> str:
        text = text.replace("×", "").replace("\n", " ")
        text = re.sub(r"^\s*(success|warning)\s*:\s*", "", text, flags=re.IGNORECASE)
        return " ".join(text.split())


    def force_check_checkbox(self, locator: str) -> None:
        self.page.evaluate(
            """(selector) => {
                const cb = document.querySelector(selector);
                if (cb && !cb.checked) {
                    cb.checked = true;
                }
            }""",
            locator
        )








