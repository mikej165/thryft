package org.thryft.protocol.test;


public class JsonProtocolTest {
    public JsonProtocolTest() {
        throw new UnsupportedOperationException();
        // final Set<MagentoProduct> products = Sets.newLinkedHashSet();
        // for (int productI = 0; productI < 2; productI++) {
        // final MagentoProduct product = new MagentoProduct.Builder()
        // .setDescription(
        // "Test product " + Integer.toString(productI))
        // .setName("Test product " + Integer.toString(productI))
        // .setPrice(new BigDecimal(0))
        // .setShortDescription(
        // "Test product " + Integer.toString(productI))
        // .setSku("testproduct" + Integer.toString(productI))
        // .setStatus(MagentoProductStatus.ENABLED)
        // .setType(MagentoProductType.SIMPLE)
        // .setVisibility(ImmutableSet.of("CATALOG"))
        // .setUrlKey("testproduct" + Integer.toString(productI))
        // .setUrlPath("/testproduct" + Integer.toString(productI))
        // .build();
        // products.add(product);
        // }
        // this.products = ImmutableSet.copyOf(products);
    }

    // @Test
    // public void testReadList() throws Exception {
    // final JsonProtocol iprot = new JsonProtocol(new StringReader(
    // __writeProductsAsString()));
    // final TList list = iprot.readListBegin();
    // final List<MagentoProduct> products = Lists.newArrayList();
    // for (int i = 0; i < list.size; i++) {
    // final MagentoProduct product = new MagentoProduct(iprot);
    // assertThat(product, is(notNullValue()));
    // products.add(product);
    // }
    // assertEquals(2, products.size());
    // }
    //
    // @Test
    // public void testReadStruct() throws Exception {
    // final MagentoProduct product = products.asList().get(0);
    // final JsonProtocol iprot = new JsonProtocol(new StringReader(
    // __writeProductAsString(product)));
    // final MagentoProduct product2 = new MagentoProduct(iprot);
    // assertEquals(product, product2);
    // }
    //
    // private String __writeProductAsString(final MagentoProduct product)
    // throws Exception {
    // final StringWriter stringWriter = new StringWriter();
    // final JsonProtocol oprot = new JsonProtocol(stringWriter);
    // product.write(oprot);
    // oprot.flush();
    // return stringWriter.toString();
    // }
    //
    // private void __writeProducts(final TProtocol oprot) throws Exception {
    // oprot.writeSetBegin(new TSet(TType.STRUCT, products.size()));
    // for (final MagentoProduct product : products) {
    // product.write(oprot);
    // }
    // oprot.writeSetEnd();
    // }
    //
    // private String __writeProductsAsString() throws Exception {
    // final StringWriter stringWriter = new StringWriter();
    // final JsonProtocol oprot = new JsonProtocol(stringWriter);
    // __writeProducts(oprot);
    // oprot.flush();
    // return stringWriter.toString();
    // }
    //
    // private final ImmutableSet<MagentoProduct> products;
}