# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "l10n cl stock picking dte layout",
    "summary": """
        Fix DTE layout for Stock Picking on CL
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["<Github Username/s>"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Stock/picking",
    "version": "14.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["base",
                "l10n_cl_stock_picking"],
     'data': ['views/layout.xml'],
}
