from playwright.sync_api import expect
from ..playwright_manager import page
import logging
from robot.api import logger
from robot.api.deco import library, keyword

@library
class ItemsPage:
    @keyword(name="Prüfe den Rucksack")
    def check_backpack_shown(self, backpack_name):
        link_element = page().locator("#item_4_title_link")
        expect(link_element).to_have_text(backpack_name)

    @keyword
    def logging_example_keyword(self):
        print("Simple print: hello world, I am checking it out")
        logging.debug("I am shown in debug log level only")
        logger.debug("<p>I am HTML message</p><a href='https://google.com'>SOME LINK</a>", html=True)

    def invisible_function(self):
        pass