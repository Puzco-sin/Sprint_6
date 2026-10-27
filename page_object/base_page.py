from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(driver, 15)

    def open_url(self, url: str) -> None:
        self._driver.get(url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return self._driver.find_element(*locator)

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self._driver.find_elements(*locator)

    def wait_until(self, condition):
        return self._wait.until(condition)

    def wait_for_elements_count(
        self, locator: tuple[str, str], count: int
    ) -> list[WebElement]:
        return self.wait_until(
            lambda _: (
                elements
                if len(elements := self.find_elements(locator)) == count
                else False
            )
        )

    def wait_for_matching_element(
        self, locator: tuple[str, str], text: str
    ) -> WebElement:
        return self.wait_until(
            lambda _: next(
                (
                    element
                    for element in self.find_elements(locator)
                    if element.text == text
                    and element.is_displayed()
                    and element.is_enabled()
                ),
                False,
            )
        )

    def wait_for_url(self, url: str) -> str:
        return self.wait_until(EC.url_to_be(url))

    def wait_for_new_window(self, current_handles: list[str]) -> bool:
        return self.wait_until(EC.new_window_is_opened(current_handles))

    def switch_to_window(self, window_handle: str) -> None:
        self._driver.switch_to.window(window_handle)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def current_window_handle(self) -> str:
        return self._driver.current_window_handle

    @property
    def window_handles(self) -> list[str]:
        return self._driver.window_handles
