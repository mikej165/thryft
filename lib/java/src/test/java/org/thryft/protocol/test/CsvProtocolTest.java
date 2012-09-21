package org.thryft.protocol.test;

import java.io.IOException;

import org.apache.thrift.TException;
import org.apache.thrift.transport.TTransportException;
import org.junit.Test;

public class CsvProtocolTest {
    @Test
    public void testRead() throws IOException, TException, TTransportException {
        throw new UnsupportedOperationException();
        // final CsvProtocol iprot = new CsvProtocol(
        // new StringReader(PRODUCTS_CSV));
        // final List<MagentoProduct> products = Lists.newArrayList();
        // final TList list = iprot.readListBegin();
        // for (int i = 0; i < list.size; i++) {
        // final MagentoProduct product = new MagentoProduct(iprot);
        // assertThat(product, is(notNullValue()));
        // products.add(product);
        // }
        // assertEquals(2, products.size());
    }

    public final static String PRODUCTS_CSV = "\"store\",\"websites\",\"attribute_set\",\"type\",\"sku\",\"category_ids\",\"has_options\",\"name\",\"image\",\"small_image\",\"thumbnail\",\"options_container\",\"url_key\",\"url_path\",\"gift_message_available\",\"meta_title\",\"meta_description\",\"custom_design\",\"price\",\"weight\",\"description\",\"short_description\",\"meta_keyword\",\"custom_layout_update\",\"status\",\"tax_class_id\",\"visibility\",\"qty\",\"min_qty\",\"use_config_min_qty\",\"is_qty_decimal\",\"backorders\",\"use_config_backorders\",\"min_sale_qty\",\"use_config_min_sale_qty\",\"max_sale_qty\",\"use_config_max_sale_qty\",\"is_in_stock\",\"low_stock_date\",\"notify_stock_qty\",\"use_config_notify_stock_qty\",\"manage_stock\",\"use_config_manage_stock\",\"stock_status_changed_automatically\",\"news_from_date\",\"news_to_date\",\"special_price\",\"special_from_date\",\"special_to_date\",\"required_options\",\"class\"\n"
            + "\"admin\",\"base\",\"Default\",\"simple\",\"Blue-Eyes.Com - 43\",\"12,36\",\"0\",\"Frank Sinatra / That's Life CD\",\"/f/i/file_6_46.jpg\",\"/f/i/file_6_46.jpg\",\"/f/i/file_6_46.jpg\",\"Block after Info Column\",\"that-s-life\",\"that-s-life.html\",\"Use config\",\"frank sinatra that's life cd\",\"10 contemporary tunes performed  with that Sinatra touch.\n"
            + "\",\"\",\"18.9500\",\"0.0000\",\"10 contemporary tunes performed  with that Sinatra touch.\n"
            + "\n"
            + "Track Listings\n"
            + "\n"
            + "1. That's Life\n"
            + "2. I Will Wait for You\n"
            + "3. Somewhere My Love (Lara's Theme) [From Doctor Zhivago]\n"
            + "4. Sand and Sea\n"
            + "5. What Now, My Love?\n"
            + "6. Winchester Cathedral\n"
            + "7. Give Her Love\n"
            + "8. Tell Her (You Love Her Each Day)\n"
            + "9. Impossible Dream\n"
            + "10. You're Gonna Hear from Me \",\"10 contemporary tunes performed  with that Sinatra touch.\n"
            + "\n"
            + "\n"
            + "1. That's Life<br>\n"
            + "\n"
            + "1. That's Life\n"
            + "2. I Will Wait for You\n"
            + "3. Somewhere My Love (Lara's Theme) [From Doctor Zhivago]\n"
            + "4. Sand and Sea\n"
            + "5. What Now, My Love?\n"
            + "6. Winchester Cathedral\n"
            + "7. Give Her Love\n"
            + "8. Tell Her (You Love Her Each Day)\n"
            + "9. Impossible Dream\n"
            + "10. You're Gonna Hear from Me \n"
            + "\",\"\",\"\",\"Enabled\",\"None\",\"Catalog, Search\",\"0.0000\",\"0.0000\",\"1\",\"0\",\"0\",\"1\",\"1.0000\",\"1\",\"0.0000\",\"1\",\"0\",\"2010-05-18 14:38:23\",\"\",\"1\",\"0\",\"1\",\"1\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"\n"
            + "\"admin\",\"base\",\"Default\",\"simple\",\"Blue-Eyes.Com - 44\",\"12\",\"0\",\"Frank Sinatra / Cycles - CD\",\"/C/y/Cycles.jpg\",\"/C/y/Cycles.jpg\",\"/C/y/Cycles.jpg\",\"Block after Info Column\",\"cycles\",\"cycles.html\",\"Use config\",\"frank sinatra cycles cd\",\"Frank's take on country music.Long out of print. Newly reissued in Europe. We have 'em !\",\"\",\"18.9500\",\"0.0000\",\"Long out of print. Newly reissued in Europe. We have 'em !\n"
            + "1. Rain in My Heart <br>\n"
            + "2. From Both Sides Now <br>\n"
            + "3. Little Green Apples <br>\n"
            + "4. Pretty Colors <br>\n"
            + "5. Cycles <br>\n"
            + "6. Wandering <br>\n"
            + "7. By the Time I Get to Phoenix <br>\n"
            + "8. Moody River <br>\n"
            + "9. My Way of Life <br>\n"
            + "10. Gentle on My Mind <br>\",\"<p>\n"
            + "1. Rain in My Heart <br>\n"
            + "2. From Both Sides Now <br>\n"
            + "3. Little Green Apples <br>\n"
            + "4. Pretty Colors <br>\n"
            + "5. Cycles <br>\n"
            + "6. Wandering <br>\n"
            + "7. By the Time I Get to Phoenix <br>\n"
            + "8. Moody River <br>\n"
            + "9. My Way of Life <br>\n"
            + "10. Gentle on My Mind <br>\",\"\",\"\",\"Enabled\",\"None\",\"Catalog, Search\",\"0.0000\",\"0.0000\",\"1\",\"0\",\"0\",\"1\",\"1.0000\",\"1\",\"0.0000\",\"1\",\"0\",\"2010-05-18 14:40:43\",\"\",\"1\",\"0\",\"1\",\"1\",\"2010-02-22 00:00:00\",\"2010-10-22 00:00:00\",\"\",\"\",\"\",\"\",\"\"\n"
            + "";
}