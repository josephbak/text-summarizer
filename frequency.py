import nltk

def generate_summary_by_frequency(sentences, sent_value, avg):
    """
    Generate a summary sentence by sentence score which is greater than the average.
    15 words for now, need to be modified.
    """
    sentence_count = 0
    summary = ""

    for sent in sentences:
        if sent[:15] in sent_value and sent_value[sent[:15]] >= avg:
            summary += sent + " "
            sentence_count += 1
    return summary