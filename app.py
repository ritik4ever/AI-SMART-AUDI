
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

def run_security_tools(contract_path):
    slither_result = subprocess.getoutput(f"slither {contract_path}")
    mythril_result = subprocess.getoutput(f"mythril analyze {contract_path}")
    return slither_result, mythril_result

@app.route('/analyze', methods=['POST'])
def analyze_contract():
    contract = request.files['contract']
    contract_path = f"./contracts/{contract.filename}"
    contract.save(contract_path)
    slither_result, mythril_result = run_security_tools(contract_path)
    return jsonify({
        "slither": slither_result,
        "mythril": mythril_result
    })

if __name__ == '__main__':
    app.run(debug=True)
