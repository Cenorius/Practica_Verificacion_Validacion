# -*- coding: utf-8 -*-

from .context import Practica
import unicodedata

import unittest

class PracticaTestSuite(unittest.TestCase):

	def test_count(self):
		
		str=u"si si Hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('Hola',1),('si',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_acents(self):

		str=u'si sí Hola bièn bién bien'
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('Hola',1),('si',2),('bien',3)],"La lista devuelta tiene acentos")