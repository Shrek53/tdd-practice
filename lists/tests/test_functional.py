from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_root_url_has_To_do_in_it(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-do', self.browser.title)
        # self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
