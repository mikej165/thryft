include "exception_type.thrift"

// service comment
service TestService1a {
    // function comment
    // @requires_roles ADMIN
    /** Multi-line
    function comment */
    void test_function(
    	// Parameter comment
    	i32 input,
    	// Parameter2 comment
    	i32 input2
   	) throws (
   		// Throws comment
   		exception_type.TestException e
   	);

   	void test_function2(i32 input, i32 input2);
}
