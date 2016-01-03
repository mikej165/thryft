package org.thryft;

public interface StructBean {
    public Object get(final CompoundType.FieldMetadata fieldMetadata);

    public Object get(final String fieldThriftName);

    /**
     * Check if the compound type is empty. False if any fields are set.
     *
     * @return false if any fields are set
     */
    public boolean isEmpty();
}
