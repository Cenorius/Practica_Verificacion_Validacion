# -*- coding: utf-8 -*-

from .context import Practica
import unicodedata

import unittest

class PracticaTestSuite(unittest.TestCase):

	def test_count(self):
		
		str=u"si si hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('si',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_acents(self):

		str=u'si sí hola bièn bién bien'
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('si',2),('bien',3)],"La lista devuelta tiene acentos")

	def test_count_upper(self):

		str=u'Si si Hola Bien biEn bieN BIEN'

		result=Practica.count(str)
		print(result)
		self.assertEqual(result,[('hola',1),('si',2),('bien',4)],"La lista devuelta tiene mayusculas")
