import sys
import os
import subprocess
import docker

def build():
    os.chdir("../../../../scripts")
    command = ["python3", "build_docker_image.py", "-n", "r-demo-course", "-c", "0000", "-r", "2024-01-01", "-u", "au"]    # TODO: pass arguments 
    subprocess.run(command, capture_output=False, text=True)
    client = docker.from_env()
    images = client.images.list()
    r_images = [i for i in images if "r-demo-course" in i.tag]
    # image = r_images
    print({r_images})

if __name__ == "__main__":  # Run the Docker container using the newly built image
    build()
    # container_name = "test-rstudio"
    # port_mapping = "8787:8787"
    # start_command = "sudo start_course -s req -c clgaass_01"

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



