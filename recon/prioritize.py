from urllib.parse import parse_qs , urlparse

HIGH_RISK_PARAMS = [
    "admin",
    "redirect",
    "id",
    "login",
    "next",
    "url",
    "callback",
    "file",
    "path",
    "q"
]

def prioritize_params(urls):

    risky_params = []
    
    for url in urls:
        parsed_urls = urlparse(url)
        params_url = parse_qs(parsed_urls.query)

        for param in params_url:
            if param.lower() in HIGH_RISK_PARAMS:
                risky_params.append(url)

    return list(set(risky_params))

