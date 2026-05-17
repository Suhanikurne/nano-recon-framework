from urllib.parse import urlparse, parse_qs

def extract_params(urls):
    interesting_params = []

    for url in urls:
        parsed_urls = urlparse(url)
        print(f"PRINTING PARSED URLS ... -> {parsed_urls}")
        params_urls = parse_qs(parsed_urls.query)
        print(f"PRINTING PARAMETERS ... -> {params_urls}")

        if params_urls:
            interesting_params.append(url)

    return list(set(interesting_params))


