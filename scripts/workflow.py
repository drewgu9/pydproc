# import dependencies
from pathlib import Path
import yaml
import os
import shutil
import docker

# non-dependency imports
from definitions import docker_base_path, saved_images_path, saved_data_path

# load client for docker. This requires user set env variables $DOCKER_USERNAME and $DOCKER_PASSWORD
client = docker.from_env()
# Maps image name to containers running it
containers = {}

def make_docker_dir(specs):
    new_image_path = saved_images_path / specs['proc_name']
    if new_image_path.exists():
        shutil.rmtree(new_image_path)

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


def fromyml(spec_file: str):
    """
    Build docker image from yml file as input

    :param spec_file: path to spec file
    :return:
    """
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

    # Build and tag new docker image
    build_pathway = os.path.abspath(saved_images_path / specs['proc_name'])
    client.images.build(path=build_pathway, tag=f"pydproc/{specs['proc_name']}")
                        
    # os.system("docker build -t pydproc/weather " + build_pathway)

def start(proc_name: str):
    """
    Start docker container and mounts saved_data folder

    :param proc_name: name of image in pydproc repo
    """
    image_name = f'pydproc/{proc_name}:latest'
    if not image_name in [i.tags[0] for i in client.images.list() if len(i.tags) > 0]:
        print(f'ERROR: pydproc/{proc_name} docker image has not been built yet.')
        return

    if not proc_name in containers.keys():
        containers[proc_name] = []

    run_name = f'{proc_name}-{len(containers[proc_name])}'
    new_save_dir = saved_data_path / run_name
    os.mkdir(new_save_dir)

    print(f'Starting new run {run_name}')
    container = client.containers.run(image_name, 'python run_proc.py',
        volumes={str(new_save_dir): {'bind': '/saved_data', 'mode': 'rw'}}, stream=True, detach=True, remove=True)
     # os.system("docker run --rm -v $PWD/saved_data:/workdir/saved_data pydproc_weather")
                        
    # Save logs
    with open(new_save_dir / (run_name + ".log"), "w+") as log_file:
        log_file.write(str(container.logs()))

    containers[proc_name].append({run_name: container})

def stop(run_name):
    # TODO parse run_name for proc_name
    # TODO stop the container in containers[proc_name][run_name]
    pass

def restart(run_name):
    # TODO parse run_name for proc_name
    # TODO stop the container in containers[proc_name][run_name]
    pass

def get_data(run_name, destination):
    # TODO search saved_data_path for run_name and shutil.copytree() it to destination
    pass


if __name__ == "__main__":
    # TODO Uncomment this for when we create cli
    # globals()[sys.argv[1]]()

    fromyml("./examples/weather.yml")
    start("weather")

