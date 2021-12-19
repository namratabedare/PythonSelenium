import time

from selenium import webdriver
import unittest

from testdata.properties import cookbook
from utilities.supporing_functions import launch_site
from utilities.webdriver_instance import new_web_driver


class HandleDropDown(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = new_web_driver("local", "CH")
        website = cookbook
        launch_site(cls.driver, website)
        print("This will run only once before the setUp method for the first test")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("This will run only once after the tearDown method for the last test")

    # sequence of test methods in editor can be anything: Execution sequence would be alphabetic
    def test_checkbox_enabled(self):
        element_ledheadlamp = HandleDropDown.driver.find_element_by_name("ledheadlamp")

        # to select the checkbox if not selected
        if not element_ledheadlamp.is_enabled():
            print("checkbox LED Head Lamp is disabled")
        time.sleep(5)
        self.assertFalse(element_ledheadlamp.is_enabled())


if __name__ == "__main__":
    unittest.main()
