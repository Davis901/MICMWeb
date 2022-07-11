keywords = Element("keywords")
result = Element("result")

def play_game(*args):
    user_input = keywords.value
    result.element.innerText = "Round trip successful"
keywords.clear()