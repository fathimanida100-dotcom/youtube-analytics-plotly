
import pandas as pd
import plotly.express as px

df = pd.read_csv("youtube_data.csv")

# Remove total summary rows if they exist
if "Video title" in df.columns:
    df = df[df["Video title"] != "Total"]

# Dynamic column detection fallback
x_col = "Views" if "Views" in df.columns else df.columns[1]
y_col = "Likes" if "Likes" in df.columns else df.columns[2]
hover_col = "Video title" if "Video title" in df.columns else df.columns[0]

fig = px.scatter(
    df, 
    x=x_col,
    y=y_col,
    hover_name=hover_col,
    title="Real YouTube Channel Metrics",
    template="plotly_dark"
)

fig.show()
