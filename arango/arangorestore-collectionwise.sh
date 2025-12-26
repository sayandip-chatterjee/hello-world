#!/bin/bash

# Assuming each line in the file "xyz" contains a collection name
# Adjust the path to your file accordingly
file_path="collections"

IFS=$'\n' read -d '' -r -a collection_file < "$file_path"

# Connection details
arangodb_pod="arangodb-deploy-crdn-bh34p7xb-4a075c"
input_directory="magic-backup"
arango_username="root"
arango_password="R0cKSTar5"
arango_endpoint="ssl://localhost:8529"

# Loop over each collection in the array
for collection_name in "${collection_file[@]}"; do
  echo $collection_name
  # Trim leading and trailing whitespaces (if any)
  collection_name=$(echo "$collection_name" | xargs)

  # Run arangorestore for the current collection
  kubectl exec -it "$arangodb_pod" -- sh -c "arangorestore --input-directory \"$input_directory\" \
    --server.endpoint \"$arango_endpoint\" \
    --server.username \"$arango_username\" \
    --server.password \"$arango_password\" \
    --all-databases false \
    --overwrite true \
    --server.authentication true \
    --server.database processTree \
    --collection \"$collection_name\""
done





## create 
## 1. getting collection names and storing them in a file
## 2. dump them as collections individually
## 3. recover as collections individually
## One script with multiple functions and invoke the function via some flag or switch