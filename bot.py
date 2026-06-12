# Pulse - Daily Summary Bot
#Fetches: Weather (wttr.in) + a quote (zenqoutes.io)
#Runs: everydat at 8 AM IST via Gitzhub Actions
#APIs: both free, no API keys needed
import requests
from datetime import date

#--Function 1: Weather----------
def get_weather(city="Thiruvananthapuram"):
    """fetch today's weather as a one-line text summary."""
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

#--FUNCTION 2: Qoute------------
def get_quote():
    """"Fetch a random motivational qoute from ZenQuotes."""    
    url= "https://zenquotes.io/api/random"
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        data=response.jason()               #convert JSON toPython list
        quote=data[0]["q"]                  #the quote text
        author=data[0]["a"]                 #the author name
        return f'"{quote}"-{author}'
    except Exception as e:
        return f"Quote unavailable ({e})"
    
    from datetime import date

def build_summary():
    """Assemble the full daily summary from all data sources."""
    today = date.today().strftime("%A, %d %B %Y")
    weather = get_weather()
    quote = get_quote()

    summary = f"""
================================
PULSE - Daily Summary
{today}
================================

WEATHER
  {weather}

TODAY'S QUOTE
  {quote}

================================
"""
    return summary

# -- FUNCTION 4: Run everything ------------------------
def run():
    """Main entry point. Called by GitHub Actions."""
    summary = build_summary()

    # Print to the GitHub Actions log (visible in Actions tab)
    print(summary)

    # Save to a file (uploaded as downloadable artifact)
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Pulse ran successfully.")


# -- Entry point guard ---------------------------------
# Only runs when you execute: python bot.py
# Does NOT run when another file imports bot.py
if __name__ == "__main__":
    run()