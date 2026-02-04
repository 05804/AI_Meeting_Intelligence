import nltk
nltk.data.path.append("C:\\Users\\shaik\\AppData\\Roaming\\nltk_data")
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter



# Download NLTK data (first time only)
nltk.download('punkt')

# Read transcript
with open("transcript.txt", "r", encoding="utf-8") as f:
    transcript = f.read()

# --- 1️⃣ Simple summary using top sentences ---
sentences = sent_tokenize(transcript)
words = word_tokenize(transcript.lower())
word_freq = Counter(words)

# Remove common words (stopwords)
stopwords = set([
    "the","is","in","and","to","a","of","for","on","with","as","we","our","this","that",
    "are","at","it","by","be","an","from","or","will","but","if","you","can","have"
])

for w in list(word_freq):
    if w in stopwords or not w.isalpha():
        del word_freq[w]

# Score sentences
sentence_scores = {}
for sent in sentences:
    sentence_scores[sent] = sum(word_freq.get(w.lower(), 0) for w in word_tokenize(sent))

# Pick top 5 sentences
summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:5]
summary_text = " ".join(summary_sentences)

# --- 2️⃣ Extract action items & decisions (keywords) ---
action_items = []
decisions = []

for line in transcript.split("\n"):
    line_lower = line.lower()
    if any(k in line_lower for k in ["action", "todo", "task"]):
        action_items.append(line.strip())
    if any(k in line_lower for k in ["decided", "decision", "agreed"]):
        decisions.append(line.strip())

# --- 3️⃣ Save analysis ---
with open("analysis.txt", "w", encoding="utf-8") as f:
    f.write("=== Meeting Summary ===\n")
    f.write(summary_text + "\n\n")
    f.write("=== Action Items ===\n")
    for item in action_items:
        f.write("- " + item + "\n")
    f.write("\n=== Decisions ===\n")
    for d in decisions:
        f.write("- " + d + "\n")

# --- 3️⃣ Save analysis as Markdown ---
with open("analysis.md", "w", encoding="utf-8") as f:
    f.write("# 📝 Meeting Analysis\n\n")
    f.write("## 📌 Summary\n")
    f.write(summary_text + "\n\n")
    
    f.write("## ✅ Action Items\n")
    if action_items:
        for item in action_items:
            f.write(f"- {item}\n")
    else:
        f.write("- None\n")
    
    f.write("\n## 🏁 Decisions\n")
    if decisions:
        for d in decisions:
            f.write(f"- {d}\n")
    else:
        f.write("- None\n")

print("✅ Markdown analysis complete! Check analysis.md")

