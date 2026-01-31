# TODO:
# Import json library
# Import fetch_data from client.api_client
# Import validate_items from utils.validators
# In the main function:
#   - fetch items from the API using the fetch_data function
#   - validate the received items using the validate_items function
#   - open the JSON file and write items as formatted JSON

def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    # Fetch items

    print("Validating items…")
    # Validate items

    json_file_path = "data/posts.json"
    # Save JSON data into the file

if __name__ == "__main__":
    main()