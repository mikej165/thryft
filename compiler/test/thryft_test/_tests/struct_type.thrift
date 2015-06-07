// struct comment
struct TestStruct {
    // field comment
    1:double dfield;

    // @validation {"minLength": 2}
    // @js_view_metadata {"displayFormat": "some format", "editControl": "some control"}
    2: string stringfield;

    3: optional string emailfield;

    4: optional string firstnamefield;
}
