import random

from faker import Faker
from google.cloud import pubsub_v1
import json

def publish_message(publisher, project_id, topic_name, message):
    # Prepare the topic path
    topic_path = publisher.topic_path(project_id, topic_name)

    # Data must be a bytestring
    message_data = message.encode("utf-8")

    # Publish the message
    future = publisher.publish(topic_path, message_data)
    print(f"Published message ID: {future.result()}")

def publish_json_message(publisher, project_id, topic_name, message_dict):
    # Caminho do tópico
    topic_path = publisher.topic_path(project_id, topic_name)

    # Converter o dicionário Python em JSON
    message_data = json.dumps(message_dict).encode('utf-8')

    # Publicar a mensagem JSON
    future = publisher.publish(topic_path, message_data)
    print(f"Mensagem publicada com ID: {future.result()}")

if __name__ == "__main__":
    # Replace these with your project and topic details
    project_id = "databricks-estudo"
    topic_name = "databrick_files"
    print(f'Publicando no topico {topic_name}')
    fake = Faker("pt_BR")
    publisher = pubsub_v1.PublisherClient()
    for _ in range(100):
        message_dict = {
            "cliente_id": fake.uuid4(),
            "nome": fake.name(),
            "quantidade": random.randint(0, 10)
        }

        publish_json_message(publisher, project_id, topic_name, message_dict)
