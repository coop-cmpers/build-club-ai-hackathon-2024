import google.generativeai as genai

class GenAI:
  getVolunteeringSuggestionsInstructions = """
  I'm writing a software to recommend users locations to volenteer for their local communities
  and make a positive impact. I would like for you to process the following array of possible opportunities and return your top 
  5 picks (if there is more than 5 possible titles / inputs), making sure that they are all different types of opportunities / 
  different forms of volenteering. Otherwise, if you don't have 5 possible volenteering locations, please include everything that
  is available in the data and give recommendations for websites to find more opportunities. Please return the data to the user
  in the form of a numbered list"

  ======
  """

  def __init__(self, key: str) -> None:
    genai.configure(api_key=key)
    self.model = genai.GenerativeModel("gemini-1.5-flash")

  def callGenAIWithAnyPrompt(self, prompt: str) -> str:
    response = self.model.generate_content(prompt)
    return response.text

  def getVolunteeringSuggestions(self, opportunities: list[str]) -> str:
    print("=== Calling Gemini with the scraped volunteering opportunities ===")
    prompt = self.getVolunteeringSuggestionsInstructions + str(opportunities)
    response = self.model.generate_content(prompt)
    return response.text
