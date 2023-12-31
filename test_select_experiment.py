import pandas as pd
import altair as alt
from vega_datasets import data
	iris = data.iris()
	tooltip = iris.columns.tolist()
	
	#Selector
	selector = alt.selection_point()
	condition = alt.condition(selector, 
	          "species:N", 
	          alt.value("lightgray")
	)
	
	chart = alt.Chart(iris).mark_point(filled=True).encode(
	    x=alt.X("petalLength"),
	    y=alt.Y("petalWidth"),
	    color = condition,
	    tooltip = tooltip
	).add_selection(selector)
	
chart