# -*- coding: utf-8 -*-
from .context import Practica
import unicodedata


import unittest

class PracticaTestSuite(unittest.TestCase):

	def test_count(self):
		
		str=u"bicicleta bicicleta hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_acents(self):

		str=u'bicicleta bicicletá hola bièn bién bien'
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta tiene acentos")

	def test_count_upper(self):

		str=u'Bicicleta bicicleta Hola Bien biEn bieN BIEN'

		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',4)],"La lista devuelta tiene mayusculas")

	def test_removeStopwords(self):

		lstr=['yo','el','ella','tuyos','como','coche']

		result=Practica.removeStopwords(lstr)

		self.assertEqual(result,['coche'],"La lista devuelta tiene stopwords")

	def test_removeSymbols(self):
		lstr=["que" ,"pasa" ,"tio","#","@","()","(colega"]

		result=Practica.removeSymbols(lstr)
		print(result)
		self.assertEqual(result,["que" ,"pasa" ,"tio","colega"],"La lista devuelta tiene simbolos")

