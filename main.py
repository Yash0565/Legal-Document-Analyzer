from extractor import extract_text_from_pdf, chunk_text
from summarizer import summarize_chunks, extract_key_clauses

pdf_path = input("Enter the full path to your PDF file: ").strip()

print("\nReading document...")
raw_text = extract_text_from_pdf(pdf_path)
total_words = len(raw_text.split())
total_sentences = len(raw_text.split('.'))
print(f"Extracted {total_words} words across {total_sentences} sentences.")

print("\n" + "="*60)
print("PLAIN-ENGLISH SUMMARY")
print("="*60)

chunks = chunk_text(raw_text, max_words=400)
summaries = summarize_chunks(chunks)

summary_word_count = sum(len(s.split()) for s in summaries)

for i, summary in enumerate(summaries):
    print(f"\nSection {i+1}:\n{summary}")

print("\n" + "="*60)
print("KEY CLAUSES DETECTED")
print("="*60)

clauses = extract_key_clauses(raw_text)

if clauses:
    for clause_name, clause_text in clauses.items():
        print(f"\n>> {clause_name}:\n{clause_text}")
else:
    print("No standard clauses detected.")

print("\n" + "="*60)
print("DOCUMENT STATS")
print("="*60)
print(f"Total words in document         : {total_words}")
print(f"Total sentences in document     : {total_sentences}")
print(f"Total chunks processed          : {len(chunks)}")
print(f"Words in summary                : {summary_word_count}")

compression = round((1 - summary_word_count / total_words) * 100, 1) if total_words > 0 else 0
print(f"Compression ratio               : {compression}% ")

clauses_possible = 8
clauses_found = len(clauses)
clause_coverage = round((clauses_found / clauses_possible) * 100, 1)
print(f"Clauses detected                : {clauses_found} / {clauses_possible} known clause types")
print(f"Clause coverage                 : {clause_coverage}%")
print("="*60)


