import re

def extract_contact_number_from_resume(text):
    contact_number = None
    #print('Text phone number: ', text)

    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    #print('Match:', match)
    if match:
        contact_number = match.group()

    return contact_number