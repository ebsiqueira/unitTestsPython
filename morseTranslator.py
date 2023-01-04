class Morse:
    def __init__(self, text):
        self.morseChar = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "/"
        }
        self.input = text.lower()
        self.translationResult = ""

    def getInput(self):
        return self.getInput

    def getMorseChar(self):
        return self.morseChar

    def getTranslationResult(self):
        return self.translationResult

    def checkEndOfInput(self, it):
        if(it != (len(self.input)-1)):
            self.translationResult += " "

    def translate(self):
        for it in range(0, len(self.input)):
            if(self.input[it] in self.morseChar):
                self.translationResult += self.morseChar[self.input[it]]
                self.checkEndOfInput(it)