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

def get_subdomains(domain):
    subfinder = run_command(
        f"subfinder -d {domain} -silent"
    )

    assetfinder = run_command(
        f"assetfinder --subs-only {domain}"
    )

    return list(set(subfinder + assetfinder))
    

