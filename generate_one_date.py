import math
import random
from datetime import datetime

from faker import Faker

from utils.const import (
    TIPOS_LOJA, STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS, TIPOS_VEICULO,
)
from utils.generator import criar_entregas, criar_lojas, criar_pedidos
from utils.writer import write_json_by_date, write_parquet, write_parquet_by_date, write_json

NUM_PEDIDOS = 1_000
NUM_LOJAS = math.ceil(NUM_PEDIDOS * 0.05)

seed_value = 12345
fake = Faker("pt_BR")
fake.seed_instance(seed_value)
random.seed(seed_value)
today = datetime.today()

dates = {
    'start_date': datetime(today.year, today.month, today.day),
    'end_date': datetime(today.year, today.month, today.day),
}

lojas = criar_lojas(NUM_LOJAS, TIPOS_LOJA, fake)
pedidos = criar_pedidos(NUM_PEDIDOS, lojas, fake, STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS, dates)
entregas = criar_entregas(pedidos, TIPOS_VEICULO)

write_parquet_by_date(pedidos, 'data_pedido', 'data/pedidos/pedido')
write_json(lojas, 'data/lojas/lojas.json')
write_json_by_date(entregas, 'data_inicio_entrega', 'data/entregas/entrega')
