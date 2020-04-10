# This file contains paths to important dirs

from pathlib import Path
import os

# TODO use glob to find package_dir
package_dir = Path(os.path.abspath('.'))
docker_base_path = package_dir / "docker_base"
saved_images_path = package_dir / "saved_images"
saved_data_path = package_dir / "saved_data"
