import CloudFlare

# Cloudflare API credentials
email = ""
api_key = ""
# Domain name
domain_name = ""

# Initialize CloudFlare API client
cf = CloudFlare.CloudFlare(email=email, token=api_key)

# Read IP addresses from ip.txt
with open("ip.txt", "r") as f:
    ip_addresses = f.read().splitlines()

# Create or update DNS records
for i, ip_address in enumerate(ip_addresses):
    record_name = f"{i+1}.{domain_name}"
    try:
        # Get zone ID
        zone_id = cf.zones.get(params={"name": domain_name})[0]["id"]

        # Get existing DNS records for the subdomain
        existing_records = cf.zones.dns_records.get(zone_id, params={"name": record_name})

        # Delete existing record if it exists
        if existing_records:
            for record in existing_records:
                cf.zones.dns_records.delete(zone_id, record["id"])
                print(f"Deleted existing DNS record for {record_name}")

        # Create new DNS record
        cf.zones.dns_records.post(
            zone_id,
            data={
                "name": record_name,
                "type": "A",
                "content": ip_address,
                "proxied": False  # Set to True if you want to use Cloudflare proxy
            }
        )
        print(f"Created DNS record for {record_name} with IP {ip_address}")
    except CloudFlare.exceptions.CloudFlareAPIError as e:
        print(f"Error updating DNS record for {record_name}: {e}")
