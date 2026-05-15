import subprocess

def run_command(command):
    try:
        result = subprocess.check_output(
            command,
            shell = True,
            text = True
        )
        return result.splitlines()
    except:
        return []

def get_urls(domain):
    return run_command(
        f"gau {domain}"
    ) 
