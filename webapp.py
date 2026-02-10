import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Urban Suffocation",
    layout="wide"
)

st.title("Urban Suffocation")
st.subheader(
    "A Spatiotemporal Analysis of Air Pollution, Policy, Weather, and Public Response in Delhi"
)


tab_intro, tab_proposal, tab_team = st.tabs([
    "Introduction",
    "Proposal Overview",
    "Team"
])


with tab_intro:

    st.header("Research Topic & Significance")

    st.markdown("""
    This project analyzes severe air pollution events in Delhi by studying long-term trends
    in PM2.5 and AQI levels. Delhi is consistently among the most polluted cities in the world,
    making air quality a serious public health and environmental concern. Pollution levels are
    influenced by multiple interacting factors, including emissions, weather conditions, and
    human activity. Understanding when and why extreme pollution episodes occur can help
    policymakers, public health agencies, and urban planners design better early-warning systems
    and interventions. The study aims to provide data-driven insights that support proactive
    responses rather than reactive measures, benefiting both decision-makers and the public.
    """)

   
    st.subheader("Illustrative Visual")

    chart_data = pd.DataFrame({
        "Year": [2015, 2017, 2019, 2021, 2023],
        "Average AQI": [210, 235, 260, 285, 300]
    })

    st.line_chart(chart_data.set_index("Year"))

    
    st.header("Stakeholders (Who is Affected?)")

    st.markdown("""
    Air pollution in Delhi directly affects residents through increased health risks and
    reduced quality of life, particularly for vulnerable populations such as children and
    the elderly. Healthcare systems experience increased strain during severe pollution
    episodes. Government agencies are responsible for policy enforcement and mitigation
    strategies. Schools and businesses may face disruptions during extreme events. Urban
    planners and environmental organizations rely on accurate data to guide long-term
    sustainability decisions. These stakeholders reflect the wide-ranging social, economic,
    and health impacts of air pollution.
    """)

    
    st.header("Existing Solutions & Gaps")

    st.markdown("""
    Existing solutions include air quality monitoring networks, emission control policies,
    and public health advisories. While these measures improve awareness, challenges remain
    due to sensor outages, inconsistent enforcement, and limited integration of environmental
    and social data. Many current approaches focus on short-term mitigation rather than
    identifying long-term recurring patterns.

    **References:**  
    World Health Organization (2021) - Air Quality Guidelines  
    Gupta et al. (2020) - Urban Air Pollution in India
    """)

    
    st.header("Blueprint for the Project")

    st.markdown("""
    The project will integrate air quality, meteorological, satellite-based, and public
    attention datasets related to Delhi. Exploratory data analysis will identify trends and
    anomalies. Temporal alignment will allow comparison across data sources. Seasonal and
    yearly patterns will be examined. Public attention indicators will be analyzed alongside
    pollution levels. The project emphasizes transparency and interpretability throughout
    the analysis process.
    """)

    
    st.header("Research Questions")

    st.markdown("""
    1. How have PM2.5 and AQI levels in Delhi changed over the past decade?  
    2. Are there recurring seasonal patterns in severe air pollution events?  
    3. How do temperature and wind speed relate to extreme AQI levels?  
    4. Do pollution episodes align with specific weather conditions?   
    5. How does public search interest change during high pollution periods?    
    6. Are pollution trends consistent across different years?  
    7. Can historical patterns indicate upcoming severe pollution episodes?    
    """)


with tab_proposal:
    st.header("Proposal Overview")

    st.markdown("""
    **Research Topic:**  
    Spatiotemporal analysis of air pollution and public response in Delhi.

    **Scope:**  
    - Analysis of PM2.5 and AQI trends  
    - Integration of weather and satellite data  
    - Examination of public attention indicators  

    **Focus:**  
    - Descriptive and comparative pattern analysis  
    - Long-term trend evaluation  
    """)


with tab_team:
    st.header("Team")

    cols = st.columns(4)

    with cols[0]:
        st.image("images/abhiram.jpg", width=150)
        st.markdown("""
        **Abhirama Karthikeya Mullapudi**  
        Data Lead  
        [LinkedIn](https://www.linkedin.com/in/abhiramakarthikeyamullapudi/) | [GitHub](https://github.com/abhiram17-1289)
        """)

    with cols[1]:
        st.image("images/nataraj.png", width=100)
        st.markdown("""
        **Natarajan Krishnan**  
        EDA Lead  
        [LinkedIn](http://www.linkedin.com/in/natarajan-krishnan-a99aa137a) | [GitHub](https://github.com/natarajankrishna)
        """)

    with cols[2]:
        st.image("images/thiyagu.png", width=150)
        st.markdown("""
        **Thiyagu Rajendran**  
        Visualization Lead  
        [LinkedIn](https://www.linkedin.com/in/thiyagu-r-a94b941a3/
        ) | [GitHub](https://github.com/thiyagu-17)
        """)

    with cols[3]:
        st.image("images/hari.jpg", width=150)
        st.markdown("""
        **Srihari Pulagalla**  
        Modelling Lead  
        [LinkedIn](https://www.linkedin.com/in/srihari-pulagalla-652558352/) | [GitHub](https://github.com/Srihari4589)
        """)

    st.markdown("---")
    st.markdown(
        "Our mission is to analyze air pollution data responsibly and communicate insights clearly."
    )


