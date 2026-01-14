from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    receipt_hide_branding = fields.Boolean(
        string="Hide 'Powered by Odoo'",
        default=True
    )


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_receipt_hide_branding = fields.Boolean(
        related='pos_config_id.receipt_hide_branding',
        readonly=False
    )
