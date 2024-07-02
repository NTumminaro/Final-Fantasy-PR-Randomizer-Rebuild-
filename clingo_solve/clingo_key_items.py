class ClingoKeyItem:
    def __init__(self, json_data):
        self.solver = json_data.get("Solver")
        self.input = json_data.get("Input", [])
        self.call = [Call1(call) for call in json_data["Call"]]
        self.result = json_data.get("Result")
        self.models = Models1(json_data["Models"])
        self.calls = json_data.get("Calls")
        self.time = Time1(json_data["Time"])

class Models1:
    def __init__(self, data):
        self.number = data["Number"]
        self.more = data["More"]

class Time1:
    def __init__(self, data):
        self.total = data["Total"]
        self.solve = data["Solve"]
        self.model = data["Model"]
        self.unsat = data["Unsat"]
        self.cpu = data["CPU"]

class Call1:
    def __init__(self, data):
        self.witnesses = [Witness(witness) for witness in data["Witnesses"]]

class Witness:
    def __init__(self, data):
        self.value = data["Value"]
