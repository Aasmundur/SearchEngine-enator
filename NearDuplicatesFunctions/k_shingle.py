import re
def k_shingle(text, k):
    
    text = text.lower()

    text = re.sub(r'[^a-z\s]', '', text)

    words = text.split()
    
    shingles = set()

    for i in range(len(words) - k + 1):
        shingle = ' '.join(words[i:i + k])
        shingles.add(shingle)
    
    return shingles