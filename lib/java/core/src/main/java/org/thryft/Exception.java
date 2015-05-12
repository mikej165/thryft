package org.thryft;

@SuppressWarnings("serial")
public abstract class Exception extends java.lang.Exception implements
CompoundType {
    public abstract String getThriftQualifiedClassName();
}
