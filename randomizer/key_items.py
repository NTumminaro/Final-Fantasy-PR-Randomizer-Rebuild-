import os
import json
from clingo_solve.clingo_solver import run_clingo
from clingo_solve.clingo_key_items import ClingoKeyItem


class KeyItemsRandomizer:
    FLAGS = {
        "lute": 5,
        "crown": 10,
        "crystal_eye": 11,
        "jolt_tonic": 12,
        "mystic_key": 13,
        "nitro_powder": 14,
        "canal": 15,
        "star_ruby": 17,
        "rod": 19,
        "earth_crystal": 21,
        "canoe": 22,
        "fire_crystal": 23,
        "floater": 24,
        "airship": 25,
        "cube": 26,
        "oxyale": 29,
        "slab": 31,
        "learn_lufien": 32,
        "chime": 33,
        "water_crystal": 34,
        "air_crystal": 35,
        "rat_tail": 45,
        "adamantite": 47,
        "excalibur": 48,
    }

    LOCATIONS = {
        "sara": 1,
        "king": 2,
        "bikke": 3,
        "marsh": 4,
        "astos": 5,
        "matoya": 6,
        "elf": 7,
        "locked_cornelia": 8,
        "nerrick": 9,
        "vampire": 11,
        "sarda": 12,
        "ice": 16,
        "citadel_of_trials": 24,
        "fairy": 18,
        "mermaids": 20,
        "lefien": 23,
        "waterfall": 19,
        "sky2": 25,
        "smyth": 10,
        "lich": 13,
        "kary": 15,
        "kraken": 21,
        "tiamat": 26,
        "dr_unne": 22,
    }

    def __init__(self, seed, directory):
        self.seed = seed
        self.directory = directory
        self.ld = []
        self.complete = []

    def write_spoiler_log(self, spoiler_log_path):
        with open(spoiler_log_path, "w", encoding="utf-8") as spoiler_log:
            for loc in self.ld:
                spoiler_log.write(
                    f"Location {loc['location']} -> Key Item {loc['key_item']}\n"
                )

    def run_clingo(self):
        print(f"Running Clingo with seed {self.seed}...")
        data_file = os.path.join("clingo_solve", "KeyItemDataShip.lp")
        solving_file = os.path.join("clingo_solve", "KeyItemSolvingShip.lp")
        clingo_output = run_clingo(data_file, solving_file, self.seed)
        print("Clingo output:", clingo_output)
        return clingo_output

    def parse_clingo_output(self, clingo_output):
        print("Parsing Clingo output...")
        clingo_data = ClingoKeyItem(json.loads(clingo_output))

        for call in clingo_data.call:
            for witness in call.witnesses:
                for value in witness.value:
                    pairs = value.strip("[]").split(", ")
                    for pair in pairs:
                        key_item_str, location_str = (
                            pair.replace("pair(", "").replace(")", "").split(",")
                        )
                        key_item = self.FLAGS.get(key_item_str.strip(), -1)
                        location = self.LOCATIONS.get(location_str.strip(), -1)

                        print(
                            f"Parsed key item: {key_item_str.strip()} -> {key_item}, location: {location_str.strip()} -> {location}"
                        )

                        if key_item != -1 and location != -1:
                            self.ld.append({"key_item": key_item, "location": location})
                            self.complete.append(location)

        print(f"Complete location data: {self.ld}")

    def randomize(self, dest_directory):
        clingo_output = self.run_clingo()
        self.parse_clingo_output(clingo_output)
        self.update_json_files(dest_directory)
        self.write_spoiler_log(os.path.join(dest_directory, "spoiler_log.txt"))

    def update_json_files(self, dest_directory):
        print("Updating JSON files...")
        for loc in self.ld:
            files = self.get_files_for_location(loc["location"])
            for file in files:
                dest_file = file.replace(self.directory, dest_directory)
                print(f"Updating {dest_file} with key item {loc['key_item']}")
                self.json_rewrite(dest_file, loc)

    def get_files_for_location(self, location):
        location_to_files = {
            1: [
                os.path.join(
                    self.directory, "Map_20011", "Map_20011_2", "sc_e_0004_1.json"
                ),
                os.path.join(
                    self.directory, "Map_20011", "Map_20011_2", "sc_e_0004_2.json"
                ),
            ],
            2: [
                os.path.join(
                    self.directory, "Map_20011", "Map_20011_2", "sc_e_0003_3.json"
                )
            ],
            3: [
                os.path.join(
                    self.directory, "Map_20040", "Map_20040", "sc_e_0009_2.json"
                )
            ],
            4: [
                os.path.join(
                    self.directory, "Map_30021", "Map_30021_3", "sc_e_0010_1.json"
                )
            ],
            5: [
                os.path.join(
                    self.directory, "Map_20081", "Map_20081_1", "sc_e_0011_2.json"
                )
            ],
            6: [
                os.path.join(
                    self.directory, "Map_20031", "Map_20031_1", "sc_e_0012.json"
                )
            ],
            7: [
                os.path.join(
                    self.directory, "Map_20071", "Map_20071_1", "sc_e_0013.json"
                )
            ],
            8: [
                os.path.join(
                    self.directory, "Map_20011", "Map_20011_1", "sc_e_0014.json"
                )
            ],
            9: [
                os.path.join(
                    self.directory, "Map_20051", "Map_20051_1", "sc_e_0015.json"
                )
            ],
            10: [
                os.path.join(
                    self.directory, "Map_20051", "Map_20051_1", "sc_e_0052.json"
                )
            ],
            11: [
                os.path.join(
                    self.directory, "Map_30031", "Map_30031_3", "sc_e_0017.json"
                )
            ],
            12: [
                os.path.join(
                    self.directory, "Map_20101", "Map_20101_1", "sc_e_0019.json"
                )
            ],
            13: [
                os.path.join(
                    self.directory, "Map_30031", "Map_30031_5", "sc_e_0021_2.json"
                )
            ],
            14: [
                os.path.join(self.directory, "Map_20110", "Map_20110", "sc_e_0022.json")
            ],
            15: [
                os.path.join(
                    self.directory, "Map_30051", "Map_30051_6", "sc_e_0023_2.json"
                )
            ],
            16: [
                os.path.join(
                    self.directory, "Map_30061", "Map_30061_4", "sc_e_0024_2.json"
                )
            ],
            17: [
                os.path.join(
                    self.directory, "Map_10010", "Map_10010", "sc_e_0025_4.json"
                )
            ],
            18: [
                os.path.join(self.directory, "Map_20150", "Map_20150", "sc_e_0029.json")
            ],
            19: [
                os.path.join(
                    self.directory, "Map_30091", "Map_30091_1", "sc_e_0026.json"
                )
            ],
            20: [
                os.path.join(
                    self.directory, "Map_30081", "Map_30081_8", "sc_e_0033.json"
                )
            ],
            21: [
                os.path.join(
                    self.directory, "Map_30081", "Map_30081_1", "sc_e_0036_2.json"
                )
            ],
            22: [
                os.path.join(self.directory, "Map_20090", "Map_20090", "sc_e_0034.json")
            ],
            23: [
                os.path.join(self.directory, "Map_20160", "Map_20160", "sc_e_0035.json")
            ],
            24: [
                os.path.join(
                    self.directory, "Map_30071", "Map_30071_3", "sc_e_0047.json"
                )
            ],
            25: [
                os.path.join(
                    self.directory, "Map_30111", "Map_30111_2", "sc_e_0051.json"
                )
            ],
            26: [
                os.path.join(
                    self.directory, "Map_30111", "Map_30111_5", "sc_e_0037_2.json"
                )
            ],
        }
        return location_to_files.get(location, [])

    def json_rewrite(self, file_name, loc):
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        for script in data["Mnemonics"]:
            if script["mnemonic"] == "MsgFunfare":
                script["operands"]["sValues"][0] = "MSG_KEY_" + (
                    str(loc["key_item"]) if loc["key_item"] > 0 else "A1"
                )
            if (
                script["mnemonic"] == "GetItem"
                and script["operands"]["iValues"][1] >= 0
            ):
                key_item = self.get_key_item_value(loc["key_item"])
                script["operands"]["iValues"][0] = key_item
                script["operands"]["iValues"][1] = 0 if key_item == 2 else 1
            if (
                script["mnemonic"] == "SetFlag"
                and script["operands"]["iValues"][0] < 100
                and script["operands"]["sValues"][0] == "ScenarioFlag1"
            ):
                script["operands"]["iValues"][0] = (
                    loc["key_item"] if loc["key_item"] > 0 else 0
                )

        print(f"Rewriting file: {file_name} with location data: {loc}")

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def get_key_item_value(self, key_item):
        key_item_mapping = {
            5: 45,  # lute
            10: 46,  # crown
            11: 47,  # crystal eye
            12: 48,  # jolt tonic
            13: 49,  # mystic key
            14: 50,  # nitro powder
            17: 53,  # star ruby
            19: 54,  # rod
            21: 55,  # floater
            22: 56,  # chime
            23: 57,  # cube
            29: 60,  # oxyale
            31: 62,  # slab
            32: 63,  # learn lufuin
            33: 64,  # earth crystal
            34: 65,  # fire crystal
            35: 66,  # water crystal
            45: 57,  # rat tail
            47: 51,  # adamantite
            48: 92,  # excalibur
        }
        return key_item_mapping.get(key_item, 2)


# Example usage
if __name__ == "__main__":
    import random

    random.seed(12345)
    seed = random.randint(0, 1000000)
    directory = "resources/maps"
    tempmods_directory = "tempmods"

    key_item_randomizer = KeyItemsRandomizer(seed, directory)
    key_item_randomizer.randomize(tempmods_directory)
    print(
        f"Randomization complete. Check the {tempmods_directory} directory for results."
    )
