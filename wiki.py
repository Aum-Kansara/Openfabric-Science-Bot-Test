import wikipedia
results = wikipedia.search("Force")
print(wikipedia.summary(results[0],auto_suggest=False))