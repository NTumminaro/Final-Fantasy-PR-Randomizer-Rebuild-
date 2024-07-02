import os
import shutil
import random
from randomizer.key_items import KeyItemsRandomizer  # Ensure this import is correct


def setup_tempmods_directory(tempmods_path):
    if os.path.exists(tempmods_path):
        shutil.rmtree(tempmods_path)
    os.makedirs(tempmods_path)


def copy_files_to_tempmods(src_directory, dest_directory):
    if not os.path.exists(dest_directory):
        os.makedirs(dest_directory)

    for root, dirs, files in os.walk(src_directory):
        for file in files:
            src_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(src_file_path, src_directory)
            dest_file_path = os.path.join(dest_directory, relative_path)

            dest_file_dir = os.path.dirname(dest_file_path)
            if not os.path.exists(dest_file_dir):
                os.makedirs(dest_file_dir)

            shutil.copy2(src_file_path, dest_file_path)


if __name__ == "__main__":
    # Seed for reproducibility
    random.seed(12345)
    seed = random.randint(0, 1000000)

    # Define directories
    maps_directory = "resources/maps"
    tempmods_directory = "tempmods"
    spoiler_log_path = os.path.join(tempmods_directory, "spoiler_log.txt")

    # Setup tempmods directory
    setup_tempmods_directory(tempmods_directory)

    # Copy files to tempmods directory
    copy_files_to_tempmods(maps_directory, tempmods_directory)

    # Initialize the key item randomizer
    key_item_randomizer = KeyItemsRandomizer(seed, maps_directory)

    # Run the randomization, targeting the tempmods directory
    key_item_randomizer.randomize(tempmods_directory)

    # Write the spoiler log
    key_item_randomizer.write_spoiler_log(spoiler_log_path)

    print(
        f"Randomization complete. Check the {tempmods_directory} directory for results."
    )
    print(f"Spoiler log written to {spoiler_log_path}")
