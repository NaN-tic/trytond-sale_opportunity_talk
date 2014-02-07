# This file is part of the sale_opportunity_talk module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .opportunity import *


def register():
    Pool.register(
        SaleOpportunityTalk,
        SaleOpportunity,
        module='sale_opportunity_talk', type_='model')
