import sqlite3
import gradio as gr
import pandas as pd

def fetch_teams():
    conn = sqlite3.connect('teams_database.db')
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM teams;

    """
    cursor.execute(query)

    results = cursor.fetchall()

    conn.close()

    df = pd.DataFrame(results,columns = ["id","city","name"])

    return df

iface = gr.Interface(
    fn = fetch_teams,
    inputs = []
)