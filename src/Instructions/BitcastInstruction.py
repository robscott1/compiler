class BitcastInstruction:

    def __init__(self, og_type, value, new_type, result):
        self.og_type = og_type
        self.value = value
        self.new_type = new_type
        self.result = result

    def to_text(self):
        new_type = self.new_type.to_text() if not \
            isinstance(self.new_type, str) else self.new_type
        og_type = self.og_type.cast_up().to_text() if not \
            isinstance(self.og_type, str) else self.og_type

        return f"{self.result} = bitcast {og_type} " \
               f"{self.value} to {new_type}"

    def to_value(self):
        return f"{self.result}"

