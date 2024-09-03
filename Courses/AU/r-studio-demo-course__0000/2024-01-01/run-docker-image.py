import sys
import os
import subprocess
import docker

if __name__ == "__main__":

    # Define the command with the arguments
    args = [
        "-n", "r-studio-demo-course", # Course name
        "-c", "0000",                 # Course code
        "-r", "2024-01-01",           # Course release
        "-u", "au"                    # University
    ]

    # Define the Docker container's name and port mapping
    CONTAINER_NAME = "COURSE_NAME-test"
    PORT = "8787"
    START_COMMAND = "start_course -s req -c class_01"

    # Initialize the Docker client to interact with Docker from Python
    try:
        client = docker.from_env()
    except Exception as e:
        print(f"Error initializing Docker client: {e}")
        sys.exit(1)  # Exit the script if Docker client cannot be initialized

    # Convert the args list into a dictionary for easy access to values
    try:
        args_dict = dict(zip(args[0::2], args[1::2]))
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        sys.exit(1) # Exit if argument parsing fails
    
    # Construct the image tag using the extracted arguments
    IMAGE_TAG = 'dreg.cloud.sdu.dk/ucloud-courses/{}-{}__{}:{}'.format(
        args_dict["-u"],
        args_dict["-n"].replace(" ", "-"),  # Replace whitespace with dashes
        args_dict["-c"],
        args_dict["-r"]
    )

    # Remove existing container if it exists
    try:
        existing_container = client.containers.get(CONTAINER_NAME)
        existing_container.stop()
        existing_container.remove()
        print(f"Removed existing container: {CONTAINER_NAME}")
    except docker.errors.NotFound:
        print(f"No existing container named '{CONTAINER_NAME}' found.")

    # Print the image tag and run the Docker container
    print(f"Running the Docker container '{CONTAINER_NAME}' from the image '{IMAGE_TAG}'...")
    container = client.containers.run(
        image=IMAGE_TAG,
        name=CONTAINER_NAME,
        ports={"{}/tcp".format(PORT): PORT},    # Remove port mapping if access from host machine or external networks is not required.
        detach=True,                            # Run the container in detached mode.                  
        stdin_open=True,                        # Keep STDIN open.
        tty=True,                               # Allocate a pseudo-TTY.
        command=f"bash -c '{START_COMMAND}'"
    )

    print(f"Container '{CONTAINER_NAME}' is running. You can access it via port {PORT}.")
