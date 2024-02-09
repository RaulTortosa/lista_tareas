# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_tareas(models.Model):
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'
    _rec_name="tarea"

    tarea = fields.Char("Nombre")
    prioridad = fields.Integer("Nivel de prioridad")
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()
    
    fechaInicio = fields.Datetime(string="Fecha y Hora de inicio")
    fechaFin = fields.Datetime(string="Fecha y Hora de finalizacion")
    duracion = fields.Float("Duración (en horas)")
    imagen = fields.Binary('Imagen de la tarea')

    prioridad_con_texto = fields.Char(compute='_compute_prioridad_con_texto', store=True)

    @api.depends('prioridad')
    def _compute_prioridad_con_texto(self):
        for record in self:
            record.prioridad_con_texto = "Prioridad: %s" % record.prioridad

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False               