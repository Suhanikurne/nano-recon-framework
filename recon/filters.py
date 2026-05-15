def filter_urls(urls):

    print("[+] FILTERING INTERESTING URLS....")
    
    interesting_urls = []

    keywords = [
        "admin",
        "api",
        "login",
        "auth"
    ]

    for url in urls:

        if "?" in url:
            interesting_urls.append(url)

        elif any(
            keyword in url.lower()
            for keyword in keywords
        ):
            interesting_urls.append(url)

        elif url.endswith(".js"):
            interesting_urls.append(url)

    return list(set(interesting_urls))
