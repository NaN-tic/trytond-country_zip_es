# -*- encoding: utf-8 -*-
#This file is part country_zip_es module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

{
    'name' : 'Spanish l10n - Country - Zip',
    'name_es_ES': 'Localización Española - País - Código Postal',
    'name_ca_ES': 'Localització Espanyola - Pais - Codi Postal',
    'version' : '0.0.1',
    'author' : 'Zikzakmedia SL',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''Provincias, municipios y códigos postales del Estado Español
Los datos han sido obtenidos de los datos públicos del Instituto Nacional de Estadística (INE) 
''',
    'description_es_ES': '''Provincias, municipios y códigos postales del Estado Español
Los datos han sido obtenidos de los datos públicos del Instituto Nacional de Estadística (INE) 
''',
    'description_ca_ES': '''Provincies, municipis i codis postals de l'Estat Espanyol
Les dades han sigut obtingudes de dades públiques de l'Institut Nacional de Estadística (INE). 
''',
    'depends' : [
        'country_zip',
    ],
    'xml' : [
        'country_zip_es.xml',
    ],
    'translation': [],
}
