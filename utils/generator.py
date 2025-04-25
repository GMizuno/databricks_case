import random
from datetime import datetime, timedelta
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from faker import Faker

ESTADOS_UF = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

def random_latitude():
    return round(random.uniform(-33.7, 5.3), 6)


def random_longitude():
    return round(random.uniform(-73.9, -34.8), 6)


def criar_loja(tipos_lojas: list[str], fake: "Faker") -> dict:
    return {
        "loja_id": fake.uuid4(),
        "tipo": random.choice(tipos_lojas),
        "latitude": random_latitude(),
        "longitude": random_longitude(),
    }


def criar_cliente(tipos_clientes: list[str], fake: "Faker") -> dict:
    return {
        "client_id": fake.uuid4(),
        "tipo": random.choice(tipos_clientes),
        "estado": random.choice(ESTADOS_UF),
        "nome": fake.name(),
    }


def criar_lojas(qtd_lojas: int, tipos_lojas: list[str], fake: "Faker") -> list[dict]:
    return [criar_loja(tipos_lojas, fake) for _ in range(qtd_lojas)]


def criar_clientes(qtd_clientes: int, tipos_clientes: list[str], fake: "Faker") -> list[dict]:
    return [criar_cliente(tipos_clientes, fake) for _ in range(qtd_clientes)]


def criar_pedido(loja: dict, cliente: dict, fake: "Faker", status_pedido_choices, status_pedido_weights, dates: Optional[dict] =  None) -> dict:
    entrega_id = fake.uuid4()
    pedido_id = fake.uuid4()

    if dates is None:
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2025, 3, 29)
    else:
        start_date = dates["start_date"]
        end_date = dates["end_date"]

    status = random.choices(status_pedido_choices, weights=status_pedido_weights, k=1)[0]
    data_pedido = fake.date_time_between(start_date=start_date, end_date=end_date)

    return {
        "pedido_id": pedido_id,
        "loja_id": loja["loja_id"],
        "entrega_id": None if status in ["em processamento", "cancelado"] else entrega_id,
        "cliente_id": cliente["client_id"],
        "status": status,
        "data_pedido": data_pedido.strftime('%Y-%m-%d %H:%M:%S'),
        "qtd_produto": random.randint(1, 10),
        "valor_pedido": round(random.uniform(50, 500), 2),
        "valor_frete": round(random.choice([0, random.uniform(5, 50)]), 2),
    }


def criar_pedidos(qtd_pedidos: int, lojas: list[dict], clientes: list[dict], fake: "Faker", status_pedido_choices, status_pedido_weights, dates = None) -> list[dict]:
    return [criar_pedido(random.choice(lojas), random.choice(clientes), fake, status_pedido_choices, status_pedido_weights, dates) for _ in range(qtd_pedidos)]


def criar_entrega(pedido: dict, tipos_veiculo) -> Optional[dict]:
    data_pedido = pedido['data_pedido']
    data_inicio_entrega = datetime.strptime(data_pedido, "%Y-%m-%d %H:%M:%S") + \
                          timedelta(minutes=random.randint(20, 30))
    data_final_entrega = data_inicio_entrega + timedelta(minutes=random.randint(20, 90))

    if pedido["status"] != "cancelado":
        return {
            "entrega_id": pedido['entrega_id'],
            "tipo_veiculo": random.choice(tipos_veiculo),
            "latitude": random_latitude(),
            "longitude": random_longitude(),
            "data_inicio_entrega": data_inicio_entrega.strftime('%Y-%m-%d %H:%M:%S'),
            "data_final_entrega": data_final_entrega.strftime('%Y-%m-%d %H:%M:%S'),
        }


def criar_entregas(pedidos: list[dict], tipos_veiculo) -> list[dict]:
    return [
        criar_entrega(pedido, tipos_veiculo) for pedido in pedidos if
        criar_entrega(pedido, tipos_veiculo) is not None
    ]
