
# Smart Resume Screening and Job Recommendation System
<img src="Image/resume_image.webp" alt="Overview of Mood Analysis Flow" title="Overview of Mood Analysis Flow" width="400">


## Project Overview

This project implements an **Smart Resume Screening and Job Recommendation System** that helps employers automatically categorize resumes, recommend jobs based on resume data, and extract key information such as skills, education, name, phone number, and email from uploaded resumes.

It utilizes **Natural Language Processing (NLP)** techniques for **Resume Categorization**, **Resume Job Recommendation**, and **Resume Parsing (Information Extraction)**. Users can upload resumes in **TXT** or **PDF** formats, and the system will process the uploaded resume to extract relevant details and provide job recommendations based on the analysis.

You can access the live application here: [Smart Resume Screening App](https://your-app-link-on-render.com).

## Features

### 1. Resume Categorization
Once the user uploads their resume, the system categorizes the resume into relevant categories based on the content. This helps employers quickly identify the type of candidate based on their resume.

### 2. Resume Job Recommendation
Based on the content of the uploaded resume, the system recommends relevant job positions that best match the candidate's skills, experience, and qualifications.

### 3. Resume Parsing (Information Extraction)
The system extracts key information from the uploaded resume, including:
- **Name**
- **Phone Number**
- **Email Address**
- **Skills**
- **Education Background**

This information is displayed to the user for review.

## Dataset Information

### Jobs Dataset with Features
The **jobs_dataset_with_features** contains job-related data, which is used for:
- Categorizing resumes into relevant fields.
- Recommending appropriate jobs to candidates.

## Technologies Used

- **Python**
- **Flask** for the web framework
- **NLP Libraries** (such as spaCy, NLTK, or transformers) for text processing
- **PDF Parsing** (like PyPDF2 or pdfplumber) for extracting text from PDF resumes
- **HTML/CSS** for the frontend design
- **Render** for application deployment

## How It Works

1. **Upload Your Resume**: Users can upload a resume in either **PDF** or **TXT** format using the file upload form.
2. **Processing**: Once the resume is uploaded, the system processes the document using NLP models to categorize the resume and extract key details like name, phone number, skills, and education.
3. **Job Recommendations**: The system uses the parsed data to suggest jobs that best fit the candidate’s profile.
4. **Display Results**: After processing, the system displays the following to the user:
   - **Category of Resume**
   - **Recommended Job(s)**
   - **Extracted Information** (Name, Phone Number, Email, Skills, and Education)

## Setup Instructions

### Prerequisites

Make sure you have the following software installed:
- **Python 3.x**
- **Flask** (Web framework)
- **PDF parsing libraries** like `PyPDF2`, `pdfplumber` (if using PDFs)
- **spaCy**, **transformers**, or other NLP libraries for processing text
- **HTML/CSS** for the frontend

### Local Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/smart-resume-screening.git
    cd smart-resume-screening
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the **jobs_dataset_with_features** from the release link:  
   [Jobs Dataset with Features Release](https://your-dataset-link.com)

4. Place the dataset in the appropriate directory as required by the application.

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open a browser and go to `http://127.0.0.1:5000/` to access the app.

## Accessing the Deployed App

The application has been deployed on **Render**. You can use the live app here:  
[Smart Resume Screening App](https://your-app-link-on-render.com).

## How to Use

1. On the homepage, click the **Upload Your Resume** section.
2. Select your **resume file** (PDF or TXT) from your local device and submit the form.
3. Wait for the system to process your resume. After processing:
   - The **Category** of your resume and the **Recommended Job** will be displayed.
   - Any **extracted information** like your name, phone number, email, skills, and education will also be shown.
4. You can then navigate back to the homepage by clicking the **Go to Home** button.


