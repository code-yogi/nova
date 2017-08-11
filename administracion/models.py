# -*- coding: utf-8 -*-

# Librerias Django
from __future__ import unicode_literals
from django.db import models

# Otros Modelos:
from seguridad.models import Profile


class Zona(models.Model):

    descripcion = models.CharField(max_length=144)

    created_by = models.ForeignKey(Profile, related_name='zon_created_by', null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(Profile, related_name='zon_updated_by', null=True)
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class Empresa(models.Model):

    clave = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=144)
    descripcion_jde = models.CharField(max_length=144)
    descripcion_ebs = models.CharField(max_length=144)
    alias = models.CharField(max_length=40, blank=True, null=True)
    created_by = models.ForeignKey(Profile, related_name='emp_created_by', null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(Profile, related_name='emp_updated_by', null=True)
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return self.descripcion


class Cliente(models.Model):

    clave = models.CharField(max_length=144)
    nombre = models.CharField(max_length=144)
    created_by = models.ForeignKey(Profile, related_name='cli_created_by', null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(Profile, related_name='cli_updated_by', null=True)
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.clave

    def __unicode__(self):
        return self.clave


class Contrato(models.Model):

    con_clave = models.CharField(max_length=4)
    con_numero = models.CharField(max_length=14, null=True)
    con_nombre = models.CharField(max_length=100)
    con_descripcion = models.CharField(max_length=300, null=True)
    con_cliente = models.ForeignKey(Cliente, related_name='con_cliente')
    con_inicio = models.DateField(null=True)
    con_termino = models.DateField(null=True)
    con_ampliacion = models.DateField(null=True)
    con_comentarios = models.CharField(max_length=120, null=True)
    con_zona = models.ForeignKey(Zona)
    con_coordinador = models.ForeignKey(Profile, related_name='con_coordinador')
    con_supervisor = models.ForeignKey(Profile, related_name='con_supervisor')
    con_estado = models.CharField(max_length=3)
    created_by = models.ForeignKey(Profile, related_name='con_created_by', null=True)
    created_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(Profile, related_name='con_updated_by', null=True)
    updated_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
        blank=True
    )

    def __str__(self):
        value = "%s - %s" % (self.con_clave, self.con_nombre)
        return value

    def __unicode__(self):
        value = "%s - %s" % (self.con_clave, self.con_nombre)
        return value
