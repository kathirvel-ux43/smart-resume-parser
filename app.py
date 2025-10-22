# Main application - user interface for resume parser

import streamlit as st
import pandas as pd
from text_extractor import FileTextReader
from resume_parser import ResumeAnalyzer
import os

def create_resume_parser_app():
    st.set_page_config(
        page_title="Resume Analysis Tool",
        page_icon="📋",
        layout="wide"
    )
    
    st.title("Resume Analysis Tool")
    st.write("Upload resume files to extract important information")
    
    uploaded_resumes = st.file_uploader(
        "Select resume files",
        type=['pdf', 'docx'],
        accept_multiple_files=True
    )
    
    if uploaded_resumes:
        text_reader = FileTextReader()
        resume_analyzer = ResumeAnalyzer()
        
        all_analysis_results = []
        
        for resume_file in uploaded_resumes:
            st.subheader(f"File: {resume_file.name}")
            
            temp_filename = f"temp_{resume_file.name}"
            with open(temp_filename, "wb") as temp_file:
                temp_file.write(resume_file.getbuffer())
            
            file_content = ""
            if resume_file.name.endswith('.pdf'):
                file_content = text_reader.get_pdf_content(temp_filename)
            else:
                file_content = text_reader.get_docx_content(temp_filename)
            
            processed_content = text_reader.prepare_text(file_content)
            
            if processed_content:
                analysis_result = resume_analyzer.analyze_resume_content(processed_content)
                analysis_result['file_name'] = resume_file.name
                all_analysis_results.append(analysis_result)
                
                left_column, right_column = st.columns(2)
                
                with left_column:
                    st.write("**Contact Details**")
                    st.json(analysis_result['contact_details'])
                    
                    st.write("**Technical Skills**")
                    if analysis_result['technical_skills']:
                        for skill in analysis_result['technical_skills']:
                            st.write(f"• {skill}")
                    else:
                        st.info("No technical skills identified")
                
                with right_column:
                    st.write("**Education Background**")
                    if analysis_result['education_history']:
                        for education in analysis_result['education_history']:
                            st.write(f"• {education['qualification']} - {education['specialization']}")
                    else:
                        st.info("No education details found")
                    
                    st.write("**Professional Experience**")
                    if analysis_result['work_experience']:
                        for experience in analysis_result['work_experience'][:3]:
                            st.write(f"• {experience['details'][:80]}...")
                    else:
                        st.info("No work experience detected")
            
            os.remove(temp_filename)
            st.markdown("---")
        
        if all_analysis_results:
            st.sidebar.header("Export Options")
            
            summary_data = []
            for result in all_analysis_results:
                summary_row = {
                    'File Name': result['file_name'],
                    'Email': result['contact_details'].get('email_address', 'Not available'),
                    'Phone': result['contact_details'].get('phone_number', 'Not available'),
                    'Skills Found': len(result['technical_skills']),
                    'Education Items': len(result['education_history']),
                    'Experience Items': len(result['work_experience'])
                }
                summary_data.append(summary_row)
            
            summary_table = pd.DataFrame(summary_data)
            st.subheader("Analysis Summary")
            st.dataframe(summary_table)
            
            export_col1, export_col2 = st.sidebar.columns(2)
            
            with export_col1:
                csv_data = summary_table.to_csv(index=False)
                st.download_button(
                    "Download CSV Summary",
                    csv_data,
                    "resume_analysis_summary.csv",
                    "text/csv"
                )
            
            with export_col2:
                import json
                json_data = json.dumps(all_analysis_results, indent=2)
                st.download_button(
                    "Download Full Data (JSON)",
                    json_data,
                    "complete_analysis_data.json",
                    "application/json"
                )

                left_column, right_column = st.columns(2)
                score = resume_analyzer.calculate_resume_score(processed_content)
                st.write(f"**Resume Score: {score}/100**")
                
                st.progress(score/100)
                
                if score >= 80:
                    st.success("Excellent Resume!")
                elif score >= 60:
                    st.warning("Good Resume - Could be improved")
                else:
                    st.error("Basic Resume - Needs more content")
                
                with left_column:
                    st.write("**Contact Details**")
if __name__ == "__main__":
    create_resume_parser_app()