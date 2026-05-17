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
    print("[+] RUNNING GAU...")
    gau_urls = run_command(
        f"gau {domain}")

    print("[+] RUNNING WAYBACKURLS...")
    wayback_urls = run_command(
        f"waybackurls {domain}")

    print("[+] RUNNING KATANA...")
    katana_urls = run_command(
        f"katana -u https://{domain} -silent -d 2 -c 20")

    
    all_urls = list(
        set(
            gau_urls +
            wayback_urls +
            katana_urls ))
    return all_urls
