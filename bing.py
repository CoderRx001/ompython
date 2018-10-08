subscription_key = "034074d6968d4526aeb0f955b7c934d6"
assert subscription_key

search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"

search_term = "Microsoft"

import requests
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

descriptions = [article["description"] for article in search_results["value"]]

from IPython.display import HTML
rows = "\n".join(["<tr><td>{0}</td></tr>".format(desc) for desc in descriptions])
HTML("<table>"+rows+"</table>")

    print(descriptions,article)
