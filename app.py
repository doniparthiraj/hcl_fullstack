from flask import Flask, request, jsonify
from flask_cors import CORS
from dbhelper import db_helper
import networkx as nx
import pandas as pd

csv_file = "links.csv"
df = pd.read_csv(csv_file)

G = nx.DiGraph()

for _, row in df.iterrows():
    G.add_edge(row["From"], row["To"], weight=row["Time"])

start_node = "A" 
end_node = "F"
try:
    shortest_path = nx.dijkstra_path(G, start_node, end_node, weight="weight")
    shortest_distance = nx.dijkstra_path_length(G, start_node, end_node, weight="weight")

    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
    print(f"Shortest distance: {shortest_distance}")
except nx.NetworkXNoPath:
    print(f"No path found between {start_node} and {end_node}")

all_distances = nx.single_source_dijkstra_path_length(G, start_node, weight="weight")

print("\nShortest distances from node A:")
for node, distance in all_distances.items():
    print(f"{node}: {distance}")

app = Flask(__name__)
CORS(app)

@app.route('/add_bank', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.add_bank(
        data['bank_name'],
        data['charges']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/add_user', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.add_user(
        data['name'],
        data['phone_number'],
        data['account_number'],
        data['balance'],
        data['bank_name']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/link_bank', methods=['POST'])
def AddUser():
    data = request.json
    response = db_helper.link_bank(
        data['from'],
        data['to']
    )
    return jsonify(response), response[1] if isinstance(response, tuple) else 200


@app.route('/fast_route', methods=['POST'])
def FastRoute():
    data = request.json
    response = check(data)
    response = find_fastroute(data["from"],data["to"])
    return jsonify(response), response[1] if isinstance(response, tuple) else 200

if __name__ == '__main__':
    app.run(debug=True)
