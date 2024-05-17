#!/usr/bin/env python3

from urllib.parse import unquote, urlparse, urlunparse
import base64


def base64_decode_string(encoded_string):
    '''
    Returns the Base64-decoded string

            Parameters:
                    encoded_string (str): A Base64-encoded string

            Returns:
                    decoded_string (str): A Base64-decoded string
    '''
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    return decoded_string


def bytes_to_string(byte_data, encoding='utf-8'):
    '''
    Converts bytes to a string

            Parameters:
                    byte_data (bytes): Bytes
                    encoding (string): A text encoding to use. Default: utf-8

            Returns:
                    byte_data.decode(encoding)
    '''
    # Convert the byte data to a string using the specified encoding
    try:
        return byte_data.decode(encoding)
    except UnicodeDecodeError:
        return f"Cannot decode bytes with {encoding} encoding."


def defang_url(url):
    '''
    Make a URL safe for sharing.

            Parameters:
                    url (str): A Base64-encoded string

            Returns:
                    (str): A defanged URL
    '''
    parsed_url = urlparse(url)
    modified_url = parsed_url._replace(scheme='hxxps')
    modified_netloc = modified_url.netloc.replace('.', '[.]')
    modified_url = modified_url._replace(netloc=modified_netloc)
    return urlunparse(modified_url)


def hex_to_bytes(hex_string):
    '''
    Converts a string to bytes

            Parameters:
                    hex_string (str): A byte sequence in string format

            Returns:
                    bytes.fromhex (bytes): A byte sequence in bytes format
    '''
    # Convert the hexadecimal string to bytes
    return bytes.fromhex(hex_string)


def parse_url(url):
    '''
    Take a URL as a string and return a URL named tuple

            Parameters:
                    url (str): A URL in string format

            Returns:
                    urlparse(url) (tuple): Parse a URL into six components,
                    returning a 6-item named tuple
    '''
    return urlparse(url)


def print_url(url):
    '''
    Take a URL as a string and print a bunch of information about it

            Parameters:
                    url (str): A URL in string format

            Returns:
                    Prints a bunch of text about that URL.
    '''
    # Parse the URL into a URL object.
    parsed_url = urlparse(url)

    # Print each component of the URL.
    print("")  # Blank line
    print("Scheme:", parsed_url.scheme)
    print("Netloc:", parsed_url.netloc)
    print("Path:", parsed_url.path)
    print("Params:", parsed_url.params)
    print("Query:", parsed_url.query)

    # Parse and dump individual query items.
    queries = parsed_url.query.split('&')
    print("\tQuery Details:")
    for item in queries:
        item_name, item_value = item.split('=')
        print("\t\t", item_name, ':', unquote(item_value))

    print("Fragment:", parsed_url.fragment)
    print("Username:", parsed_url.username)
    print("Password:", parsed_url.password)
    print("Hostname:", parsed_url.hostname)
    print("Port:", parsed_url.port)


if __name__ == "__main__":
    url = input("Enter a URL: ")
    print_url(url)
    print("")  # Blank line
    print("Defanged:", defang_url(url))
