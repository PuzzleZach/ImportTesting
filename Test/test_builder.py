from ..lib.core.api_factory import api_builder

def test_builder():
  endpoint = api_builder("/get-health")
  known_body = {"days_interval": 3}
  return endpoint.body == known_body
