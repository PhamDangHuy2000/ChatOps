import requests

access_token = "MDRjZTBhYTEtM2UyZS00ZDAzLWFiNWEtMTlhZDE5MGE1NThlZTNlZjRlY2QtNWU2_P0A1_d0b89fcd-d5f4-4ad4-862a-e756c6dc6d5c"

base_url = "https://webexapis.com/v1/"


def get_bot_id():
    url = f'{base_url}/people/me'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    return response.json()['id']

bot_id = get_bot_id() # gán id lấy được vào biến bot_id

def get_message(message_id):
    url = f'{base_url}/messages/{message_id}'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    msg_text = response.json()['text']

    return msg_text

def post_message(room_id, text):
    url = f'{base_url}/messages'

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    data = {
        "roomId": room_id,
        "text": text
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.content)

if __name__ == "__main__":
    # get_message("Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL01FU1NBR0UvYTQ1ZjE5NjAtNzIxYy0xMWVkLTlkN2YtZGJjNzU2MTNhZjQy")
    #post_message("Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vM2U4MTdiZTAtNzFhMS0xMWVkLWI2M2UtYmI2YmYwZjlkMDcx", "hello huy")
    print(bot_id)
