from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect("bot_data.sqlite")
    trades = con.execute("SELECT * FROM trades ORDER BY id DESC LIMIT 20").fetchall()
    con.close()
    html = """
    <h1>PASIYA-MD FOREX BOT BASE Dashboard</h1>
    <table border='1'>
      <tr><th>ID</th><th>Symbol</th><th>Signal</th><th>Result</th><th>Time</th></tr>
      {% for t in trades %}
      <tr><td>{{t[0]}}</td><td>{{t[1]}}</td><td>{{t[2]}}</td><td>{{t[3]}}</td><td>{{t[4]}}</td></tr>
      {% endfor %}
    </table>
    """
    return render_template_string(html, trades=trades)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
