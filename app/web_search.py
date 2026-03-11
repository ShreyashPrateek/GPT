import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json

def search_web(query: str, max_results: int = 3) -> str:
    """Search the web and return formatted results"""
    try:
        # Use DuckDuckGo HTML search
        url = "https://html.duckduckgo.com/html/"
        params = {"q": query}
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
        response = requests.post(url, data=params, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return "Unable to fetch current information at this time."
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('div', class_='result', limit=max_results)
        
        if not results:
            return "No current information found. The event may not have occurred yet or information is not available."
        
        formatted_results = f"Current information (as of {datetime.now().strftime('%Y-%m-%d')}):\n\n"
        
        for i, result in enumerate(results, 1):
            title_elem = result.find('a', class_='result__a')
            snippet_elem = result.find('a', class_='result__snippet')
            
            if title_elem and snippet_elem:
                title = title_elem.get_text(strip=True)
                snippet = snippet_elem.get_text(strip=True)
                link = title_elem.get('href', '')
                
                formatted_results += f"{i}. {title}\n"
                formatted_results += f"   {snippet}\n"
                if link:
                    formatted_results += f"   Source: {link}\n"
                formatted_results += "\n"
        
        return formatted_results
        
    except Exception as e:
        return "Unable to fetch current information. Please try rephrasing your question."

def needs_web_search(query: str) -> bool:
    """Determine if a query needs web search based on keywords"""
    current_keywords = [
        "current", "latest", "recent", "today", "now", "2024", "2025", "2026",
        "news", "update", "happening", "winner", "score", "result", "live"
    ]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in current_keywords)
