import os
import indice_sefip
import unittest
import tempfile

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = indice_sefip.app.test_client()

    def test_main(self):
        rv = self.app.get('/')
        print(rv.data)
        self.assertEqual(rv.data, b'Home')

    def test_api(self):
        route = "/mes_ini_compt/%s/mes_fim_compt/%s/ano_ini_compt/%s/ano_fim_compt/%s/dia_ini_pgto/%s/mes_ini_pgto/%s/ano_ini_pgto/%s/dia_fim_pgto/%s/mes_fim_pgto/%s/ano_fim_pgto/%s/tipo_iden_empresa/%s/cod_fpas/%s/cod_simples/%s/opcao/%s/cod_categoria/%s/index_categoria/%s/index_opcao/%s/index_tipo_iden_empresa/%s/index_cod_fpas/%s/index_cod_simples/%s" % (
            '04',
            '06',
            '2007',
            '2007',
            '30',
            '05',
            '2017',
            '30',
            '05',
            '2017',
            '1',
            '000',
            '1',
            '1967',
            '1',
            '1',
            '1',
            '1',
            '3',
            '1')
        
        print(route)
        # rv = self.app.get(route)
        # print(rv.data)


if __name__ == 'bn':
    unittest.main()