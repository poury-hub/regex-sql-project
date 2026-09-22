import regex as re 
import sqlite3 as sql


class Extracting:


    


    def __init__(self, name):
        self.name = name
        with open(name, 'r') as f:
            self.data = f.read()

        conn = sql.connect(f'{self.name}.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE log_data
                     IP TEXT,
                     Day INTEGER,
                     Month TEXT,
                     Year ,
                     Hour INTEGER,
                     Minute INTEGER,
                     Second INTEGER,
                     Timezone TEXT,
                     Method TEXT,
                     Path TEXT,
                     Protocol TEXT,
                     Status INTEGER,
                     Size INTEGER,
                     Referrer TEXT)''')


        lines = self.data.splitlines()
        for line in lines:
            self.line = line
            c.execute(f"INSERT INTO log_data (IP) VALUES (?)",(self.IPs() if self.IPs() else None,))
            c.execute('''UPDATE log_data SET Day = ? WHERE IP = ?''', (self.Day() if self.Day() else None, self.IPs() if self.IPs() else None))
            self.Day()
            self.Month()
            self.Year()
            self.Time()
            self.Timezone()
            self.Re()
            self.Request()
            self.SZ()
            self.Referrer()

    self.PIP = re.compile(r'\d+\.\d+\.\d+\.\d+')
    self.PDay = re.compile(r'(?<=\[)(\d{2})(?=/)')
    self.PMonth = re.compile(r'(?<=\[\d{2}/)([A-Za-z]{3})(?=/)')
    self.PYear = re.compile(r'(?<=\[\d{2}/[A-Za-z]{3}/)(\d{4})(?=:)')
    self.PTime = re.compile(r'(?<=\d{4}:)(\d{2}):(\d{2}):(\d{2})(?=\s)')
    self.PTimezone = re.compile(r'(?<=:\d{2}:\d{2}:\d{2}\s)([+-]\d{4})(?=\])')
    self.PReferrer = re.compile(r'(?<="\s\d{3}\s\d+\s")(.+)(?="\s")')

    def IPs(self) -> str:
        M = re.search(self.PIP, self.line)
        if(M):
            return M.group(1)
        else:
            return(None)

    def Day(self) -> str:
        M = re.search(self.PDay, self.line)

        if(M):
            return M.group(1)
        else:
            return(None)

    def Month(self) -> str:
        M = re.search(self.PMonth, self.line)

        if(M):
            return M.group(1)
        else:
            return(None)

    def Year(self) -> str:
        M = re.search(self.PYear, self.line)

        if(M):
            return M.group(1)
        else:
            return(None)

    def Time(self) -> tuple[str , str , str]:
        M = re.search(self.PTime, self.line)

        if(M):
            return (M.group(1), M.group(2), M.group(3))
        else:
            return(None)


    def Timezone(self) -> str:
        M = re.search(self.PTimezone, self.line)

        if(M):
            return M.group(1)
        else:
            return(None)

    def Re(self) -> str:
        pattern = re.compile(r'(?<=]\s")(.+)(?="\s\d{3})')
        M = re.search(pattern, self.line)

        if(M):
            return M.group(1)
        else:
            return(False)

    def Request(self) -> tuple[str , str , str]:
        if(self.Re()):
            line = self.Re()
            method = re.search(r'^(GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)', line)
            path = re.search(r'(?<=GET|POST|PUT|DELETE|PATCH|OPTIONS|HEAD)\s(/\S+)(?=\s)', line)
            protocol = re.search(r'(HTTP/\d+\.\d+)', line)
                
            return (
            method.group(1) if method else method,
            path.group(1) if path else path,
            protocol.group(1) if protocol else protocol)

        else:
            return(None)

    def SZ(self) -> tuple[str , str]: #status and size
        M = re.search(self.PSZ, self.line)

        if(M):
            return (M.group(1), M.group(2))
        else:
            return(None)
    
    def Referrer(self) -> str:
        M = re.search(self.PReferrer, self.line)

        if(M):
            return M.group(1)
        else:
            return(None)

        


va = Extracting("access.log")
va.Timezone()
va.Time()
va.Referrer()     
print(va.Referrer() )