from hamcrest.core import assert_that
from hamcrest.core.core.isequal import equal_to
from hamcrest.library.object.haslength import has_length
from thryft.protocol.json_protocol import JsonProtocol
import unittest


class JsonProtocolTest(unittest.TestCase):
    PRODUCTS_JSON = '''[{"@class":"yogento.api.models.magento.catalog.product.MagentoProduct","backorders":0,"description":"This mint condition lavender pocket silk was given\nto a female fan by Frank Sinatra in 1979 after she handed him a rose while he was onstage at Caesars Palace, Las Vegas. Only one to sell.\n\nShe also received a red pocket silk from FS two nights later.","image":"/s/c/scarf.JPG","is_in_stock":false,"is_qty_decimal":false,"low_stock_date":1323291108000,"manage_stock":false,"max_sale_qty":0.0000,"meta_description":"","meta_keyword":"","meta_title":"","min_qty":0.0000,"min_sale_qty":1.0000,"name":"Frank Sinatra Lavender Pocket Silk","news_from_date":1260853200000,"news_to_date":1268625600000,"price":499.9500,"qty":0.0000,"short_description":"This mint condition lavender pocket silk was given\nto a female fan by Frank Sinatra in 1979 after she handed him a rose while he was onstage at Caesars Palace, Las Vegas. Only one to sell.","sku":"1","small_image":"/s/c/scarf.JPG","special_from_date":1260939600000,"special_price":399.9500,"special_to_date":1295154000000,"status":"DISABLED","stock_status_changed_automatically":true,"thumbnail":"/s/c/scarf.JPG","type":"SIMPLE","url_key":"tyu","url_path":"tyu.html","visibility":["CATALOG","SEARCH"],"weight":0.0000}]'''

    def test_read(self):
        iprot = JsonProtocol(self.PRODUCTS_JSON)
        products = []
        for _ in xrange(iprot.readListBegin()[1]):
            product = MagentoProduct.read(iprot)
            assert product is not None
            products.append(product)
        iprot.readListEnd()
        assert_that(products, has_length(1))

    def test_write(self):
        iprot = JsonProtocol(self.PRODUCTS_JSON)
        products = \
            [MagentoProduct.read(iprot)
             for _ in xrange(iprot.readListBegin()[1])]
        iprot.readListEnd()

        oprot = JsonProtocol()
        oprot.writeListBegin()
        for product in products:
            product.write(oprot)
        oprot.writeListEnd()
        ojson = str(oprot)

        iprot = JsonProtocol(ojson)
        products2 = \
            [MagentoProduct.read(iprot)
             for _ in xrange(iprot.readListBegin()[1])]
        iprot.readListEnd()
        assert_that(products2, equal_to(products))
