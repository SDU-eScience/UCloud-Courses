import sys
import os
import subprocess
import docker

def build():

    # Change to scripts directory
    os.chdir("../../../../scripts")

    # Define the command with the arguments
    command = [
        "python3", "build-docker-image.py",
        "-n", "nlp-demo-course", # Course name
        "-c", "0000",                   # Course code
        "-r", "2024-01-01",             # Course release
        "-u", "au"                      # University
    ]

    # Execute the command to build the Docker image
    subprocess.run(command, capture_output=False, text=True)

    # Return the command list for later use in the run function
    return command

def run(command):

    # Define the Docker container's name and port mapping
    CONTAINER_NAME = "test-nlp"
    PORT = "8888"
    START_COMMAND = "sudo start_course -c class_01 -a true"

    # Initialize the Docker client to interact with Docker from Python
    client = docker.from_env()

    # Extract the arguments from the command list
    args = dict(zip(command[2::2], command[3::2]))
    
    # Construct the image tag using the extracted arguments
    IMAGE_TAG = 'dreg.cloud.sdu.dk/ucloud-courses/{}-{}__{}:{}'.format(
        args["-u"],
        args["-n"].replace(" ", "-"),  # replace whitespace with dash
        args["-c"],
        args["-r"]
    )

    # Print the image tag and run the Docker container
    print(f"Running the Docker container '{CONTAINER_NAME}' from the image '{IMAGE_TAG}'...")
    container = client.containers.run(
        image=IMAGE_TAG,
        name=CONTAINER_NAME,
        ports={"{}/tcp".format(PORT): PORT},
        detach=True,                            # Run the container in detached mode.                  
        tty=True,                               # Enable container terminal.
        command=f"bash -c '{START_COMMAND}'"
    )

    print(f"Container '{CONTAINER_NAME}' is running. You can access it via port 8787.")

if __name__ == "__main__":
    
    # Build image and retrieve the command list
    command = build()

    # Pass command list and start the container
    run(command)
