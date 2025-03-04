# Load student admissions dataset
university_data = pd.read_csv('university_student_dashboard_data.csv')

# Streamlit Dashboard Code (to be deployed on Streamlit Cloud)
def university_dashboard():
    st.title('University Admissions & Retention Dashboard')
    
    # Metrics
    total_applications = university_data['Applications'].sum()
    total_enrollments = university_data['Enrollments'].sum()
    retention_rate = university_data['Retention Rate'].mean()
    
    st.metric('Total Applications', total_applications)
    st.metric('Total Enrollments', total_enrollments)
    st.metric('Average Retention Rate', f'{retention_rate:.2f}%')
    
    # Visualization - Enrollment by Department
    fig, ax = plt.subplots()
    sns.barplot(data=university_data, x='Department', y='Enrollments', ax=ax)
    ax.set_title('Enrollments by Department')
    st.pyplot(fig)

