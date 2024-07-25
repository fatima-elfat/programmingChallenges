"""
Challenge008: Find the domain name using an IP address.
For this Python challenge, you’ll want to import the Python socket library.
That’s the only hint. Write a function that accepts an IP address,
makes a DNS request, and returns the domain name
that maps to that IP address using PTR DNS records.
"""

import socket


def getDomaineName(IPAdress):
    """ Finds the domain name using an IP address.
    """
    try:
        hostname = socket.gethostbyaddr(IPAdress)[0]
        return hostname
    except socket.herror:
        return "Not found"


if __name__ == "__main__":
    print("should be Google:", getDomaineName("8.8.8.8"))
    print("should be OpenDNS:", getDomaineName("208.67.222.222"))
    print("should be Oracle:", getDomaineName("216.146.35.35"))
    print("should be NordVPN :", getDomaineName("103.86.99.100"))
