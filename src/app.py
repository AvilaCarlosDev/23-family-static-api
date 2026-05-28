"""
Family Static API - Flask Application
RESTful API for managing the Jackson family data
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
from datastructure import FamilyStructure

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if not member:
        return jsonify({"error": f"Member {id} not found"}), 404
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json()
    if not body or 'first_name' not in body:
        return jsonify({"error": "Missing first_name"}), 400
    new_member = jackson_family.add_member(body)
    return jsonify(new_member), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    success = jackson_family.delete_member(id)
    if not success:
        return jsonify({"error": f"Member {id} not found"}), 404
    return jsonify({"done": True}), 200

if __name__ == '__main__':
    app.run(debug=True, port=3000)
