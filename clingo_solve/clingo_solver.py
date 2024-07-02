import clingo
import json


def run_clingo(data_file, solving_file, seed):
    control = clingo.Control(arguments=["--seed", str(seed)])
    control.load(data_file)
    control.load(solving_file)
    control.ground([("base", [])])
    result = []

    def on_model(model):
        result.extend(model.symbols(shown=True))

    control.solve(on_model=on_model)

    # Convert the result to a string format that can be loaded as JSON
    output = {
        "Solver": "clingo",
        "Input": [],
        "Call": [{"Witnesses": [{"Value": [str(symbol) for symbol in result]}]}],
        "Result": "SAT",
        "Models": {"Number": 1, "More": "yes"},
        "Calls": 1,
        "Time": {"Total": 0.0, "Solve": 0.0, "Model": 0.0, "Unsat": 0.0, "CPU": 0.0},
    }

    return json.dumps(output)
