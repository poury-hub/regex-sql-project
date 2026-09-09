import regex as re 



class Extracting:

    def __init__(self, name):
        self.name = name
        with open(name, 'r') as f:
            self.data = f.read()    


    def IPs(self) -> list[str]:
        pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')       
        return pattern.findall(self.data)

    def Day(self) -> list[str]:
        pattern = re.compile(r'(?<=\[)(\d{2})(?=/)')
        
        return pattern.findall(self.data)

    def Month(self) -> list[str]:
        #pattern = re.compile(r'(?<=\[)(\d{2})/([A-Za-z]{3})(?=/)')
        pattern = re.compile(r'(?<=\[\d{2}/)([A-Za-z]{3})(?=/)')
        return pattern.findall(self.data)

    def Year(self) -> list[str]:
        pattern = re.compile(r'(?<=\[\d{2}/[A-Za-z]{3}/)(\d{4})(?=:)')
        return pattern.findall(self.data)

    def Time(self) -> list[tuple[str , str , str]]:
        pattern = re.compile(r'(?<=\d{4}:)(\d{2}):(\d{2}):(\d{2})(?=\s)')
        return pattern.findall(self.data)

    def Timezone(self) -> list[str]:
        pattern = re.compile(r'(?<=:\d{2}:\d{2}:\d{2}\s)([+-]\d{4})(?=\])')
        return pattern.findall(self.data)

    def Re(self) -> list[str]:
        pattern = re.compile(r'(?<=]\s")(.+)(?="\s\d{3})')
        return pattern.findall(self.data)

    def Request(self) -> list[tuple[str , str , str]]:
        output: list[tuple[str , str , str]] = []

        for line in self.Re():
            method = re.search(r'^(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)', line)
            path = re.search(r'(?<=GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s(/\S+)(?=\s)', line)
            protocol = re.search(r'(?<=HTTP/)(\d+\.\d+)', line)
            
            if(method and path and protocol):
                i = (method.group(1) , path.group(1) , protocol.group(1))
                output.append(i)
            else:
                i = (" " , " " , " ")
                output.append(i)
    
        return output

        


va = Extracting("access.log")
va.Timezone()
va.Time()
va.Request()     
# print(path)