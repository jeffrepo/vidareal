# -*- coding: utf-8 -*-

from odoo import api, models
import odoo.addons.l10n_gt_extra.a_letras as a_letras

class ReporteFacturaLibreria(models.AbstractModel):
    _name = 'report.vidareal.reporte_factura_libreria'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'account.move'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'a_letras': a_letras,
        }
