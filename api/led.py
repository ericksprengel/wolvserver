import json

def get(handler):
  return json.dumps({
    "id": 9876,
    "message": "you GOT me. :P",
  })

def post(handler):
  dir(handler)
  # turn on your led here
  print("---> AQUI VC DAH A DEDADA")
  return json.dumps({
    "message": "led turned ON", "id": 123456
  })
