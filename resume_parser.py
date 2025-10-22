# Resume analysis module - extracts information from text

import spacy
import re

class ResumeAnalyzer:
    def __init__(self):
        self.nlp_engine = spacy.load("en_core_web_sm")
    
    def find_technical_skills(self, resume_text):
        technology_list = [
            'python', 'java', 'javascript', 'html', 'css', 'sql',
            'react', 'angular', 'nodejs', 'django', 'flask',
            'machine learning', 'data analysis', 'tableau',
            'aws', 'azure', 'docker', 'git', 'github',
            'excel', 'word', 'powerpoint', 'ms office'
        ]
        
        detected_skills = []
        lower_text = resume_text.lower()
        
        for tech in technology_list:
            if tech in lower_text:
                formatted_tech = tech.title() if ' ' not in tech else tech
                detected_skills.append(formatted_tech)
        
        return detected_skills
    
    def find_education_details(self, resume_text):
        education_found = []
        
        degree_patterns = [
            r'(B\.S\.|B\.A\.|B\.Tech|Bachelor)[\s\w]*?in\s+([\w\s]+)',
            r'(M\.S\.|M\.A\.|M\.Tech|Master)[\s\w]*?in\s+([\w\s]+)',
            r'(Ph\.D|PhD|Doctorate)[\s\w]*?in\s+([\w\s]+)',
        ]
        
        for pattern in degree_patterns:
            matches = re.findall(pattern, resume_text, re.IGNORECASE)
            for match in matches:
                education_found.append({
                    'qualification': match[0],
                    'specialization': match[1] if len(match) > 1 else 'General'
                })
        
        return education_found
    
    def find_work_experience(self, resume_text):
        work_history = []
        
        processed_text = self.nlp_engine(resume_text)
        text_sentences = [sent.text for sent in processed_text.sents]
        
        for sentence in text_sentences:
            work_indicators = ['company', 'corporation', 'technologies', 'solutions', 'worked', 'experience']
            time_indicators = r'(20\d{2}|19\d{2}|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
            
            has_work_words = any(word in sentence.lower() for word in work_indicators)
            has_time_reference = re.search(time_indicators, sentence)
            
            if has_work_words and has_time_reference:
                work_history.append({
                    'details': sentence.strip(),
                    'length': len(sentence)
                })
        
        return work_history
    
    def find_contact_info(self, resume_text):
        contact_details = {}
        
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_regex = r'[\+]?[0-9]{1,4}?[-\s]?[0-9]{7,10}'
        
        email_match = re.search(email_regex, resume_text)
        if email_match:
            contact_details['email_address'] = email_match.group()
        
        phone_match = re.search(phone_regex, resume_text)
        if phone_match:
            contact_details['phone_number'] = phone_match.group()
        
        return contact_details
    
    def analyze_resume_content(self, resume_text):
        analysis_results = {
            'contact_details': self.find_contact_info(resume_text),
            'technical_skills': self.find_technical_skills(resume_text),
            'education_history': self.find_education_details(resume_text),
            'work_experience': self.find_work_experience(resume_text),
            'text_sample': resume_text[:300] + '...' if len(resume_text) > 300 else resume_text
        }
        
        return analysis_results
    
    def calculate_resume_score(self, resume_text):
        score = 0
        
        contact_info = self.find_contact_info(resume_text)
        if contact_info.get('email_address'): 
            score += 10
        if contact_info.get('phone_number'): 
            score += 10
        
        skills = self.find_technical_skills(resume_text)
        if skills: 
            score += min(len(skills) * 3, 30)
        
        education = self.find_education_details(resume_text)
        if education: 
            score += min(len(education) * 5, 20)
        
        experience = self.find_work_experience(resume_text)
        if experience: 
            score += min(len(experience) * 6, 30)
        
        return score
   