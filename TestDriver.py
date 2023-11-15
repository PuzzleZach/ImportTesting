from .Test.test_auth import test_auth
from .Test.test_builder import test_builder

# Would use unittest in practice but this is faster.
if __name__ == "__main__":
  auth = test_auth()
  build = test_builder()
  print(f"The result of our auth test is {auth} and the result for our build test is {build}")
