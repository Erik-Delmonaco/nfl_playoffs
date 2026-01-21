import sqlite3
import gradio as gr
import pandas as pd

def fetch():
    conn = sqlite3.connect('teams_database.db')
    cursor = conn.cursor()

    query = """
        SELECT *
        FROM teams;
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    points = [(len(record[1]),len(record[2])) for record in records]
    points_df = pd.DataFrame(points,columns = ('x','y'))
    return points_df


iface = gr.Interface(fn = fetch,inputs = [], outputs = gr.LinePlot(x = 'x',y = 'y',x_lim = (0,15),y_lim = (0,15)))

iface.launch()