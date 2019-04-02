# -*- coding: utf-8 -*-
# Copyright 2017 Ignacio Ibeas <ignacio@acysos.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Suministro Inmediato de Información - Factura simplificada",
    "version": "11.0.0.1.0",
    "category": "Accounting & Finance",
    "website": "https://www.acysos.com",
    "author": "Acysos S.L.",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": ["zeep",
                   "requests"],
    },
    "depends": [
        "l10n_es",
        "l10n_es_aeat_sii",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/account_journal_data.xml",
        "views/res_company_view.xml",
        "views/account_invoice_view.xml",
    ],
    'images': ['static/description/banner.jpg'],
}
