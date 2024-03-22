import pandas 
import matplotlib.pyplot as pt
from pandas import DataFrame  as df
filenames = ["dhoni.txt","virat.txt","sachin.txt","yuvraj.txt"]
names = ["Date","Country","Runs","Balls"]
dataframe = df()
for file in filenames:
    player = file.replace(".txt","")
    frame = pandas.read_csv(file , sep = "\s+",names = names)
    frame["player"]= player
    frame["StrikeRate"] = frame ["Runs"]/frame["Balls"]*100
    dataframe = pandas.concat([dataframe,frame])
print(dataframe.columns)
pt.figure(figsize=(9,6))
for player , player_data in dataframe.groupby("player"):
    pt.plot(player_data["Date"],player_data["Runs"],label=player)
pt.xlabel("Date")
pt.ylabel("Runs")
pt.title("RUNS OVER TIME")
pt.legend()
pt.xticks(rotation=45)
pt.grid()
pt.show()
pt.figure(figsize=(9,6))
for player ,player_data in dataframe.groupby("player"):
    pt.plot(player_data["Date"],player_data["StrikeRate"],label=player)
pt.xlabel("Date")
pt.ylabel("StrikeRate %")
pt .title("StrikeRate Over time")
pt.legend()
pt.xticks(rotation=45)
pt.grid()
pt.show()
total_runs = dataframe[["player","Runs"]] .groupby("player").sum().reset_index()
pt.figure(figsize=(8,5))
pt.bar(total_runs["player"],total_runs["Runs"],color = ["Blue","Green","Yellow","Red"])
pt.xlabel("player")
pt.ylabel("Total Runs")
pt.title("EACH PLAYER RUNS OVER TIME")
pt.legend()
pt.grid(axis="y")
pt.show()


