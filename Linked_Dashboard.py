import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.express as px

st.set_page_config(page_title="LinkedIn Job Posting 2023 Data Analysis",page_icon= ":bar_chart:", layout="wide")
st.title(":globe_with_meridians: LinkedIn Job Posting 2023 Data Analysis")
st.markdown('<style>div.block-container{padding-top:1rem;}<style>', unsafe_allow_html=True)

df = pd.read_csv(r'/Users/sayed.ahmed/Library/CloudStorage/GoogleDrive-sayed.ahmed.sayed@gmail.com/My Drive/DataScience/DS_Projects/Epsilon_mid-project/LinkedIn Job Postings 2023/jobs_2.csv')
show_data = st.sidebar.checkbox("Show Data", False, key=1)
if show_data:
    st.header("Sample Data")
    st.dataframe(df.head(10))
 


country_name = st.sidebar.selectbox('Select Country' ,df['country'].unique())
work_type = st.sidebar.selectbox('Choose Work Type', df['work_type'].unique())
num = df.describe()
cat = df.describe(include= 'O')

tab1, tab2, tab3 = st.tabs(["📊 Visual1", "ℹ️ Visual2", "📊 Visual3"])



with tab1:
    tab1_col1, tab1_col2, tab1_col3 = st.columns(3)
    
    new = df[df['country'] == country_name].head(50)
    with tab1_col1:
        
        fig = px.pie(new, names= "work_type", title= "Work Type Distribution", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="Work Type", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.pie(df, names="sponsored", title="Sponsored Distribution", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="sponsored", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.pie(new, names="application_type", title="Application Type", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="application_type", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
    with tab1_col2:
        fig = px.pie(new, names="views", color= 'job_title', title="No of Jobs Dist Per Views", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="No of Views", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.pie(new, names="remote_allowed", color= 'remote_allowed', title="Remote Allowed", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="Remote Allowed", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.pie(new, names="applies", color= 'applies', title="Job Applies", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="Job Applies", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
    with tab1_col3:
        fig= px.bar(new, x= 'country', y= 'skill_abr', color= 'skill_abr', barmode ='group', title = f'Country Name {country_name.upper()} Per Skills'.title() )
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.bar(new, x= 'country', y= 'experience_level', color= 'experience_level', barmode ='group', title = f'Country Name {country_name.upper()} Per Work Exp'.title())
        st.plotly_chart(fig, use_container_width= True)
        
        fig = px.bar(new, x= 'country', y= 'city', color= 'city', barmode ='group', title = f'Country Name {country_name.upper()} Per City'.title())
        st.plotly_chart(fig, use_container_width= True)
        
        
        
        
        
with tab2:
    tab2_col1, tab2_col2, tab2_col3 = st.columns(3)
    
    with tab2_col1:
        
        applies = df.groupby(['job_title','work_type'])[['applies']].sum().sort_values('applies', ascending= False).reset_index().head(200)
        df_applies = applies[applies['work_type'] == work_type]
        fig= px.bar(df_applies, x= 'job_title', y= 'applies', color= 'applies', barmode ='group', title = f'Job Title {work_type.upper()} Per Applied'.title())
        fig.update_layout(legend_title="Job Applies", showlegend= True)
        st.plotly_chart(fig, use_container_width= False)
        



with tab3:
    tab3_col1, tab3_col2, tab3_col3 = st.columns(3)
    
    with tab3_col1:
        
        st.subheader('Numerical Descriptive Satatistics')
        st.dataframe(num)
        
        fig = px.pie(new, names="work_type", title="Work Type Distribution", color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_traces(textposition= 'inside', textinfo= 'percent+label')
        fig.update_layout(legend_title="Work Type", showlegend= True)
        st.plotly_chart(fig, use_container_width= True)
        
        
    with tab3_col3:
        st.subheader('Categorical Descriptive Statistics')
        st.dataframe(cat)
        
        applies = df.groupby(['job_title','work_type'])[['applies']].sum().sort_values('applies', ascending= False).reset_index().head(20)
        df_applies = applies[applies['work_type'] == work_type]
        fig= px.bar(df_applies, x= 'job_title', y= 'applies', color= 'applies', barmode ='group', title = f'Work Type {work_type.upper()} Per Job Title'.title() )
        st.plotly_chart(fig, use_container_width= True)
        
        applies = df.groupby(['work_type'])[['applies']].sum().sort_values('applies', ascending= False).reset_index()
        fig= px.bar(applies, x= 'work_type', y= 'applies', color= 'work_type', barmode ='group', title = f'Country Name {country_name.upper()} Per Skills'.title() )
        st.plotly_chart(fig, use_container_width= True)
        
    
        
        

