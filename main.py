import random
import json

from faker import Faker

from utils.const import (
    STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS, TIPOS_VEICULO,
)
from utils.generator import criar_entregas, criar_pedidos
from utils.writer import write_json, write_parquet

from datetime import date

hoje = date.today()
data_formatada = hoje.strftime("%Y-%m-%d")

NUM_PEDIDOS = 5_000

seed_value = 1231231
fake = Faker("pt_BR")
fake.seed_instance(seed_value)
random.seed(seed_value)

lojas = json.load(open("data/lojas/lojas.json"))
pedidos = criar_pedidos(NUM_PEDIDOS, lojas, fake, STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS)
entregas = criar_entregas(pedidos, TIPOS_VEICULO)

write_parquet(pedidos, f'pedido_{data_formatada}.parquet')
write_json(entregas, f'entrega_{data_formatada}.json')