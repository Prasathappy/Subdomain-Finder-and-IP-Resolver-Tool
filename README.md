<h1 align="center" id="title">🌐 Subdomain Finder and IP Resolver</h1>

<p id="description">An advanced Python tool that combines subdomain discovery and IP address resolution in one efficient solution. This project is designed for cybersecurity professionals penetration testers and developers looking to automate DNS reconnaissance for a target domain.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Subdomain Discovery: Scans a target domain for potential subdomains using a customizable wordlist and DNS queries.
*   IP Address Resolution: Resolves the IP addresses (A records) for discovered subdomains.
*   Multi-Threading: Leverages threading for faster execution and improved performance.
*   Output Results: Saves discovered subdomains and their corresponding IPs in a neatly formatted output file.

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/Prasathappy/Subdomain-Finder-and-IP-Resolver-Tool.git
```

<p>2. Install the required libraries:</p>

```
pip install dnspython
```

<p>3. Move to the Directory:</p>

```
cd Subdomain-Finder-and-IP-Resolver-Tool
```

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Language: Python
*   dns.resolver: For DNS resolution.
*   concurrent.futures: For multi-threading.
*   argparse: For handling command-line arguments.
