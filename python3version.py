import urllib.request  as urllib2
from urllib.request import Request, urlopen 
from bs4 import BeautifulSoup  
import pandas as pd
import matplotlib.pyplot as plt


# Specify the url
atp = "http://www.atpworldtour.com/en/rankings/singles"

# Query the website and return the html to the variable 'page'
req = Request(atp, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req)

# The document is parsed as a tree, could have passed the html file directly also like open("index.html").
soup = BeautifulSoup(page)

# We want a table of rank vs points
rank = []
points = []

# Get the large table (non-generic stuff is table name, columns)
table = soup.find('table', attrs={'class':'mega-table'})
table_body = table.find('tbody')

# Get all the rows to iterate over them
rows = table_body.find_all('tr')

# Build our own data by picking the required columns for each row
for row in rows:

    cols = row.find_all('td')
    cols = [str(ele.text.strip()).replace(',','') for ele in cols] 

    # rank
    rank.append(cols[0])

    # points
    points.append(cols[5])

# Create a variable of the value of the columns
columns = {'Points': points,'Rank': rank}

# Create a dataframe from the columns variable
df = pd.DataFrame(columns)
df = df[df.columns[::-1]]

# Convert to float (For plotting, as columns are still string objects)
df.Rank = df.Rank.astype(float)
df.Points = df.Points.astype(float)

# Plot and save.   Sample here: https://postimg.org/image/b02k5093v/ 
ax = df.plot(x='Rank', y='Points', kind='line') 

# kind= area, pie, hist...etc. density/kde is the most useful i guess. line is the default. 
ax.set_xlabel("Rank")
ax.set_ylabel("Points")

# Another plot for density, not saved though. Sample here: https://postimg.org/image/5zdqf0qg5/
df.plot(x='Rank', y='Points', kind='density')

plt.show()
fig = ax.get_figure()
fig.savefig('menstennis.png')

# Many things can be done. Like age distribution of players.
# Instead of points we have age in column 4, and then do a kde or density plot.
# Sample here: https://postimg.org/image/ts39cz6cr/
