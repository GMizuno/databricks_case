## Databricks

## Objetivo

## Tabelas e Esquemas

### Pedidos

- pedido_id (uuid4)
- loja_id (uuid4)
- entrega_id (uuid4)
- cliente
- status (faturado (80%), em processamento (15%), cancelado (5%))
- data_pedido (começa em 2024)
- qtd_produto (quantidade de produtos, maior que 0)
- valor_pedido (valor da compra, maior que 0)
- valor_frete (esse valor pode ser 0)

### Loja

- loja_id (uuid4)
- tipo (italiano, japones, fastfood, arabe, distruibuidora de bebida)
- latitude (considerar latitudes no brasil)
- longitude (considerar longitudes no brasil)

### Entrega

- entrega_id (uuid4)
- tipo de veiculo (moto, bicicleta e carro)
- latitude (considerar latitudes no brasil)
- longitude (considerar longitudes no brasil)
- data_inicio_entrega (essa data tem que ser de 20 ate 30 min maior que data_pedido)
- data_final_entrega (essa data tem que ser de 20 ate 90 min maior que data_inicio_entrega)