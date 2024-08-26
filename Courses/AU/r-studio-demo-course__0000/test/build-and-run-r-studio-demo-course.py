import sys
import os
import subprocess
import docker
from pprint import pprint
import inspect

def build():
    imageId = "dreg.cloud.sdu.dk/ucloud-courses/au-r-studio-demo-course__0000:2024-01-01"
    client = docker.from_env()
    client.images.remove(imageId)
    os.chdir("../../../../scripts")
    command = ["python3", "build_docker_image.py", "-n", "r-studio-demo-course", "-c", "0000", "-r", "2024-01-01", "-u", "au"]
    subprocess.run(command, capture_output=False, text=True)
    
    client.containers.run(imageId)
    # images = client.images.list()
    # r_images = list(filter(lambda i: "r-studio-demo-course" in i.tag, images))
    # r_images = list(filter(lambda i: "r-studio-demo-course" in i.tag, images))
    # image = r_images
    # print({r_images.__dict__})
    # for i in images:
    #     pprint(inspect.getmembers(i))
    # pprint(inspect.getmembers(r_images))

if __name__ == "__main__":  # Run the Docker container using the newly built image
    build()
    # container_name = "test-rstudio"
    # port_mapping = "8787:8787"
    # start_command = "sudo start_course -s req -c class_01"

    # print(f"Running the Docker container '{container_name}' from the image '{image_tag}'...")
    # container = client.containers.run(
    #     image=image_tag,
    #     name=container_name,
    #     ports={"8787/tcp": 8787},
    #     detach=True,
    #     tty=True,
    #     command=f"bash -c '{start_command}'"
    # )

    # print(f"Container '{container_name}' is running. You can access it via port 8787.")
    # run()


