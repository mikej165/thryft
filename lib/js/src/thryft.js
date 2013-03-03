if (typeof thryft === "undefined") {
	thryft = new Object();
}
if (typeof thryft.core === "undefined") {
	thryft.core = new Object();
}
if (typeof thryft.core.protocol === "undefined") {
	thryft.core.protocol = new Object();
}

thryft.core.protocol.__BuiltinsProtocolListScope = function(input) {
	if (typeof input !== "undefined") {
		this.list = input.slice(0); // Copy
		this.list.reverse(); // So pop() will be the right order
	} else {
		this.list = [];
	}
};

thryft.core.protocol.__BuiltinsProtocolListScope.prototype = {
	readValue : function() {
		return this.list.pop();
	},

	writeValue : function(value) {
		this.list.push(value);
	}
},

thryft.core.protocol.__BuiltinsProtocolMapScope = function(input) {
	if (typeof input !== "undefined") {
		this.map = jQuery.extend({}, input);
	} else {
		this.map = {};
	}
	this.nextKey = undefined;
};

thryft.core.protocol.__BuiltinsProtocolMapScope.prototype = {
	readValue : function() {
		if (typeof this.nextKey === "undefined") {
			for ( var key in this.map) {
				this.nextKey = key;
				return key;
			}
		} else {
			var value = this.map[this.nextKey];
			delete this.map[this.nextKey];
			this.nextKey = undefined;
			return value;
		}
	},

	writeValue : function(value) {
		if (typeof this.nextKey === "undefined") {
			this.nextKey = value;
		} else {
			this.map[this.nextKey] = value;
			this.nextKey = undefined;
		}
	}
};

thryft.core.protocol.__BuiltinsProtocolStructScope = function(input) {
	if (typeof input !== "undefined") {
		this.struct = jQuery.extend({}, input);
	} else {
		this.currentFieldName = undefined;
		this.struct = {};
	}
};

		thryft.core.protocol.__BuiltinsProtocolStructScope.prototype = {
			readFieldBegin : function() {
				for ( var fieldName in this.struct) {
					return {
						"fname" : fieldName
					};
				}
				return {
					"fname" : ""
				};
			},

			readFieldEnd : function() {
				for ( var fieldName in this.struct) {
					delete this.struct[fieldName];
					break;
				}
			},

			readValue : function() {
				for ( var fieldName in this.struct) {
					return this.struct[fieldName];
				}
			},

			writeFieldBegin : function(name) {
				this.currentFieldName = name;
			},

			writeFieldEnd : function() {
				this.currentFieldName = undefined;
			},

			writeValue : function(value) {
				this.struct[this.currentFieldName] = value;
			}
		},

		thryft.core.protocol.BuiltinsProtocol = function(input, inputIsMap) {
			this.scopeStack = [ new thryft.core.protocol.__BuiltinsProtocolListScope() ];
			if (typeof input !== "undefined") {
				this.scopeStack[this.scopeStack.length - 1].writeValue(input);
			}
		};

thryft.core.protocol.BuiltinsProtocol.prototype = {
	freeze : function(name) {
		if (this.scopeStack.length > 0 && this.scopeStack[0].list.length > 0) {
			return this.scopeStack[0].list[0];
		} else {
			return {};
		}
	},

	readBinary : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readBool : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readByte : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readDateTime : function() {
		return new Date(this.readI64());
	},

	readDecimal : function() {
		return this.readString();
	},

	readDouble : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readFieldBegin : function() {
		return this.scopeStack[this.scopeStack.length - 1].readFieldBegin();
	},

	readFieldEnd : function() {
		this.scopeStack[this.scopeStack.length - 1].readFieldEnd();
	},

	readI16 : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readI32 : function(f) {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readI64 : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readListBegin : function() {
		var list = this.scopeStack[this.scopeStack.length - 1].readValue();
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolListScope(list));
		return {
			size : list.length
		};
	},

	readListEnd : function() {
		this.scopeStack.pop();
	},

	readMapBegin : function() {
		var map = this.scopeStack[this.scopeStack.length - 1].readValue();
		var mapSize = 0;
		for ( var key in map) {
			mapSize++;
		}
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolMapScope(map));
		return {
			size : mapSize
		};
	},

	readMapEnd : function() {
		this.scopeStack.pop();
	},

	readSetBegin : function() {
		return this.readListBegin();
	},

	readSetEnd : function() {
		this.readListEnd();
	},

	readString : function() {
		return this.scopeStack[this.scopeStack.length - 1].readValue();
	},

	readStructBegin : function() {
		var struct = this.scopeStack[this.scopeStack.length - 1].readValue();
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolStructScope(
						struct));
		return {};
	},

	readStructEnd : function() {
		this.scopeStack.pop();
	},

	writeBinary : function(str) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(str);
	},

	writeBool : function(value) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(value);
	},

	writeByte : function(i8) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(i8);
	},
	
	writeDateTime : function(datetime) {
		this.writeI64(datetime.getTime());
	},
	
	writeDecimal : function(decimal) {
		this.writeString(decimal);
	},

	writeDouble : function(dbl) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(dbl);
	},

	writeFieldBegin : function(name, fieldType, fieldId) {
		this.scopeStack[this.scopeStack.length - 1].writeFieldBegin(name,
				fieldType, fieldId);
	},

	writeFieldEnd : function() {
		this.scopeStack[this.scopeStack.length - 1].writeFieldEnd();
	},

	writeFieldStop : function() {
	},

	writeI16 : function(i16) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(i16);
	},

	writeI32 : function(i32) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(i32);
	},

	writeI64 : function(i64) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(i64);
	},

	writeListBegin : function(elemType, size) {
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolListScope());
	},

	writeListEnd : function() {
		var listScope = this.scopeStack.pop();
		this.scopeStack[this.scopeStack.length - 1].writeValue(listScope.list);
	},

	writeMapBegin : function(keyType, valType, size) {
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolMapScope());
	},

	writeMapEnd : function() {
		var mapScope = this.scopeStack.pop();
		this.scopeStack[this.scopeStack.length - 1].writeValue(mapScope.map);
	},

	writeSetBegin : function(elemType, size) {
		this.writeListBegin(elemType, size);
	},

	writeSetEnd : function() {
		this.writeListEnd();
	},

	writeString : function(str) {
		this.scopeStack[this.scopeStack.length - 1].writeValue(str);
	},

	writeStructBegin : function(name) {
		this.scopeStack
				.push(new thryft.core.protocol.__BuiltinsProtocolStructScope());
	},

	writeStructEnd : function() {
		var structScope = this.scopeStack.pop();
		this.scopeStack[this.scopeStack.length - 1]
				.writeValue(structScope.struct);
	},
};
