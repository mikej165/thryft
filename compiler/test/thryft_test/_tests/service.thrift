include "exception_type.thrift"

// service comment
service TestService1a {
    // function comment
    // @requires_roles ADMIN
    /** Multi-line
    function comment */
    void test_function(
    	// Parameter comment
    	i32 input
   	) throws (
   		// Throws comment
   		exception_type.ExceptionType e
   	);
}
