{
    "name": "l10n Chile Account Move 'exento' Method Override",
    "summary": """
        This module overrides the account move 'exento' method to apply a fix. The current official 'exento' method
        doesn't handle multiple taxes in the same account move line.
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
    "depends": [
        "l10n_cl_fe",
    ],
}
