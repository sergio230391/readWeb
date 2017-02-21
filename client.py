#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Client web per www.udl.cat
@autor: Sergio
'''
import urllib2

class Client(object):
    def get_web(self,page):
        """ Baixar-se la web """
        f = urllib2.urlopen(page)
        html = f.read()
        f.close()
        return html

    def main(self):
        web = self.get_web('http://www.udl.cat/')
        # Buscar el text
        # Imprimir resultats
        print web

if __name__ == "__main__":
    client = Client()
    client.main()
