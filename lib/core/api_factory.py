from ..auth.auth_system import get_token

class API_Endpoint:
  def __init__(self, endpoint, header, body):
    self.endpoint = endpoint
    self.header = header
    self.body = body

class API_Builder:
  def build(self, endpoint):
    header = {"token":get_token()}
    if endpoint == "/get-health":
      body = {"days_interval": 3}
      return API_Endpoint(endpoint, header, body)

def api_builder(endpoint):
  return API_Builder().build(endpoint)
