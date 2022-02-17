{
    "name": "l10n Chile VAT Checker",
    "summary": """
        This module overwrite the Vat Check from the Chile Community localization of https://globalresponse.cl
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["FedericoGregori"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Localization/Chile",
    "version": "14.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "l10n_cl_fe",
    ],
    "data": [
        "views/res_partner_views.xml",
    ],
}
