package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import org.thryft.CompoundType;
import org.thryft.CompoundType.FieldMetadata;

import com.google.common.base.MoreObjects;

@SuppressWarnings("serial")
public final class MissingFieldInputProtocolException extends InputProtocolException {
    public MissingFieldInputProtocolException(final CompoundType.FieldMetadata field) {
        super("missing " + field.getJavaName());
        this.field = checkNotNull(field);
    }

    public final FieldMetadata getField() {
        return field;
    }

    @Override
    public String toString() {
        return MoreObjects.toStringHelper(this).add("field", field).toString();
    }

    private final FieldMetadata field;
}
