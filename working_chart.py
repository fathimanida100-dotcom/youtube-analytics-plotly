
import pandas as pd
import plotly.express as px
data = {
    "Video Title": ["Vid A", "Vid B", "Vid C"],
    "Category": ["Tutorial", "Vlog", "Review"],
    "Views": [10000, 25000, 15000],
    "Likes": [500, 1200, 800],
    "Watch Time (Hours)": [600, 1100, 400]
}
df = pd.DataFrame(data)
fig = px.scatter(df, x="Views", y="Likes", size="Watch Time (Hours)", color="Category", title="YouTube Matrix", size_max=40, template="plotly_dark")
fig.show()
