
import unittest

import patternizer


class TestAPI(unittest.TestCase):
    def test_patternize_text(self):
        try:
            patterns = patternizer.patternize_text(
                "Hello world",
            )
            print(patterns)
        except Exception as e:
            self.fail(e)

    def test_patternize_image(self):
        try:
            patterns = patternizer.patternize_image(
                "tests/test_pic.png",
                size=(70, 70)
            )
            print(patterns)
        except Exception as e:
            self.fail(e)