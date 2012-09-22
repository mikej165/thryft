// C++-style comment
/* C-style comment */
/**
  * Multi-line C-style comment
  * Another line.
*/
# Python-style comment

namespace * thryft 

// Constant comment
const i32 x = 1; 

// Struct comment
struct TestStruct {
    // Field comment    
    required string field;
}

// Service comment
service TestService {
    // Function comment
    void ping();
}

// Enum comment
enum TestEnum {
    // Enumerator comment
    ENUMERATOR = 1,
}

// Exception comment
exception TestException {
    // Exception field comment
    required string message;
}
