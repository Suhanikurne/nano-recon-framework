# Nano Recon Framework

Nano Recon Framework is a Python-based reconnaissance automation tool built for web application attack surface mapping.

## Features

- Subdomain enumeration
- URL collection
- Interesting endpoint filtering
- Multithreaded HTTP status checking
- Page title extraction
- Output saving
- Modular architecture

## Technologies Used

- Python
- requests
- BeautifulSoup4
- colorama
- concurrent.futures

## Project Structure

```bash
nano-recon-framework/
│
├── main.py
├── requirements.txt
├── recon/
│   ├── subdomains.py
│   ├── urls.py
│   ├── filters.py
│   └── status.py
│
└── output/
```

## Installation

```bash
git clone https://github.com/Suhanikurne/nano-recon-framework.git

cd nano-recon-framework

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

## Future Improvements

- Parameter discovery
- Screenshot collection
- Technology fingerprinting
- AI-based report generation
- Async requests with aiohttp

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.
