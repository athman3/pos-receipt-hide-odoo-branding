/** @odoo-module */

import { PosData } from "@point_of_sale/app/services/data_service";
import { patch } from "@web/core/utils/patch";

patch(PosData.prototype, {
    async setup(...args) {
        await super.setup(...args);
        // After POS data is loaded, refresh the receipt_hide_branding field from server
        await this.refreshBrandingSetting();
    },

    async refreshBrandingSetting() {
        try {
            const configId = odoo.pos_config_id;
            if (!configId) return;
            
            // Fetch the current value of receipt_hide_branding from the server
            const result = await this.orm.read("pos.config", [configId], ["receipt_hide_branding"]);
            
            if (result && result.length > 0) {
                const config = this.models["pos.config"].get(configId);
                if (config) {
                    config.receipt_hide_branding = result[0].receipt_hide_branding;
                }
            }
        } catch (error) {
            console.warn("Could not refresh branding setting:", error);
        }
    }
});
