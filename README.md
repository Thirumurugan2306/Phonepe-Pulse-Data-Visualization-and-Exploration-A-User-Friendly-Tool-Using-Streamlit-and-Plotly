# Phonepe-Pulse-Data-Visualization-and-Exploration-A-User-Friendly-Tool-Using-Streamlit-and-Plotly

This repository contains a Python script for creating a web app using Streamlit to visualize insights from Phonepe Pulse data.

#Requirements
The following packages are required to run the code:

pandas
PIL
streamlit
webbrowser
streamlit_option_menu
plotly
sqlalchemy

#What is Phonepe Pulse?

Phonepe pulse is launched for getting accurate and comprehensive data on digital payment transaction trends in India

Phonepe Pulse webiste mostly shows more than 2000+ transactions done by the consumers on interactive map of India.

Phonepe Pulse is India's first interactive geospatial platform on digital payments.

They have shared the transaction data in Github repository for easy access for everyone

Problem Statement
The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.

#Usage

The web app will open in a browser window. The app allows the user to navigate between three sections: HOME, GEO-INSIGHTS, and DASHBORD.
##HOME
The HOME section displays the title and navigation bar.
##GEO-INSIGHTS
The GEO-INSIGHTS section displays a map visualization of transaction data.
The geo_insights function first creates two columns using the st.columns method, which will be used to display the visualizations and insights side by side. The user is prompted to select the type of data they want to see (transactions or users), the metric they want to use (count or amount), the year, and the quarter using streamlit widgets. Depending on the user's selection, the app filters the transaction data to include only the selected year and quarter and creates various visualizations using Plotly.

The choropleth map shows the total transaction count or amount for each state in India. The user can hover over each state to see the state name and the transaction count or amount. The map also includes a color scale to indicate the magnitude of the count or amount.

The app also displays various insights related to the selected data. For example, it displays the total transaction count or amount for all states, the total transaction count, and the amount for each category of transaction. The app also uses CSS styling to improve the appearance of the visualizations and insights.



The DASHBORD section displays various visualizations of transaction and user data.

###Data Source
The script reads data from a MySQL database called 'Phonepe_Pulse'. The following tables are used:

aggregated_transactions
aggregated_user
map_transaction
map_user
top_transaction
top_user
