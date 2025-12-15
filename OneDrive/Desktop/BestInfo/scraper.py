import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    user_agent="BestInfo/1.0 (educational project)",
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

topic = input("Enter a topic to search: ")

page = wiki.page(topic)

if not page.exists():
    print("No information found for this topic.")
    exit()

print("\nTITLE:")
print(page.title)

print("\nSUMMARY:")
print(page.summary)

print("\nFULL DETAILS:")
print(page.text)
