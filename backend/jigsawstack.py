import requests

class JigsawStack:
  def __init__(self, key: str) -> None:
    self.jssHeaders = { "x-api-key": key }
    self.jssBaseURL = "https://api.jigsawstack.com"

  def scrapeGoVolunteer(self, location: str, keyword: str) -> list[str]:
    goVolunteerURL = f"https://govolunteer.com.au/volunteering/in-{location}?keyword={keyword}"
    goVolunteerParams = {
      "url": goVolunteerURL,
      "elements": [
        {
          "selector": "h2",
        },
      ],
    }
    
    r = requests.post(f"{self.jssBaseURL}/v1/web/scrape", headers=self.jssHeaders, json=goVolunteerParams)
    results = r.json()["data"][0]["results"]

    if "No opportunities at the mo" in results[0]["text"]:
      return []

    opportunities = []
    for result in results:
      if "please wait" not in result["text"].lower() and "something's gone wrong" not in result["text"].lower():
        opportunities.append(result["text"])

    return opportunities

  def scrapeSeekVolunteer(self, location: str, keyword: str, page: int) -> list[str]:
    seekVolunteerURL = f"https://www.volunteer.com.au/volunteering/in-{location}?keyword={keyword}&page={str(page)}"
    seekVolunteerParams = {
      "url": seekVolunteerURL,
      "elements": [
        {
          "selector": ".mb-0",
        },
      ]
    }

    r = requests.post(f"{self.jssBaseURL}/v1/web/scrape", headers=self.jssHeaders, json=seekVolunteerParams)
    results = r.json()["data"][0]["results"]

    opportunities = []
    for result in results:
      if "When new opportunities for this search" not in result["text"] and "Email address" not in result["text"]:
        opportunities.append(result["text"])

    return opportunities

  def scrapeVolunteeringOpportunities(self, location: str, keyword: str) -> list[str]:
    allOpportunities = []

    print("=== Scraping volunteering opportunities from Go Volunter ===")
    allOpportunities.extend(self.scrapeGoVolunteer(location, keyword))

    print("=== Scraping volunteering opportunities from Seek Volunter ===")
    # Seek returns multiple pages, and it is possible to iterate over them, but it takes too long, so limit to 1 page
    allOpportunities.extend(self.scrapeSeekVolunteer(location, keyword, 1)) 

    return allOpportunities

  def getOccupationSuggestions(self, keyword: str) -> list[str]:
    params = { "search_value": keyword }
    r = requests.get(f"{self.jssBaseURL}/v1/data/occupation", headers=self.jssHeaders, params=params)
    occupations = r.json()["data"][:8] # return first 8 recommendations
    return occupations