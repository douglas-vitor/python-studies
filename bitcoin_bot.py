import ssl
import json

import websocket

#Bitstamp API Documentation
#https://www.bitstamp.net/api/
#https://www.bitstamp.net/websocket/v2/


def comprar():
    pass


def vender():
    pass


def ao_abrir(ws):
    print("Abriu a conexão")
    json_subscribe = """
    {
        "event": "bts:subscribe",
        "data": {
            "channel": "live_trades_btcusd"
        }
    }
    """
    ws.send(json_subscribe)


def ao_fechar(ws):
    print("Fechou a conexao")


def erro(ws, erro):
    print("Erro: ", erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem["data"]["price"]
    print(price)

    if price > 9000:
        vender()
    elif price < 8000:
        comprar()
    else:
        print("aguardar")


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
    on_open=ao_abrir,
    on_close=ao_fechar,
    on_message=ao_receber_mensagem,
    on_error=erro)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})