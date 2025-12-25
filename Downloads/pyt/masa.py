# __ str __ method example
class Exploit:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Exploit Loaded → {self.name}"

exp = Exploit("Remote Code Execution")
print(exp)

# __len__ method example
class PayloadList:
    def __init__(self, payloads):
        self.payloads = payloads
    
    def __len__(self):
        return len(self.payloads)

payload_list = PayloadList(["payload1", "payload2", "payload3"])
print(len(payload_list))

# __ contains __ method example
class ScannerReslts:
    def __init__(self, results):
        self.results = results

    def __contains__(self, item):
        return item in self.results
    
scan = ScannerReslts(["vuln1", "vuln2", "vuln3"])
print("vuln2" in scan)


class Pay:
    def __init__(self, code):
        self.code = code


    def __add__(self, other):
        return Pay(self.code + other.code)
    
p1 = Pay("<script>")
p2 = Pay("alert(1)</script>")
p3 = p1 + p2
print(p3.code)

class Exploit:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return Exploit(self.name + " + " + other.name)
    
e1 = Exploit("SQL Injection")
e2 = Exploit("XSS")
e3 = e1 + e2
print(e3.name)

class Payload:
    def __init__(self, code):
        self.code = code
    
    def __eq__(self, other):
        return self.code == other.code

p1 = Payload("<script>alert(1)</script>")
p2 = Payload("<script>alert(1)</script>")
print(p1 == p2)

class  Wordlist:
    def __init__(self, words):
        self.words = words

    def __gt__(self, other):
        return len(self.words) > len(other.words)
    
w1 = Wordlist(["a", "b"])
w2 = Wordlist(["a", "b", "c"])
print(w2 > w1)


