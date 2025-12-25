from abc import ABC, abstractmethod

# Base classes
class Scanner(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def scan(self):
        pass


class Exploit(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def run(self):
        pass


class Payload(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass


class Reporter(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def report(self, data):
        pass


# Subclasses
class PortScanner(Scanner):
    def __init__(self):
        super().__init__("Port Scanner")

    def scan(self):
        print(f"[{self.name}] Scanning ports...")


class SQLiExploit(Exploit):
    def __init__(self):
        super().__init__("SQLi Exploit")

    def run(self):
        print(f"[{self.name}] Running SQL Injection exploit...")


class ReverseShellPayload(Payload):
    def __init__(self):
        super().__init__("Reverse Shell Payload")

    def execute(self):
        print(f"[{self.name}] Spawning reverse shell...")


class ConsoleReporter(Reporter):
    def __init__(self):
        super().__init__("Console Reporter")

    def report(self, data):
        print(f"[{self.name}] REPORT: {data}")


# Pentest Manager
class PentestManager:
    def __init__(self, scanner, exploit, payload, reporter):
        self.scanner = scanner
        self.exploit = exploit
        self.payload = payload
        self.reporter = reporter

    def run(self):
        self.scanner.scan()
        self.exploit.run()
        self.payload.execute()
        self.reporter.report("Pentest completed successfully")


# Usage
scanner = PortScanner()
exploit = SQLiExploit()
payload = ReverseShellPayload()
reporter = ConsoleReporter()

manager = PentestManager(scanner, exploit, payload, reporter)
manager.run()