# cleaning labels
def clean_label(label):
  
    return label.strip().lower()

# normalize confidence
def normalize_confidence(confidence):

    return confidence / 100
