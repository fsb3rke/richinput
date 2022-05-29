import json

class rinput:
    def __init__(self, input_text):
        self.input_text = input_text
        self.input_out = rinput.__inp(self)
    def __inp(self):
        m_input = input(self.input_text)
        rich_content = json.loads(open("rich.json", "r").read())
        emojis = rich_content["emojis"]
        emojis_keyword = [x for x in rich_content["emojis"]]
        for i in emojis_keyword:
            if i in m_input:
                m_input = m_input.replace(f":{i}:", f"{chr(int(emojis[i]))}")
        return m_input

def r_rinput(text):
    return rinput(text).input_out
