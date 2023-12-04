import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    # Extract URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for the POST request
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')

    # Send the POST request and display the response
    with urllib.request.urlopen(url, data=encoded_data) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
