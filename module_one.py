import plotly.figure_factory as ff

# Read the Excel File and Pass Values Here

x_values = []

fig = ff.create_distplot(x_values, ['Distribution'], bin_size=.5, show_hist=False, show_rug=True)

fig.update_layout(legend=dict(itemsizing='constant'))
fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,  
        font = dict(family = "Arial", size = 10),
        bordercolor="LightSteelBlue",
        borderwidth=2,
    ),
    legend_title = dict(font = dict(family = "Arial", size = 20))
)

fig.update_xaxes(
                 ticks="outside",
                 tickwidth=3,
                 tickcolor='black',
                 tickfont=dict(family='Arial', color='black', size=20),
                 title_font=dict(size=46, family='Arial'),
                 title_text='Similarity Score',
                 ticklen=15,
                 range=[0, 1]
)

fig.update_yaxes(
                 ticks="outside", 
                 tickwidth=3,
                 tickcolor='black', 
                 title_text='Probability Density',
                 tickfont=dict(family='Arial', color='black', size=50),
                 title_font=dict(size=46, family='Arial'),
                 ticklen=15,
                 range=[0, 10]
)    

fig.update_layout(
    title_text="Total Distribution",
    title_font=dict(size=44, family='Arial'),
    template='simple_white',
    xaxis_tickformat = 'i',
    bargap=0.2,
    height=600,
    width=1000
)    

fig.write_image('distribution_plot.png')
