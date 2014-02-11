#This file is part of country_zip_es module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from csv import reader
from trytond.model import ModelView
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Button, StateView, Wizard, StateTransition
import os

__all__ = ['LoadCountryZipsStart', 'LoadCountryZips']
__metaclass__ = PoolMeta


class LoadCountryZipsStart(ModelView):
    '''Load Country Zips Start'''
    __name__ = 'load.country.zips.start'


class LoadCountryZips(Wizard):
    '''Load Country Zips'''
    __name__ = "load.country.zips"

    start = StateView('load.country.zips.start',
        'country_zip_es.load_country_zips_start_view_form', [
            Button('Cancel', 'end', 'tryton-cancel'),
            Button('Accept', 'accept', 'tryton-ok', default=True),
            ])
    accept = StateTransition()

    @classmethod
    def __setup__(cls):
        super(LoadCountryZips, cls).__setup__()
        cls._error_messages.update({
                'error': 'CSV Import Error!',
                'read_error': 'Error reading file: %s.\nError raised: %s.',
                })

    def transition_accept(self):
        pool = Pool()
        Subdivision = pool.get('country.subdivision')
        CountryZip = pool.get('country.zip')

        delimiter = ','
        quotechar = '"'
        data = open(os.path.join(
                os.path.dirname(__file__), 'country_zip_es.csv'))
        try:
            rows = reader(data, delimiter=delimiter, quotechar=quotechar)
        except TypeError, e:
            self.raise_user_error('error',
                error_description='read_error',
                error_description_args=('bank.csv', e))
        rows.next()

        for row in rows:
            if not row:
                continue

            countryzips = CountryZip.search([
                    ('zip', '=', row[0]),
                    ('subdivision', '=', row[2])
                    ])
            if countryzips:
                countryzip = countryzips[0]
            else:
                countryzip = CountryZip()
                countryzip.zip = row[0]
                countryzip.subdivision = Subdivision.search([
                        ('code', '=', row[2]),
                        ], limit=1)[0]
            countryzip.city = row[1]
            countryzip.save()

        return 'end'
