import json
from recon.prioritize import prioritize_params
from recon.params import extract_params
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore,init
from recon.subdomains import get_subdomains
from recon.urls import get_urls
from recon.filters import filter_urls
import time
from recon.status import check_status
import os
os.makedirs("output", exist_ok=True)

init()

def main():
    banner = r"""

    ███╗   ██╗ █████╗ ███╗   ██╗ ██████╗
    ████╗  ██║██╔══██╗████╗  ██║██╔═══██╗
    ██╔██╗ ██║███████║██╔██╗ ██║██║   ██║
    ██║╚██╗██║██╔══██║██║╚██╗██║██║   ██║
    ██║ ╚████║██║  ██║██║ ╚████║╚██████╔╝
    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝

        Nano Recon Framework
"""

    print(Fore.CYAN + banner)   
    
    domain = input(Fore.YELLOW + "ENTER DOMAIN NAME:")
    start = time.time()
    subdomains = get_subdomains(domain)
    print(Fore.GREEN + f"[+] FOUND {len(subdomains)} SUBDOMAINS")

    urls = get_urls(domain)
    print (Fore.GREEN + f"[+] FOUND {len(urls)} URLS")

    interesting_urls = filter_urls(urls)
    print(Fore.GREEN + f"[+] FOUND {len(interesting_urls)} INTERESTING URLS")

    interesting_params = extract_params(interesting_urls)
    print(Fore.GREEN + f" FOUND {len(interesting_params)} INTERESTING PARAMETERS")

    risky_params = prioritize_params(interesting_params)
    print(Fore.RED + f"FOUND {len(risky_params)} RISKY PARAMETERS")

    with open(
        "output/interesting_urls.txt",
        "w"
    ) as f:
        for url in interesting_urls:
            f.write(url + "\n")
    

    print(Fore.CYAN + "[+] FINDING INTERESTING STATUS CODE")
    live_urls =  []
    results = []    

    with ThreadPoolExecutor(max_workers=50) as executor:
        future_map ={
            executor.submit(check_status, url): url
            for url in interesting_urls
        }
        for future in as_completed(future_map):
            url = future_map[future]
            try:
                result = future.result()
                if not result:
                    continue
                result["risky"] =  result["url"] in risky_params
                results.append(result)
                interesting_status = [200,301,302,401,403,500]
                if result["status"] not in interesting_status:
                    continue        
                if result["status"] ==200:
                    color = Fore.GREEN
                elif result ["status"] == 403:
                    color = Fore.YELLOW
                elif result ["status"] == 500:
                    color = Fore.RED
                else :
                    color = Fore.CYAN
                print (color +
                    f'{result["url"]} |'
                    f'{result["status"]} |'
                    f'{result["length"]} |'
                    f'{result["title"]}')
                live_urls.append(
                    f'{result["url"]} |'
                    f'{result["status"]} |'
                    f'{result["length"]} |'
                    f'{result["title"]}')
            except Exception as e:
                print(Fore.RED + f"[ERROR] {e}")
    end = time.time()
    print(
        Fore.CYAN + f"\n[+] COMPLETED IN {end - start:.2f} SECONDS")
    
    

    with open(
            "output/live_urls.txt",
            "w"
        ) as f:
            for url in live_urls:
                f.write(url + "\n")

    with open(
        "output/interesting_params.txt",
        "w"
        ) as f:
        for url in interesting_params:
            f.write(url + "\n")

    with open(
        "output/risky_params.txt",
        "w"
        ) as f:
        for url in risky_params:
            f.write(url + "\n")
    
    with open(
        "output/results.json",
        "w"
        ) as f:
            json.dump(results , f ,indent=4)

if __name__ == "__main__": 

    try:
         main()
    except KeyboardInterrupt:
         print(Fore.RED + "\n[!] EXITING...")



  
