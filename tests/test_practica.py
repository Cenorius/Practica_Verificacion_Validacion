# -*- coding: utf-8 -*-

from .context import Practica

import unittest

class PracticaTestSuite(unittest.TestCase):

	def test_count(self):
		
		str="si si Hola bien bien bien"
		
		result=Practica.count(str)
		
		self.assertEqual(result,[('Hola',1),('si',2),('bien',3)],"La lista devuelta no es correcta")
