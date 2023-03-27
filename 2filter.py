
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

df =  pd.read_csv('world_happiness_data.csv',sep = ',', engine = 'python')
st.title ("WORLD HAPPINESS REPORT")
#st.header("Interactive visualization")
st.subheader("Happiness against Freedom,Social Support & GDP")
st.caption("FILTER1 : :blue[Please select required area in any of the scatter plots(individually)]")

###############################################################
#Interactive-graphs
select = alt.selection(type='interval')
click = alt.selection_multi(encodings=['color'])

#scatter-plot
scatter = alt.Chart(df).mark_point().encode(
    y='Happiness_score', tooltip=['average(Happiness_score)'],
    color=alt.condition(select, 'Region', alt.value('lightgray'), legend=None)).add_selection(select).transform_filter(click)
#Bar-plot
bars = alt.Chart(df).mark_bar().encode(
    y='Region',color=alt.condition(click, 'Region', alt.value('lightgray')),
    x= alt.X('count(Region)',scale=alt.Scale(domain=[0, 500]))
    ).add_selection(click).transform_filter(select).properties(width=150, height=250).properties(title='FILTER2 : Please select any region')
#scatter and Bar plot
scatter.encode(alt.X(
    'Social_support',scale=alt.Scale(zero=False))).properties( height=250,width=230).properties(title='Happiness VS Social_support')|scatter.encode(alt.X(
    'GDP_per_capita',scale=alt.Scale(zero=False))).properties( height=250,width=230).properties(title='Happiness VS GDP')|scatter.encode(alt.X(
    'Freedom',scale=alt.Scale(zero=False))).properties( height=250,width=230).properties(title='Happiness VS Freedom') | bars

###############################################################


#barplot
st.subheader("Happiness by region")
df2 = df[['Region','Happiness_score']]  
bar2 = alt.Chart(df2, title='Tooltip: happiness score for each region').mark_bar(opacity=0.3,).encode(
    alt.X('Region',scale=alt.Scale(zero=False)),
    alt.Y('mean(Happiness_score)',scale=alt.Scale(zero=False),title='Happiness score'), tooltip= 'mean(Happiness_score)', color= 'Region', opacity= "online:O").interactive()
st.altair_chart(bar2, use_container_width=True)


#Line
st.subheader("Happiness Trend ")
chart_data2 = df[["Happiness_score","year"]]
line = alt.Chart(chart_data2, title='World Happiness Trend over the years').mark_line().encode(
    alt.X('year',scale=alt.Scale(domain=(2008,2022), clamp=True)),
    alt.Y('mean(Happiness_score)',scale=alt.Scale(zero=False),title='Happiness score'))
st.altair_chart(line, use_container_width=True)
