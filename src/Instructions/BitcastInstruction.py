class BitcastInstruction:

    def __init__(self, og_type, value, new_type, result):
        self.og_type = og_type
        self.value = value
        self.new_type = new_type
        self.result = result

    def to_text(self):
        return f"{self.result} = bitcast {self.og_type} " \
               f"{self.value} to %struct.{self.new_type}*"

    def to_value(self):
        return f"{self.result}"

