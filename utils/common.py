import re


def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)  
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

def predict(resume_text, vectorizer, model, labels):
    resume_text= cleanResume(resume_text)
    #print('Entered the predict')
    #print('Resume Text: ', resume_text)
    resume_tfidf = vectorizer.transform([resume_text])
    #print("TF-IDF Shape:", resume_tfidf.shape)
    predicted_class = model.predict(resume_tfidf)[0]
    #print('Predicted_cateogory', predicted_class)
    predicted = labels.get(str(predicted_class), "Unknown Category")
    return predicted