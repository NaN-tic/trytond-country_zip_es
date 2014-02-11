# -*- encoding: utf-8 -*-
#This file is part country_zip_es module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.

from trytond.pool import Pool
from .country_zip import *


def register():
    Pool.register(
        LoadCountryZipsStart,
        module='country_zip_es', type_='model')
    Pool.register(
        LoadCountryZips,
        module='country_zip_es', type_='wizard')
