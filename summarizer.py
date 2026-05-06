import re


def extractive_summary(text, num_sentences=5):
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if len(s.strip()) > 40]
    scored = []
    for sentence in sentences:
        words = sentence.lower().split()
        important_words = ["agree", "shall", "must", "party", "payment", "term",
                          "terminat", "confidential", "liable", "govern", "law",
                          "oblig", "right", "duty", "period", "date", "fee"]
        score = sum(1 for word in words if any(kw in word for kw in important_words))
        scored.append((score, sentence))
    scored.sort(reverse=True)
    top_sentences = [s for _, s in scored[:num_sentences]]
    return top_sentences

def summarize_chunks(chunks):
    summaries = []
    for i, chunk in enumerate(chunks):
        print(f"  Summarizing section {i+1} of {len(chunks)}...")
        top_sentences = extractive_summary(chunk, num_sentences=3)
        summary = ' '.join(top_sentences)
        summaries.append(summary)
    return summaries

def extract_key_clauses(text):
    keywords = {
        "Termination":           ["terminat", "end of agreement", "cancellation"],
        "Payment Terms":         ["payment", "invoice", "fee", "compensation", "salary"],
        "Confidentiality":       ["confidential", "non-disclosure", "nda", "proprietary"],
        "Liability":             ["liability", "liable", "indemnif", "damages", "loss"],
        "Governing Law":         ["governing law", "jurisdiction", "disputes", "arbitration"],
        "Intellectual Property": ["intellectual property", "copyright", "trademark", "ownership"],
        "Non-Compete":           ["non-compete", "non compete", "restraint of trade"],
        "Renewal":               ["renewal", "auto-renew", "rollover", "extend"],
    }

    found_clauses = {}
    sentences = text.replace('\n', ' ').split('.')

    for clause, kws in keywords.items():
        for sentence in sentences:
            if any(kw.lower() in sentence.lower() for kw in kws):
                clean = sentence.strip()
                if len(clean) > 20:
                    found_clauses[clause] = clean
                    break

    return found_clauses