from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Recebi uma requisição na rota /webhook")

    if not request.is_json:
        print("Invalid Content-Type")
        return jsonify({'error': 'Invalid Content-Type'}), 400
    
    try:
        # Verificar se os dados estão vindo corretamente
        print("request: ", request.get_json())
        data = request.json
        print(f"Dados recebidos: {data}")
    except Exception as e:
        print(f"Erro ao obter JSON: {e}")
        return jsonify({'error': 'Invalid JSON'}), 400

    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    user_message = data.get('text')
    user_number = data.get('from')

    print(f"Mensagem: {user_message}, Número: {user_number}")

    if not user_message or not user_number:
        return jsonify({'error': 'Missing fields'}), 400

    return jsonify({'message': 'Requisição recebida com sucesso'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
