==========================================
Facturación Electrónica para Chile (FIXES)
==========================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-calyx--servicios%2Fl10n--cl-lightgray.png?logo=github
    :target: https://github.com/calyx-servicios/l10n-cl.git
    :alt: calyx-servicios/l10n-cl

|badge1| |badge2| |badge3|

This module  from the Chile Community localization of https://globalresponse.cl

**Table of contents**

.. contents::
   :local:

.. !!! Instalation: must only be present if there are very specific installation instructions, such as installing non-python dependencies.The audience is systems administrators. ] To install this module, you need to: !!!

Functional (Spanish)
====================

* FIX del metodo send_exchange (account.move): Hay un error en el código en uno de los métodos que se utilizan en medio del procesamiento de colas de envio.

    modulo:  l10n_cl_fe
    archivo: models/account_move.py
    clase: _inherit = "account.move"
    metodo:  def send_exchange(self):

    En la linea que indica:
        resp = self.env["sii.respuesta.cliente"].sudo().search([("exchange_id", "=", att.id)])
        resp.estado = "0"

        la clase sii.respuesta.cliente no tiene un atributo “estado”.

Bug Tracker
===========

* Contact to the development team

Credits
=======

Authors
~~~~~~~

* Calyx Servicios S.A.

Contributors
~~~~~~~~~~~~

* `Calyx Servicios S.A. <https://odoo.calyx-cloud.com.ar/>`_

  * Gaston Pablo Perez

Maintainers
~~~~~~~~~~~

This module is maintained by

.. image:: https://imgur.com/a/FPiTx23
   :alt: Calyx Servicios S.A.
   :target: https://odoo.calyx-cloud.com.ar/