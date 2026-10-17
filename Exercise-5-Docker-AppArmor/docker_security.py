
import docker

client = docker.from_env()
container_name = "flask-apparmor-test"

try:
    container = client.containers.get(container_name)

    print("Container found:", container.name)
    print("Container status:", container.status)
    print("Image:", container.image.tags)

    apparmor_status = container.attrs.get("AppArmorProfile", "")
    print("Applied AppArmor profile:", apparmor_status or "Not reported")

    if not apparmor_status or apparmor_status == "unconfined":
        print("WARNING: No custom AppArmor profile is reported.")
        print("AppArmor enforcement must be verified on a supported Linux host.")
    else:
        print("A profile is reported; verify enforcement on the host.")

except docker.errors.NotFound:
    print("Container not found:", container_name)
except docker.errors.DockerException as error:
    print("Docker SDK error:", error)
