def mult(a, b=3):
    return a * b

print(mult(4))
print(mult(4, 5))

def port_scanner(*ports):
    for p in ports:
        print(f"Scanning port {p}")

port_scanner(80, 20, 10)

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))


class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        

    def info(self):
        print(self.brand, self.ram, self.storage)

specs = Laptop("Lenovo", "12gb", "500TB")
specs.info()


class XSSPayload:
    def __init__(self, code):
        self.code = code

    def fire(self):
        print(f"Firing XSS Payload: {self.code}")

payload = XSSPayload("<img src='x' onerror=alert(1)")
payload.fire()


class Device:
    def power_on(self):
        print("Device powering on")

class phone(Device):
    pass
ob = phone()
ob.power_on()





class Exploit:
    def run(self):
        print("Running generic exploit")

start = Exploit()
start.run()

class SQLiExplot(Exploit):
    pass

sql = SQLiExplot()
sql.run()


class Payload:
    def execute(self):
        print("Executing generic payload")

class ReverseShellPayload(Payload):
    def execute(self):
        print("Opening reverse shell")

payload = ReverseShellPayload()
payload.execute()


class Account:
    def __init__(self, pin):
        self._pin = 1234  # Private attribute
    
    def show_pin(self):
        return self._pin

class Vault:
    def __init__(self, code):
        self.__code = "TOP-SECRET"
    
    def reveal(self):
        return self.__code


class Hasher:
    @staticmethod
    def hash(sha256, text):
        print(f"Hashing {text}")

# Hasher.hash("sha256", "Hello World")

class Scanner:
    def scan(self):
        pass

class PortScanner(Scanner):
    def scan(self):
        print("Scanning ports...")

port_scanner = PortScanner()
port_scanner.scan()

class VulnScanner(Scanner):
    def scan(self):
        print("Scanning for vulnerabilities...")

vuln_scanner = VulnScanner()
vuln_scanner.scan()

class NetworkScanner(Scanner):
    def scan(self):
        print("Scanning network...")

network_scanner = NetworkScanner()
network_scanner.scan()

all = [port_scanner, vuln_scanner, network_scanner]
for scanner in all:
    scanner.scan()

from abc import ABC, abstractmethod
class Exploit(ABC):
    @abstractmethod
    def run(self):
        pass
class BufferOverflow(Exploit):
    def run(self):
        print("Overflowing buffer...")
    
run_buffer = BufferOverflow()
run_buffer.run()


class RCE(Exploit):
    def run(self):
        print("Running remote code execution exploit...")


run_rce = RCE()
run_rce.run()


