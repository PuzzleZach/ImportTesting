from ..lib.auth.auth_system import get_token

def test_auth():
  token = get_token()
  return token == "Demo"
