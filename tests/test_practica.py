# -*- coding: utf-8 -*-
from .context import Practica
import unicodedata


import unittest

class PracticaTestSuite(unittest.TestCase):

	def test_count_u(self):
		
		str=u"bicicleta bicicleta hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_str(self):
		
		str="bicicleta bicicleta hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('hola',1),('bicicleta',2),('bien',3)],"La lista devuelta no es correcta")

	def test_count_int(self):
		with self.assertRaises(TypeError):
			Practica.count(1)
	
	def test_count_float(self):
		with self.assertRaises(TypeError):
			Practica.count(1.0)

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

	def test_removeSymbolsAndWhiteSpaces(self):
		lstr="que pasa ,tio, #, @ , (), (colega, bien,bien ©"

		result=Practica.removeSymbolsAndWhiteSpaces(lstr)
		
		self.assertEqual(result,["que" ,"pasa" ,"tio","colega","bien","bien"],"La lista devuelta tiene simbolos")

	def test_getWordsFrecuency(self):
		lstr=['hola','bicicleta','bicicleta','bien','bien','bien','bien']

		result=Practica.getWordsFrecuencies(lstr)
		print(result)
		self.assertEqual(result,[('hola',1),('bien',4),('bicicleta',2)],"La lista devuelta no es correcta")

	def test_getWordsFrecuency_None(self):
		lstr=None

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_Integers(self):
		lstr=[1,2,3]

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_String_Integers(self):
		lstr=["test",1,2,3]

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_Strings_Integer(self):
		lstr=["test","test2",3]

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_Unicodes_Integer(self):
		lstr=[u"test",u"test2",3]

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_Unicode_Integers(self):
		lstr=[u"test",1,2,3]

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)
	
	def test_getWordsFrecuency_Empty(self):
		lstr=[]

		result=Practica.getWordsFrecuencies(lstr)

		self.assertEqual(result,[],"La lista devuelta no esta vacia")

	def test_getWordsFrecuency_Unicode_Integer(self):
		lstr=1

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)

	def test_getWordsFrecuency_SpecialCharacter(self):
		lstr="©"

		with self.assertRaises(TypeError):
			Practica.getWordsFrecuencies(lstr)
