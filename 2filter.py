# single-value selection over [Major_Genre, MPAA_Rating] pairs
# use specific hard-wired values as the initial selected values
import streamlit as st
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


df =  pd.read_csv('world_happiness_data.csv',sep = ',', engine = 'python')
st.title ("World happiness Report")
st.header("Interactive visualization")
st.subheader("Happiness_score VS Freedom")
st.caption("by Region")
st.caption(" Please expand and select the required area in the scatter")

st.subheader("Please select required area in the scatter plots or click the region in the bar graph")
st.caption("Please expand and click the required Region in the graph")

#Interactive graphs
select = alt.selection(type='interval')
click = alt.selection_multi(encodings=['color'])


#scatter plot
scatter = alt.Chart(df).mark_point().encode(
    y='Happiness_score',
    tooltip=['average(Happiness_score)'],
    color=alt.condition(select, 'Region', alt.value('lightgray'))).add_selection(select).transform_filter(click)

#Bar plot
bars = alt.Chart(df).mark_bar().encode(
    y='Region',
    color=alt.condition(click, 'Region', alt.value('lightgray')),
    x='count(Region)').add_selection(click).transform_filter(select).properties(width=800, height=100)

scatter.encode(
    alt.X('Freedom',scale=alt.Scale(zero=False)))|scatter.encode(
    alt.X('Social_support',scale=alt.Scale(zero=False))) |scatter.encode(
    alt.X('GDP_per_capita',scale=alt.Scale(zero=False))) & bars


#barplot
st.subheader("Happiness by region")
df2 = df[['Region','Happiness_score']]  

bar2 = alt.Chart(df2).mark_bar(opacity=0.3,).encode(
    alt.X('Region',scale=alt.Scale(zero=False)),
    alt.Y('mean(Happiness_score)',scale=alt.Scale(zero=False),title='Happiness score'), tooltip= 'Region', color= 'Region', opacity= "online:O").interactive()
st.altair_chart(bar2, use_container_width=True)

#Line
st.subheader("Happiness Trend -Interactive")
chart_data2 = df[["Happiness_score","year"]]


line = alt.Chart(chart_data2, title='World Happiness Trend over the years').mark_line().encode(
    alt.X('year',scale=alt.Scale(domain=(2008,2022), clamp=True)),
    alt.Y('mean(Happiness_score)',scale=alt.Scale(zero=False),title='Happiness score'))
st.altair_chart(line, use_container_width=True)
