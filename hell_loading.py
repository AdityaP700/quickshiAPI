import os

# Messy Fix 1: Global variable + Environment check
if os.getenv("ENV") != "TESTING":
    embedding_model = load_2gb_model()  # Breaks if you forget to set the env var
    redis_client = connect_to_redis()
else:
    embedding_model = None  # Forces you to write dirty 'if' checks everywhere


##Brittle Code: It relies heavily on
# environment variables (ENV="TESTING").
#  If a developer forgets to set this
#  flag in a new test suite, the entire test suite freezes for minutes trying to download/load a 2GB model.Side Effects: Importing main.py still triggers unexpected logic. It violates the "Separation of Concerns" principle because the file is managing its own system state during an import statement.Polluted Global Namespace: It makes mocking incredibly difficult because the testing framework has to monkeypatch variables that might or might not exist depending on
#  when the file was imported.