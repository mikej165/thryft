service TestService {
    void TestFunction1();
    oneway void TestFunction2();
    void TestFunction3(1:i32 iparam);
    bool TestFunction4();
    bool TestFunction5() throws (1:MyException e);
}