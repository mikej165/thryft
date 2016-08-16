package org.thryft;

public interface StructBean {
    public Object get(final CompoundType.FieldMetadata fieldMetadata);

    public Object get(final String fieldThriftName);
}
