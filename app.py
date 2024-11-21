from flask import Flask, render_template, request
import pickle
import json
from utils.common import predict, cleanResume
from utils.resume_text import extract_text_from_pdf
from utils.name import extract_name_from_resume
from utils.email_address import extract_email_from_resume
from utils.contact_number import extract_contact_number_from_resume
from utils.education import extract_education_from_resume
from utils.skills import extract_skills_from_resume


app = Flask(__name__)

category_encoder = 'artifacts/categorization/encoder.pkl'
category_labels = 'artifacts/categorization/labels.json'
category_model = 'artifacts/categorization/model.pkl'
category_vectorizer = 'artifacts/categorization/vectorizer.pkl'

with open(category_encoder, 'rb') as file:
    category_encoder = pickle.load(file)

with open(category_labels, 'r') as file:
    category_labels = json.load(file)

with open(category_model, 'rb') as file:
    category_model = pickle.load(file)

with open(category_vectorizer, 'rb') as file:
    category_vectorizer = pickle.load(file)


job_recommendation_encoder = 'artifacts/job_recommendation/encoder.pkl'
job_recommendation_labels = 'artifacts/job_recommendation/labels.json'
job_recommendation_model = 'artifacts/job_recommendation/model.pkl'
job_recommendation_vectorizer = 'artifacts/job_recommendation/vectorizer.pkl'

with open(job_recommendation_encoder, 'rb') as file:
    job_recommendation_encoder = pickle.load(file)

with open(job_recommendation_labels, 'r') as file:
    job_recommendation_labels = json.load(file)

with open(job_recommendation_model, 'rb') as file:
    job_recommendation_model = pickle.load(file)

with open(job_recommendation_vectorizer, 'rb') as file:
    job_recommendation_vectorizer = pickle.load(file)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/pred', methods=['POST'])
def pred():
    if 'resume' in request.files:
        file = request.files['resume']
        filename = file.filename
        print('Filename', filename)
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(file)
        elif filename.endswith('.txt'):
            text = file.read().decode('utf-8')
        else:
            return render_template('index.html', message = "Invalid file enter. Please enter upload only .pdf or .txt")
        
        #print('Text', text)
        predicted_category = predict(text, category_vectorizer, category_model, category_labels)
        predicted_job = predict(text, job_recommendation_vectorizer, job_recommendation_model, job_recommendation_labels)
        cleaned_text = cleanResume(text)
        name = extract_name_from_resume(text)
        email_address = extract_email_from_resume(text)
        phone = extract_contact_number_from_resume(cleaned_text)
        extracted_education = extract_education_from_resume(text)
        extracted_skills = extract_skills_from_resume(text)


        print('Predicted_Category: ', predicted_category)
        print('Predicted Job: ', predicted_job)
        print('Education: ', extracted_education)

        

        return render_template('index.html', predicted_category=predicted_category, predicted_job=predicted_job, name=name, email_address=email_address,phone=phone, extracted_education=extracted_education, extracted_skills=extracted_skills)
    
    else:
        return render_template('index.html', message = "No file uploaded")


if __name__=='__main__':
    app.run(debug=True)


#Smart Resume Screening and Job Recommendation System