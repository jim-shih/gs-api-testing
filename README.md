# Google Custom Search API Implementation Guide

This repository demonstrates the implementation of Google Custom Search API using the REST API method in Python. This guide clarifies the differences between various Google search APIs, their billing structures, and explains why we chose the REST API approach.

## Overview

Google offers several search API options, each with different use cases, pricing models, and implementation methods. This guide focuses on the Custom Search API, which provides programmatic access to Google search results.

## API Comparison

| Feature | Custom Search API | Programmable Search Element | Custom Search JSON API |
|---------|-------------------|-----------------------------|-----------------------|
| Type | REST API | Web Interface | REST API |
| Endpoint | googleapis.com/customsearch/v1 | cse.google.com/cse | googleapis.com/customsearch/v1 |
| Authentication | API Key Required | No API Key Required | API Key Required |
| Free Quota | 100 queries/day | Unlimited | 100 queries/day |
| Pricing | $5 per 1000 queries | Free | $5 per 1000 queries |
| Result Format | JSON | HTML | JSON |
| Use Case | Programmatic access | Website integration | Programmatic access |
| Max Results | 10 per request | Up to 100 | 10 per request |

## Why REST API?

This repository uses the REST API method for implementing the Custom Search API because:

1. **Simplicity:** Straightforward implementation without additional libraries.
2. **Flexibility:** Easy customization of search parameters.
3. **Language Agnostic:** Can be implemented in any programming language supporting HTTP requests.
4. **Direct Control:** Provides direct control over API calls, facilitating rate limiting and error handling.

## Setup and Authentication

### Getting API Key
1. Visit [Google Cloud Console](https://console.cloud.google.com)
2. Navigate to "APIs & Services" → "Credentials"
3. Click "Create Credentials" → "API key"
4. Store the generated API key securely
- **Note:** Enable Custom Search API in "APIs & Services" → "Library"

### Getting Search Engine ID (CSE ID)
1. Visit [Programmable Search Engine](https://programmablesearchengine.google.com)
2. Click "Get Started"
3. Configure your search engine:
   - Name your search engine
   - Choose search scope (specific sites or entire web)
   - Configure settings (Image search, SafeSearch)
4. Find your Search Engine ID in Control Panel → "Overview" → "Basic"

## Implementation

Here's an example of how to use the Custom Search API with Python:

```python
import requests

base_url = "https://www.googleapis.com/customsearch/v1"
params = {
    'key': API_KEY,
    'cx': CSE_ID,
    'q': query
}
response = requests.get(base_url, params=params)
```

## Billing Clarification

- **Custom Search API and Custom Search JSON API:** 
  - Free quota: 100 queries per day
  - Pricing: $5 per 1000 queries after free quota
  - Use case: Programmatic access to search results

- **Programmable Search Element:** 
  - Free service with no query limits
  - Use case: Embedding a custom search engine on websites
  - Less flexible for programmatic use

## Project Setup

1. Install dependencies:
```bash
poetry install
```

2. Configure pre-commit hooks:
```bash
pre-commit install
```

3. Create `.env` file:
```
API_KEY=your_api_key_here
CSE_ID=your_cse_id_here
```

4. Run the search examples using the Python REST API implementation.

## Best Practices

1. **Monitor Usage:** Keep track of your API usage to avoid unexpected billing charges.
2. **Rate Limiting:** Implement rate limiting in your application to stay within quota limits.
3. **Error Handling:** Properly handle API errors and edge cases in your code.
4. **Secure Storage:** Always store your API key securely and never expose it in client-side code.

## Conclusion

The REST API implementation of Google Custom Search API offers a flexible and powerful way to integrate Google search capabilities into your applications. By understanding the different API options and their billing structures, you can choose the most appropriate solution for your project's needs.