# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Alumno(models.Model):
    _name = 'escolares.alumno'
    matricula = fields.Char("Matricula",size=8,required=True)
    apellidoPaterno = fields.Char(string="Apellido Paterno")
    apellidoMaterno = fields.Char(string="Apellido Materno")
    name = fields.Char(string="Nombres")
    edad = fields.Integer(string="Edad")
    carrera_id = fields.Many2one("escolares.carrera","Carrera")
 

class Materia(models.Model):
    _name = 'escolares.materia'
    clave = fields.Char(string="Clave")
    name = fields.Char(string="Nombre")
    creditos = fields.Integer(string="Creditos")

class Carrera(models.Model):
    _name = 'escolares.carrera'
    clave = fields.Char(string="Clave")
    name = fields.Char(string="Nombre")


