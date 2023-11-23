from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
import warnings

warnings.filterwarnings("ignore")

# configurações do banco de dados: endereço, login, senha e o nome do bucket
cluster = Cluster("Couchbase://127.0.0.1",
                  ClusterOptions(PasswordAuthenticator("admin1", "admin1")))

bucket = cluster.bucket("produtos")
conexao = bucket.default_collection()

warnings.resetwarnings()

print("COUCHBASE CONECTADO")
print("BUCKET:", bucket.name, "\n")
