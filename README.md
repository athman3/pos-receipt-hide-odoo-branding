# POS Receipt Hide Odoo Branding

Odoo 19 module to hide "Powered by Odoo" branding from POS receipts.

![Before and After](screenshot.png)

## Features

- Automatically hides "Powered by Odoo" branding from POS receipts
- No configuration needed - install and it works
- Compatible with **Odoo Import Module** (ZIP installation)
- Lightweight: pure XML, no Python code

## Installation

### Option 1: Import Module (Recommended)

This is the easiest method, works on Odoo.com, Odoo.sh, and self-hosted instances.

1. Download `pos_receipt_hide_odoo_branding.zip` from [Releases](https://github.com/athman3/pos-receipt-hide-odoo-branding/releases)
2. Enable **Developer Mode** in Odoo (Settings > General Settings > Developer Tools)
3. Go to **Apps** > **Import Module**
4. Upload the ZIP file and click **Import**

### Option 2: Manual Installation

1. Clone this repository into your Odoo `addons` directory
2. Restart your Odoo server
3. Go to **Apps**, search for `POS Receipt Hide Odoo Branding`, and click **Install**

### Option 3: Docker Development

```bash
# Start Odoo + PostgreSQL
docker-compose up -d

# Access Odoo at http://localhost:8069
# Login: admin / Password: admin

# Install the module
docker-compose exec odoo odoo -i pos_receipt_hide_odoo_branding -d odoo --stop-after-init
docker-compose restart odoo
```

## Module Structure

```
pos_receipt_hide_odoo_branding/
├── __init__.py
├── __manifest__.py
└── static/src/xml/
    └── order_receipt.xml    # QWeb template override
```

This is a **data module** (importable module) - it contains only XML assets and no Python code, making it compatible with Odoo's Import Module feature.

## Supported Versions

| Odoo Version | Branch | Status |
|--------------|--------|--------|
| **Odoo 19.0** | `main` | Active |

## How It Works

The module extends the `point_of_sale.OrderReceipt` QWeb template and hides the "Powered by Odoo" branding section by setting `t-if="false"` on the relevant div.

## License

[LGPL-3](LICENSE)
