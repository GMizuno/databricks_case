import math
import random

from faker import Faker

from utils.const import (STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS, TIPOS_LOJA, TIPOS_VEICULO, TIPOS_CLIENTES)
from utils.generator import criar_clientes, criar_entregas, criar_lojas, criar_pedidos
from utils.writer import write_json, write_json_by_date, write_parquet_by_date, write_parquet

NUM_PEDIDOS = 1_000
NUM_CLIENTES = 330
NUM_LOJAS = math.ceil(NUM_PEDIDOS * 0.05)

seed_value = 12345
fake = Faker("pt_BR")
fake.seed_instance(seed_value)
random.seed(seed_value)

lojas = criar_lojas(NUM_LOJAS, TIPOS_LOJA, fake)
clientes = criar_clientes(NUM_CLIENTES, TIPOS_CLIENTES, fake)
pedidos = criar_pedidos(NUM_PEDIDOS, lojas, clientes, fake, STATUS_PEDIDO_CHOICES, STATUS_PEDIDO_WEIGHTS)
entregas = criar_entregas(pedidos, TIPOS_VEICULO)

write_parquet_by_date(pedidos, 'data_pedido', 'data/pedidos/pedido')
write_parquet(clientes, 'data/clientes/cliente.parquet')
write_json(lojas, 'data/lojas/lojas.json')
write_json_by_date(entregas, 'data_inicio_entrega', 'data/entregas/entrega')
