======================
l10n Chile VAT Checker
======================

.. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is intended to be in every module    !!
   !! to explain why and how it works.               !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


.. User https://shields.io for badge creation.
.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-PersiscalConsulting%2Fnubox-lightgray.png?logo=github
    :target: https://github.com/PersiscalConsulting/nubox
    :alt: PersiscalConsulting/nubox

|badge1| |badge2| |badge3|

.. !!! Description must be max 2-3 paragraphs, and is required.

* This module overwrite the Vat Check Method from the Chile Odoo Community localization of https://globalresponse.cl

**Table of contents**

.. contents::
   :local:

.. !!! Instalation: must only be present if there are very specific installation instructions, such as installing non-python dependencies.The audience is systems administrators. ] To install this module, you need to: !!!

Functional (Spanish)
====================

Se sobreescribe el método de validación de RUT que trae la localización chilena en el módulo `l10n_cl_fe`. No se estaban reemplazando los guiones o comas.

Ahora el campo `document_number` de la localización se oculta (SE MUESTRA EN CASO DE ACTIVAR EL MODO DESARROLLADOR), y se escribe con los datos del campo `vat` en caso de que estos correspondan a las validaciones de ser un campo con un RUT válido.

El campo `document_type_id` (Document type) ahora se oculta en caso de que el tipo de número de identificación sea RUT, ya que es un dato duplicado en ese caso.

Known issues / Roadmap
======================

* Nothing at the moment.

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

  * Federico Gregori

Maintainers
~~~~~~~~~~~

This module is maintained by

.. image:: https://imgur.com/a/FPiTx23
   :alt: Calyx Servicios S.A.
   :target: https://odoo.calyx-cloud.com.ar/