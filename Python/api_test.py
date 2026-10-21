
import argparse
import ipaddress
import requests

parser = argparse.ArgumentParser(description="Subnet calculator API test")
parser.add_argument("subnet", help="Subnet IP, e.g. 192.168.1.0")
parser.add_argument("mask", help="CIDR prefix, e.g. 24")
args = parser.parse_args()


def api_call(subnet, mask):
    # Validate subnet and mask
    network = ipaddress.IPv4Network(
        f"{subnet}/{mask}", strict=False
    )

    url = f"https://networkcalc.com/api/ip/{network.network_address}/{network.prefixlen}"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    data = response.json()

    if data.get("status") != "OK":
        raise ValueError(f"API returned error: {data}")

    return data["address"]


def assignable_hosts(address):
    print(
        "There are",
        address["assignable_hosts"],
        "assignable hosts for the",
        address["cidr_notation"],
        "subnet"
    )


def first_host(address):
    print(
        "The first address is",
        address["first_assignable_host"]
    )


def mask_decimal(address):
    print(
        "The subnet mask in decimal form is",
        address["subnet_mask"]
    )


def mask_cidr(address):
    print(
        "The subnet mask in CIDR notation is",
        f"/{address['subnet_bits']}"
    )


if __name__ == "__main__":
    try:
        address = api_call(args.subnet, args.mask)

        assignable_hosts(address)
        first_host(address)
        mask_decimal(address)
        mask_cidr(address)

    except (ValueError, requests.RequestException, KeyError) as error:
        parser.exit(1, f"Error: {error}\n")
