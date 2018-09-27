#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-05 15:23:35
# @Author  : hbh (${email})
# @Link    : ${link}
# @Version : $Id$

import unittest

class TestStringMethod(unittest.TestCase):
	
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')

	def test_equal(self):
		self.assertEqual(2,2)

	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())

	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(),['hello','world'])
		# check that s.split fails when the separator is not a string
		# 如果split的参数不是string（比如2）的时候，抛出TypeError
		with self.assertRaises(TypeError):
			s.split(2)

if __name__ == '__main__':
	unittest.main()