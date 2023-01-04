import unittest
from morseTranslator import Morse

class TestTextToMorseTranslation(unittest.TestCase):

    def testTranslationWithEmptyInput(self):
        textToMorse = Morse("")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), "")

    def testTranslationWithOneWord(self):
        textToMorse = Morse("abc")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), ".- -... -.-.")

    def testTranslationWithTwoWords(self):
        textToMorse = Morse("abc abc")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), ".- -... -.-. / .- -... -.-.")

    def testTranslationWithCaps(self):
        textToMorse = Morse("AbC aBc")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), ".- -... -.-. / .- -... -.-.")

    def testTranslationOnlyWithNumbers(self):
        textToMorse = Morse("123")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), ".---- ..--- ...--")

    def testTranslationWithLettersAndNumbers(self):
        textToMorse = Morse("a1 B2 c3")
        textToMorse.translate()
        self.assertEqual(textToMorse.getTranslationResult(), ".- .---- / -... ..--- / -.-. ...--")

if __name__ == '__main__':
    unittest.main()
