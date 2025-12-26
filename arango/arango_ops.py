import argparse
import subprocess

def backup_collections(arangodb_pod, output_directory, arango_username, arango_password, arango_endpoint, database_name):
    file_path = "collections"

    with open(file_path, 'r') as file:
        collection_file = [line.strip() for line in file.readlines()]

    # Loop over each collection in the array
    for collection_name in collection_file:
        print(collection_name)
        # Trim leading and trailing whitespaces (if any)
        collection_name = collection_name.strip()

        # Run arangodump for the current collection
        subprocess.run([
            "kubectl", "exec", "-it", arangodb_pod,
            "--", "sh", "-c",
            f"arangodump --output-directory '{output_directory}' "
            f"--server.endpoint '{arango_endpoint}' "
            f"--server.username '{arango_username}' "
            f"--server.password '{arango_password}' "
            "--all-databases false "
            "--overwrite true "
            "--server.authentication true "
            f"--server.database '{database_name}'"
            f"--collection '{collection_name}'"
        ])

def restore_collections(arangodb_pod, input_directory, arango_username, arango_password, arango_endpoint, database_name):
    file_path = "collections"

    with open(file_path, 'r') as file:
        collection_file = [line.strip() for line in file.readlines()]

    # Loop over each collection in the array
    for collection_name in collection_file:
        print(collection_name)
        # Trim leading and trailing whitespaces (if any)
        collection_name = collection_name.strip()

        # Run arangorestore for the current collection
        subprocess.run([
            "kubectl", "exec", "-it", arangodb_pod,
            "--", "sh", "-c",
            f"arangorestore --input-directory '{input_directory}' "
            f"--server.endpoint '{arango_endpoint}' "
            f"--server.username '{arango_username}' "
            f"--server.password '{arango_password}' "
            "--all-databases false "
            "--overwrite true "
            "--server.authentication true "
            f"--server.database '{database_name}'"
            f"--collection '{collection_name}'"
        ])

def main():
    parser = argparse.ArgumentParser(description="Backup or restore ArangoDB collections.")
    parser.add_argument("operation", choices=["backup", "restore"], help="Specify 'backup' or 'restore' operation.")
    parser.add_argument("--arangodb_pod", required=True, help="ArangoDB pod name.")
    parser.add_argument("--output_directory", help="Output directory for backup.")
    parser.add_argument("--input_directory", help="Input directory for restore.")
    parser.add_argument("--arango_username", default="root", help="ArangoDB username.")
    parser.add_argument("--arango_password", default="R0cKSTar5", help="ArangoDB password.")
    parser.add_argument("--arango_endpoint", default="ssl://localhost:8529", help="ArangoDB endpoint.")
    parser.add_argument("--database_name", required=True, help="ArangoDB database name.")

    args = parser.parse_args()

    if args.operation == "backup":
        backup_collections()
    elif args.operation == "restore":
        restore_collections()
    else:
        print("Invalid operation. Use 'backup' or 'restore'.")

if __name__ == "__main__":
    main()
