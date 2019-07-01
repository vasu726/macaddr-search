import requests
import sys
import json
from tabulate import tabulate

MAC_ADDR_IO_URL = "https://api.macaddress.io/v1?apiKey={}&output=json&search={}"

# TODO: Need to move this to a secret store
MAC_ADDR_API_KEY = "at_qhZ2imr7hQ6AD6f6nAx7ciuJIYTlb"


def help_string():
    return 'Usage: python2.7 macaddr-search/macaddr-search.py <macaddress>\n' \
           'Example: python2.7 macaddr-search/macaddr-search.py 44:38:39:ff:ef:57'


class MacAddrIOClient:
    macaddr_io_url = "https://api.macaddress.io/v1?apiKey={}&output=json&search={}"

    def search_macaddr(self, macaddr):
        url = self.macaddr_io_url.format(MAC_ADDR_API_KEY, macaddr)
        output = requests.get(url=url)
        if output.status_code != 200 and output.status_code != 404:
            sys.exit('could not find mac address {}. '
                     'Got response code {}, error message {}'.format(macaddr,
                                                                     output.status_code,
                                                                     output.text))
        json_output = json.loads(output.text)
        vendor_details = json_output.get("vendorDetails", "")
        return vendor_details.get("companyName", ""), vendor_details.get("companyAddress", ""), vendor_details.get(
            "countryCode", "")


def main():
    if len(sys.argv) < 2:
        sys.exit("missing argument: mac address\n\n{}".format(help_string()))

    client = MacAddrIOClient()
    mac_addr = sys.argv[1]
    company_name, address, country = client.search_macaddr("44:38:39:ff:ef:57")
    if len(company_name) == 0:
        sys.exit("could not find mac address {}".format(mac_addr))
    print tabulate(
        [['Mac Address', mac_addr], ['Company Name', company_name], ['Address', address], ['Country', country]],
        headers=['Description', 'Value'])


if __name__ == "__main__":
    main()
