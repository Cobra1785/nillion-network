import os

# Alice
CONFIG_PARTY_USER = {
    "userkey_file": os.getenv("NILLION_USERKEY_PATH_PARTY_1"),
    "nodekey_file": os.getenv("NILLION_NODEKEY_PATH_PARTY_1"),
    "nodekey_alternate_file": os.getenv("NILLION_NODEKEY_PATH_PARTY_4"),
    "party_name": "User"
}

CONFIG_PARTY_SYSTEM = {
        "userkey_file": os.getenv("NILLION_USERKEY_PATH_PARTY_2"),
        "nodekey_file": os.getenv("NILLION_NODEKEY_PATH_PARTY_2"),
    "party_name": "System"
}

# Bob and Charlie
# CONFIG_N_PARTIES = [
#     {
#         "userkey_file": os.getenv("NILLION_USERKEY_PATH_PARTY_2"),
#         "nodekey_file": os.getenv("NILLION_NODEKEY_PATH_PARTY_2"),
#         "party_name": "Bob",
#         "secret_name": "bob_salary",
#         "secret_value": 8000,
#     },
#     {
#         "userkey_file": os.getenv("NILLION_USERKEY_PATH_PARTY_3"),
#         "nodekey_file": os.getenv("NILLION_NODEKEY_PATH_PARTY_3"),
#         "party_name": "Charlie",
#         "secret_name": "charlie_salary",
#         "secret_value": 12000,
#     },
# ]