#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 FILE 	hd.py
 DATE 	Created 2012-05-01

"""
import os,sys,glob
import scribus 
import random, re

document_width =  209.55
document_height = 273.1
document_margin = 12.7


def setbleeds():
	scribus.setHGuides([document_margin,document_height-document_margin])
	scribus.setVGuides([document_margin,document_width-document_margin])


def textframes(text_id, x, y, width, height, bg_colour, text_colour, fontsize, font, spacing, parsedtext, layer, linespacing=0, resize=0):
	scribus.createText(x, y, width, height, text_id)
#scribus.text_id = scribus.createText(120, 10, 200, 20)
	scribus.setText(parsedtext, text_id)
	scribus.setFont(font, text_id)
	scribus.setTextColor(text_colour, text_id)
	scribus.setTextDistances(3*spacing, spacing, 0, spacing, text_id)
	scribus.sentToLayer(layer, text_id)
	scribus.setFontSize(fontsize, text_id)

def loadimages(img_id, img_x, img_y, img_width, img_height, img_path, layer, scaletoframe):
	scribus.createImage(img_x, img_y, img_width, img_height, img_id)
	scribus.loadImage(img_path, img_id)
	scribus.sentToLayer(layer, img_id)

# create new document (smallsquare) 
if scribus.newDocument((document_width,document_height), (0,6.35,3.175,3.175), scribus.PORTRAIT, 1, scribus.UNIT_MILLIMETERS, scribus.PAGE_2, 1, 0):

	i = 0
	scribus.createLayer("images")
	scribus.createLayer("text")

	textframes("titel", 42.5, 50, 129.7, 17.99, "White","Black", 39, "FreeSans Bold", 0, "DIE SCHWÄRZUNG","text", 0, 0)
	scribus.createLine(20.2,67.5,190.2,67.5)
	scribus.createImage(55, 72.7, 99.5, 20.2, "logo")
	scribus.loadImage("handydandy_logo.eps", "logo")
	scribus.sentToLayer("images", "logo")
	scribus.setScaleImageToFrame(1,1,"logo")
	textframes("jahr", 81.7, 216.7, 46.1, 18.5, "White","Black", 22, "FreeSans Medium", 0, "2006 - 2012","text", 0, 0)
	
	scribus.newPage(-1)

	slike = glob.glob("pics/*.jpg")
	slike.sort()

	for slika in slike:
		img_id = "img_id" + str(i)
		loadimages(img_id,0,0,209.55,273.1,slika,"images",0)		
		i += 1
		if (i > 796): break
		scribus.newPage(-1)

	scribus.newPage(-1)
	credits = """Credits:

the handydandy
Bernhard Bauch
Luc Gross
Nicolaj Kirisits
Gordan Savicic
Julia Staudacher
Florian Waldner

Nickelsdorf, 2012
http://thehandydandy.yugo.at

Danksagung: Gunther Grasser, etxt..."""
	textframes("credits", 26, 140, 160, 110, "White","Black", 10, "FreeSerif Medium", 0, credits,"text", 0, 0)


# final // save doc && export PDF
scribus.saveDocAs("schwarzung.sla")


pdf = scribus.PDFfile()
#pdf.file = 'hd.pdf' 
#pdf.save()
#scribus.closeDoc()
