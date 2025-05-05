import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv('hour.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season'] = df['season'].map({1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'})
    df['yr'] = df['yr'].map({0: '2011', 1: '2012'})
    df['weekday'] = df['weekday'].map({0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'})
    df['workingday'] = df['workingday'].map({0: 'No', 1: 'Yes'})
    df['hr'] = df['hr'].map({i: f"{i}:00" for i in range(24)})
    df['weathersit'] = df['weathersit'].map({1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'})
    return df

def filter_data(df):
    st.sidebar.header("Filter Data")
    year = st.sidebar.selectbox("Select Year", df['yr'].unique())
    seasons = st.sidebar.multiselect("Select Season(s)", df['season'].unique(), default=df['season'].unique())
    min_date, max_date = df['dteday'].min(), df['dteday'].max()
    start, end = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)
    filtered = df[(df['yr'] == year) & (df['season'].isin(seasons)) & (df['dteday'] >= pd.to_datetime(start)) & (df['dteday'] <= pd.to_datetime(end))]
    return filtered

def plot_bar_chart(df, group_col, value_col, title):
    st.subheader(title)
    grouped = df.groupby(group_col)[value_col].sum().sort_values()
    st.bar_chart(grouped)

def plot_line_chart(df, x_col, y_col, title):
    st.subheader(title)
    st.line_chart(df[[x_col, y_col]].set_index(x_col))

def plot_boxplot(df, x_col, y_col, title):
    st.subheader(title)
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
    st.pyplot(fig)

def plot_area_chart(df, group_cols, value_col, title):
    st.subheader(title)
    grouped = df.groupby(group_cols)[value_col].sum().unstack().fillna(0)
    st.area_chart(grouped)

def plot_scatter_plot(df, x_col, y_col, hue_col, title):
    st.subheader(title)
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, ax=ax)
    st.pyplot(fig)

def plot_heatmap(df, cols, title):
    st.subheader(title)
    fig, ax = plt.subplots()
    sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

def plot_pie_chart(df, group_col, value_col, title):
    st.subheader(title)
    grouped = df.groupby(group_col)[value_col].sum()
    fig, ax = plt.subplots()
    ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

def plot_bar_chart_multi_col(df, value_cols, title):
    st.subheader(title)
    totals = df[value_cols].sum()
    st.bar_chart(totals)

