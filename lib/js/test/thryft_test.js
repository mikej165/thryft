BuiltinsProtocolTest = TestCase("BuiltinsProtocolTest");

BuiltinsProtocolTest.prototype.test = function(fieldName, fieldValue) {
	if (!fieldName || !fieldValue) {
		return;
	}
	var expectedObject = {};
	expectedObject[fieldName] = fieldValue;
	var expectedStruct = new thryft_test.core.protocol.test.ProtocolTestStruct(expectedObject);
	
	var oprot = new thryft.core.protocol.BuiltinsProtocol();
	expectedStruct.write(oprot);
	var writtenObject = oprot.freeze();
	assertEquals(fieldValue, writtenObject[fieldName]);

	var iprot = new thryft.core.protocol.BuiltinsProtocol(writtenObject);
	var readStruct = thryft_test.core.protocol.test.ProtocolTestStruct.read(iprot);
	assertEquals(expectedStruct.get(fieldName), readStruct.get(fieldName));
};

BuiltinsProtocolTest.prototype.testMap = function() {
	this.test("map_string_string_field", {"key": "value"});
};

BuiltinsProtocolTest.prototype.testList = function() {
	this.test("list_string_field", ['test', 'test2']);
};

BuiltinsProtocolTest.prototype.testString = function() {
	this.test("string_field", "test");
};
