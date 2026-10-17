import docker

client = docker.from_env()
container = client.containers.get("flask-apparmor-test")

tests = [
    ("Read /etc/shadow", ["cat", "/etc/shadow"]),
    ("Write to /var", ["sh", "-c", "echo test > /var/apparmor-test.txt"]),
    ("Execute /bin/ls", ["/bin/ls", "/"]),
]

for description, command in tests:
    print("\nTest:", description)
    result = container.exec_run(command)
    print("Exit code:", result.exit_code)
    print(result.output.decode(errors="replace").strip())

print("\nAppArmor is disabled in this environment.")
print("Results do not prove AppArmor enforcement.")
