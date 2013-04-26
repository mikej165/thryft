// exception comment
exception TestException {
}

// service comment
service TestService {
    // function1 comment
    void TestFunction1();
    // function2 comment
    oneway void TestFunction2();
    /**
     * Long function comment
     * @param iparam input parameter
     * Some other text
    */
    void TestFunction3(1:i32 iparam);
    // @return some boolean
    bool TestFunction4();
    // @throws TestException if it's a test
    bool TestFunction5() throws (1:TestException e);
    bool TestFunction6(1:i32 iparam) throws (1:TestException e);
}