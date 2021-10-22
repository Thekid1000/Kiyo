# tokens are necessary in order to use the data Value

kiyo_int = "kiyo_int"
kiyo_float = "float"
kiyo_add = "PLUS"
kiyo_minus = "MINUS"
kiyo_multiply = "MULTIPLY"
kiyo_div = "DIVIDE"
kiyo_LPAREN = "LPAREN"
kiyo_RPAREN = "RPAREN"


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        return f"{self.type}"

# Making a Lexar


class Lexar:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(
            self.text) else None

    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(kiyo_add))
                self.advance()
        return tokens
