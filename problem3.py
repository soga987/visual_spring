# Load student admissions dataset
university_data = pd.read_csv('Year,Term,Applications,Admitted,Enrolled,Retention Rate (%),Student Satisfaction (%),Engineering Enrolled,Business Enrolled,Arts Enrolled,Science Enrolled
2015,Spring,2500,1500,600,85,78,200,150,125,125
2015,Fall,2500,1500,600,85,78,200,150,125,125
2016,Spring,2600,1550,625,86,79,210,160,130,125
2016,Fall,2600,1550,625,86,79,210,160,130,125
2017,Spring,2700,1600,650,87,80,225,165,135,125
2017,Fall,2700,1600,650,87,80,225,165,135,125
2018,Spring,2800,1650,675,86,82,235,175,140,125
2018,Fall,2800,1650,675,86,82,235,175,140,125
2019,Spring,3000,1750,700,88,83,250,185,145,120
2019,Fall,3000,1750,700,88,83,250,185,145,120
2020,Spring,2900,1700,690,85,81,240,180,140,130
2020,Fall,2900,1700,690,85,81,240,180,140,130
2021,Spring,3100,1800,725,87,84,260,195,150,120
2021,Fall,3100,1800,725,87,84,260,195,150,120
2022,Spring,3250,1900,750,88,85,275,200,160,115
2022,Fall,3250,1900,750,88,85,275,200,160,115
2023,Spring,3350,2000,775,89,86,285,210,165,115
2023,Fall,3350,2000,775,89,86,285,210,165,115
2024,Spring,3500,2100,800,90,88,300,225,175,100
2024,Fall,3500,2100,800,90,88,300,225,175,100')

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

