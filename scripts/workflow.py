from pathlib import Path
import yaml
import os
import shutil


def make_docker_dir(specs):
    docker_base_path = os.path.abspath("../docker_base")
    new_image_path = Path(os.path.abspath(f"../saved_images/{specs['proc_name']}"))

    shutil.copytree(docker_base_path, new_image_path)

    with open(new_image_path / "proc.yml") as f:
        f.write(yaml.dump(specs))

    return


def start_workflow(spec_file):
    spec_file = Path(os.path.abspath(spec_file))

    # Check if spec file exists
    if not spec_file.exists():
        raise FileNotFoundError(f"No file found at {spec_file}")

    # Load and process spec_file
    with open(spec_file, "r+") as f:
        specs = yaml.safe_load(f)
        if not "proc_name" in specs: specs["proc_name"] = os.path.basename(spec_file).strip(".yml")

    # Make new docker dir
    make_docker_dir(specs)

    return

if __name__ == "__main__":
    start_workflow("../examples/weather.yml")
