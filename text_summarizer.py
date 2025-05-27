from transformers import pipeline

summarizer = pipeline("summarization")

text = """Artificial intelligence (AI) is transforming the world. From healthcare to transportation, AI is making things smarter, faster, and more efficient. With the help of machine learning algorithms, systems can learn from data and make decisions without being explicity programmed. This technology is growing rapidly and influencing every part of our lives, including how we work and communicate."""

summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print("Original Text:\n", text)
print("\nSummary:\n", summary[0]['summary_text'])
