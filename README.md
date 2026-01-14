# POS Receipt Hide Odoo Branding

Odoo 19 module to hide "Powered by Odoo" branding from POS receipts with a configurable toggle.

![Before and After](screenshot.png)

## Features

- Hide "Powered by Odoo" branding from POS receipts
- Configurable via Settings (Toggle ON/OFF)
- Instant updates without closing the POS session (just refresh)

## Quick Start (Docker)

```bash
# Start Odoo + PostgreSQL
docker-compose up -d

# Access Odoo
open http://localhost:8069
# Login: admin / Password: admin

# Install the module
docker-compose exec odoo odoo -i pos_receipt_hide_odoo_branding -d odoo --stop-after-init
docker-compose restart odoo
```

## Manual Installation

1. Clone this repository into your Odoo `addons` directory
2. Restart your Odoo server
3. Go to **Apps**, search for `POS Receipt Hide Odoo Branding`, and click **Install**

## Configuration

1. Go to **Settings** > **Point of Sale** > **Bills & Receipts**
2. Enable **Hide 'Powered by Odoo'**
3. Save the settings
4. Refresh your POS session (F5) to apply changes

## Supported Versions

| Odoo Version | Branch | Status |
|--------------|--------|--------|
| **Odoo 19.0** | `main` | Active |

## License

[LGPL-3](LICENSE)
