class Customer:
    def __init__(self,name, terminal, state, zip, agent):
        self.name = name
        self.terminal = terminal
        self.state = state
        self.zip = zip
        self.agent = agent

    def __str__(self):
        return f"Customer Name: {self.name}\nTerminal: {self.terminal}\nState: {self.state}\nZip Code: {self.zip}\nAgent: {self.agent}"