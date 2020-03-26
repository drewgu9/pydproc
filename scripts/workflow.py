from pathlib import Path
import yaml
import os
import shutil


def make_docker_dir(specs):
    docker_base_path = os.path.abspath("../docker_base")
    new_image_path = Path(os.path.abspath(f"../saved_images/{specs['proc_name']}"))

    # Copy docker dir template
    shutil.copytree(docker_base_path, new_image_path)

    # Overwrite proc.yml
    with open(new_image_path / "proc.yml", "w+") as f:
        f.write(yaml.dump(specs))

    # Rewrite build and run scripts
    with open(new_image_path / "build.sh", "r+") as f:
        build_script = f.read().format(IMAGE_NAME=specs['proc_name'])
    with open(new_image_path / "build.sh", "w") as f:
        f.write(build_script)

    with open(new_image_path / "run.sh", "r+") as f:
        run_script = f.read().format(IMAGE_NAME=specs['proc_name'])
    with open(new_image_path / "run.sh", "w") as f:
        f.write(run_script)


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
