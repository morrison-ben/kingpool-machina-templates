import requests


def fetch_mappings(request_data):
    
    print("request_data", request_data)

    url = "https://bolsadeaposta.bet.br/client/api/jumper/feedSports/inplayInfo/eventsRadar"

    response = requests.get(url, headers={})

    print("response", response)

    return {"status": True, "data": response.json(), "message": "Model loaded."}


def fetch_markets(request_data):

    params = request_data.get("params")

    event_id = params.get("event_id")

    market_id = params.get("market_id")

    url = f"https://mexchange-api.bolsadeaposta.bet.br/api/events/{event_id}"

    if market_id:
        url = f"{url}?market-ids={market_id}"

    print("url", url, market_id)

    response = requests.get(url, headers={})

    return {"status": True, "data": response.json(), "message": "Model loaded."}
