#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Client web per www.udl.cat
@autor: Sergio
'''
import urllib2
from bs4 import BeautifulSoup

class Client(object):
    def get_web(self,page):
        """ Baixar-se la web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    # TODO: Buscar el text
    def search_text(self,html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all("div","featured-links-item") # Buscar un div que tingui aquesta clase
        return elements

    def main(self):
        web = self.get_web('http://www.udl.cat/')
        resultat = self.search_text(web)
        # FIXME: Imprimir resultats
        print resultat

if __name__ == "__main__":
    client = Client()
    client.main()
