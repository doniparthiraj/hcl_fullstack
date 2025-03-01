from flask import Flask, request, jsonify
from flask_cors import CORS
from dbhelper import db_helper
import networkx as nx
import pandas as pd

class initial_graph:
    def __init__(self):
        self.G1 = nx.DiGraph()
        links=fdbhelper.get_links()
        for e1,e2,w in links:
            self.G1.add_edge(e1,e2,weight=w)

        self.G2 = nx.DiGraph()
        charges=fdbhelper.get_charges()
        self.node_weights={}
        for node,ch in charges:
            self.node_weights[node]=ch

        for e3,e4,_ in links:
            self.G2.add_edge(e3,e4,weight=node_weights[e3])

    def find_fast_route(self,start_node,end_node):
        try:
            shortest_path = nx.dijkstra_path(self.G1, start_node, end_node, weight="weight")
            shortest_distance = nx.dijkstra_path_length(self.G1, start_node, end_node, weight="weight")
            # print(f"Shortest distance: {shortest_distance}")
            path=f"Successfully find route: Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}
            response={
                "path":path
                "charge":shortest_distance
            }
            return jsonify(response),200
        except nx.NetworkXNoPath:
            return jsonify({"error": f"No path found between {start_node} and {end_node}"}), 500

    def find_cheap_route(self,start_node,end_node):
        try:
            shortest_path = nx.dijkstra_path(self.G2, start_node, end_node, weight="weight")
            shortest_distance = nx.dijkstra_path_length(self.G2, start_node, end_node, weight="weight")
            path=f"Successfully find route: Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}
            response={
                "path":path
                "charge":shortest_distance
            }
        except nx.NetworkXNoPath:
            print(f"No path found between {start_node} and {end_node}")

Graph_object=initial_graph()

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
