import paramiko

def get_user_input():
    # Get region selection
    region = input("Select the region (regional/global): ").strip().lower()
    if region not in ["regional", "global"]:
        raise ValueError("Invalid region. Please select 'regional' or 'global'.")

    # Get environment selection
    environment = input("Select the environment (dev/stage/prod): ").strip().lower()
    if environment not in ["dev", "stage", "prod"]:
        raise ValueError("Invalid environment. Please select 'dev', 'stage', or 'prod'.")

    return region, environment

def construct_filepath(region, environment):
    return f"/path/to/{region}/{environment}"

def change_directory_via_ssh(filepath):
    hostname = 'your.remote.server'  # Replace with your server
    username = 'your_username'        # Replace with your username
    password = 'your_password'        # Replace with your password

    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        client.connect(hostname, username=username, password=password)

        # Change directory command
        command = f"cd {filepath} && pwd"
        stdin, stdout, stderr = client.exec_command(command)

        # Output the result
        print(stdout.read().decode())
        print(stderr.read().decode())
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    try:
        region, environment = get_user_input()
        filepath = construct_filepath(region, environment)
        change_directory_via_ssh(filepath)
    except Exception as e:
        print(f"Error: {e}")
