# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Ordenador(models.Model):
     _name = 'ordenador'

     marca = fields.Char(string="Marca")
     version = fields.Char(string="Version")