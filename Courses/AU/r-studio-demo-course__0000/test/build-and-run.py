import subprocess
import docker
import os

# Path to the external script
build_script_path = "../../../../scripts/build-docker-image.py"  

# Call the external script to build the Docker image
print("Calling the external script to build the Docker image...")
try:
    subprocess.check_call(["python", build_script_path]) # 3 or nah?
except subprocess.CalledProcessError as e:
    print(f"An error occurred while building the image: {e}")
    exit(1)


# Initialize the Docker client
client = docker.from_env()

# Define the image tag
image_tag = "r-demo-course__0000:24-01-01" # TODO: variables to handle name and release. Must be same as in build script.

# Fetch the image to confirm it was built
try:
    image = client.images.get(image_tag)
    print(f"Image built with ID: {image.id}")
except docker.errors.ImageNotFound:
    print(f"Image {image_tag} not found. Ensure the build script tags the image correctly.")
    exit(1)


# Build the image
# print("Building the Docker image...")
# ## TODO: build using the common build script
# image, build_logs = client.images.build(path=".", tag=image_tag)

# Optional: Print build logs if needed
# for log in build_logs:
#     print(log.get("stream", "").strip())

# Fetch the image ID (optional, if you want to use it)
image_id = image.id
print(f"Image built with ID: {image_id}")

# Run the container using the image tag
print("Running the Docker container...")
container = client.containers.run(
    image=image_tag,  # Using the tag directly
    detach=True,      # Run container in the background
    name="r-studio-demo-test",  # Optional: name your container
    ports={'80/tcp': 8080},  # Example: map port 80 inside the container to port 8080 on the host
    environment={"ENV_VAR": "value"},  # Example: pass environment variables
    volumes={"/host/path": {"bind": "/container/path", "mode": "rw"}},  # Example: mount a volume
)

# Output container details
print(f"Container {container.name} is running with ID: {container.id}")