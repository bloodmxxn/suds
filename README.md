# SUDS — Suspicious URL Detection System

## Suspicious URL Indicators

SUDS aims to identify potentially suspicious URLs by analyzing multiple indicators. The presence of any single indicator does not necessarily mean that a URL is malicious.

### 1. URL Structure Analysis

- **URL Length:** Unusually long URLs may indicate obfuscation or excessive parameters.
- **Hostname Length:** Extremely long hostnames may be suspicious.
- **Subdomain Count:** An unusually high number of subdomains may be used to mislead users.
- **IP Address:** Using an IP address instead of a domain name may warrant further inspection.
- **URL Credentials:** Embedded usernames or passwords may indicate a deceptive URL.
- **Port:** Unusual port numbers may require further investigation.
- **Path Depth:** Excessively deep or unusual paths may be suspicious.

### 2. Query Analysis

Inspect query parameters for potentially suspicious content, including:

- HTML tags such as `<script>`.
- JavaScript code or potential Cross-Site Scripting (XSS) payloads.
- URL-encoded or multiply encoded content.
- Excessively long, duplicated, or unusual parameter values.

### 3. Fragment Analysis

The fragment is the portion of a URL after `#`. Although it is generally not sent to the server, client-side JavaScript may process it.

Potential indicators include suspicious HTML tags, script-related content, and possible XSS payloads.

### 4. Path Analysis

Inspect the URL path for:

- Unexpected or suspicious code patterns.
- URL-encoded or multiply encoded strings.
- Excessively long or unusually structured paths.
- Deceptive path segments that imitate trusted services or brands.

### 5. Domain Popularity and Reputation

- **Domain Popularity:** Check whether the registered domain appears in a list of the one million most popular domains.
- **Threat Intelligence:** Future versions may compare URLs and domains against known malicious URL feeds.

A popular domain is not necessarily safe, and an unfamiliar domain is not necessarily malicious.

### Detection Principle

SUDS records suspicious indicators independently and combines multiple pieces of evidence to assess potential risk. Each finding should include an explanation to support the final assessment.

**Disclaimer:** SUDS identifies potentially suspicious patterns; these indicators alone do not prove that a URL is malicious.
