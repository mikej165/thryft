namespace * thryft

// struct comment
struct TestStruct {
    // field comment
    1:double dfield;

    // @validation {"minLength": 2}
    // @js_view_metadata {"displayFormat": "some format", "editControl": "some control"}
    2: string stringfield;

    6: string requiredstringwithdefault = "test";

    7: list<string> requiredlistwithdefault = ["test", "test2"];

	9: list<string> requiredlistwithdefault2 = ["test"];

	10: map<string, string> requiredmapwithdefault = {"test": "value"};

    3: optional string emailfield;

    4: optional string firstnamefield;

	5: optional string optionalstringwithdefault = "test";

	8: optional list<string> optionallistwithdefault = ["test", "test2"];
}
