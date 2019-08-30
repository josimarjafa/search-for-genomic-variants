from unittest import TestCase

import app
import json


class TestDataset(TestCase):
    def setUp(self):
        self.dataset = app.Dataset()

    def test_getGene(self):
        assert len(self.dataset.getGene('BRAF')) == 68

    def test_getGeneAuto(self):
        assert self.dataset.getGeneAuto('BRA') == ['ABRAXAS1', 'BRAF', 'BRAT1', 'GABRA1', 'GABRA2', 'GABRA5']
        assert len(self.dataset.getGeneAuto('BRA')) == 6

    def test_getData(self):
        assert len(self.dataset.getData().index) == 48515



class TestRoute(TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()


    def test_Home(self):
        resp = self.app.get('/')
        assert "200 OK" == resp.status
        assert b'Variant Search Coding Assignment (VSCA) by Josimar Andrade\n\n ' \
               b'Please search a gene variation with /gene/<gene_name> or /gene/autocomplete/<gene_name> ' \
               b'for autocomplete' in resp.data


    def test_gene(self):
        resp = self.app.get('/gene/BRAF')
        assert "200 OK" == resp.status
        assert len(json.loads(resp.data)) == 68


    def test_geneAuto(self):
        resp = self.app.get('/gene/autocomplete/BRA')
        assert "200 OK" == resp.status
        assert len(json.loads(resp.data)) == 6
