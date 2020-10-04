import os
import pika
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# channel = connection.channel()

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def get_ui():
    return send_from_directory('ui', 'almanza.html')

def set_connection():
    ip_rabbit = os.environ['RABBITMQ']
    connection = pika.BlockingConnection(pika.ConnectionParameters(ip_rabbit))
    channel = connection.channel()
    channel.queue_declare(queue='alvaroalmanza')
    if channel.is_open:
        print("rabbitqm is open")
    return channel

@app.route('/push', methods=['POST'])
def send_message():
    values = request.get_json()
    print(values)
    if not values:
        response = {
            'message': 'No data found'
        }
        return jsonify(response), 400
    channel.basic_publish(exchange='',routing_key='hello',body = str(values) )
    # if success:
    #     response = {
    #         'message': 'Successfully added transaction'
    #     }
    return jsonify('ok'), 201

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p','--port', type=int, default=8080)
    args = parser.parse_args()
    port = args.port
    channel = set_connection()
    app.run(host='0.0.0.0',port=port)
    