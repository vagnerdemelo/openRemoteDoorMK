from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/open_door/<int:block_unity_id>', methods=['GET'])
def open_door(block_unity_id):
    try:
        authorization = ""

        if block_unity_id == 1854:
            authorization = os.getenv("TOKEN_TEODORO")
        elif block_unity_id == 1876:
            authorization = os.getenv("TOKEN_PEDROSO")

        url = f"https://aws.magikey.com.br/api/v2/doors/{block_unity_id}/open"
        response = requests.put(url, headers={"Authorization": authorization})

        with open("log.txt", "a") as f:
            f.write(f"Status: {response.status_code} - {response.text}\n")
        return response.json(), response.status_code
    except Exception as e:
        with open("log.txt", "a") as f:
            f.write(f"Erro: {str(e)}\n")
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
