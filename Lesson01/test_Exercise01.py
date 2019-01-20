import Exercise01

def test_replacer():
    assert Exercise01.replacer("lightz buzz") == "lights buss"

def test_numberToWord():
    assert Exercise01.numberToWord(1) == "one"
    assert Exercise01.numberToWord("1") == "one"
    assert Exercise01.numberToWord(9) == "nine"
    assert Exercise01.numberToWord("9") == "nine"
    assert Exercise01.numberToWord(10) == "ten"
    assert Exercise01.numberToWord("10") == "ten"
    assert Exercise01.numberToWord(0) == None
    assert Exercise01.numberToWord(11) == None
    assert Exercise01.numberToWord("abc") == None

def test_captilizeAll():
    assert Exercise01.captilizeAll("word") == "Word"
    assert Exercise01.captilizeAll("word other") == "Word Other"
    assert Exercise01.captilizeAll("This is a longer sentence.") == "This Is A Longer Sentence."

def test_countWords():
    assert Exercise01.countWords("word") == 1
    assert Exercise01.countWords("word other") == 2
    assert Exercise01.countWords("This is a longer sentence.") == 5
