#!/usr/bin/env python3

from urllib.parse import unquote, urlparse, urlunparse
import base64
import ipaddress
import socket
import sys


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
    modified_url = parsed_url._replace(scheme='hxxps')  # FIXME
    modified_netloc = modified_url.netloc.replace('.', '[.]')
    modified_url = modified_url._replace(netloc=modified_netloc)
    return urlunparse(modified_url)


def get_resolved_dns(netloc):
    '''
    Resolve netloc to an IP or FQDN as appropriate

            Parameters:
                    netloc (str): A Base64-encoded string

            Returns:
                    (str): A resolved record
    '''
    if is_ip_address(netloc):
        return lookup_ptr(netloc)
    else:
        return resolve_hostname(netloc)


def lookup_ptr(ip_address):
    '''
    Resolve netloc to an IP or FQDN as appropriate

            Parameters:
                    ip_address (str): An IP address as a string

            Returns:
                    (str): A hostname, if resolvable
    '''
    try:
        # Perform reverse DNS lookup
        host_name, alias_list, ip_list = socket.gethostbyaddr(ip_address)

        return host_name
    except socket.herror:
        return f"No PTR record found for {ip_address}"
    except Exception as e:
        return f"An error occurred: {e}"


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


def is_ip_address(value):
    '''
    Determine whether value is an IP address or not

            Parameters:
                    value (str): A string

            Returns:
                    (bool): Is value an IP address or not?
    '''
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


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


def resolve_hostname(hostname):
    try:
        # Perform DNS lookup
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return f"Hostname {hostname} could not be resolved"
    except Exception as e:
        return f"An error occurred: {e}"


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
    print("Proto:", parsed_url.scheme)

    # Resolve netloc to an IP or hostname, if possible.
    resolved = get_resolved_dns(parsed_url.netloc)

    print("Netloc:", parsed_url.netloc, f"({resolved or ""})")
    print("Path:", parsed_url.path)
    print("Params:", parsed_url.params)
    print("Query:", parsed_url.query)

    # Parse and dump individual query items.
    queries = parsed_url.query.split('&')
    print("\tDecoded query details:")
    for item in queries:
        item_name, item_value = item.split('=')
        print("\t\t", item_name, '=', unquote(item_value))

    print("Fragment:", parsed_url.fragment)
    print("Username:", parsed_url.username)
    print("Password:", parsed_url.password)
    print("Hostname:", parsed_url.hostname)
    print("Port:", parsed_url.port)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter a URL: ")

    print_url(url)
    print("")  # Blank line
    print("Defanged:", defang_url(url))
