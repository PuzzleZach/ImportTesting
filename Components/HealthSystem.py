from ..lib.core.api_factory import api_builder

def build_health_system():
  get_health = api_builder("/get-health")
  if get_health:
    # Testing our Health endpoint here.
    pass

if __name__ == "__main__":
  build_health_system()
