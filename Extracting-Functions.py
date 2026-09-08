import regex as re 


class Extracting:

    def __init__(self, name):
        self.name = name
        with open(name, 'r') as f:
            self.data = f.read()    


    def IPs(self):
        pattern = r'\d+\.\d+\.\d+\.\d+'       
        return re.findall(pattern, self.data)

    def Day(self):
        pattern = r'(?<=\)\d{2}(?=/)'
        return re.findall(pattern, self.data)

    def Month(self):
        pattern = r'(?<=/)(?=/)'
        return re.findall(pattern, self.data)