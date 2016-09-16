package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import org.thryft.CompoundType;
import org.thryft.CompoundType.FieldMetadata;

import com.google.common.base.MoreObjects;

@SuppressWarnings("serial")
public final class InvalidFieldInputProtocolException extends InputProtocolException {
    public InvalidFieldInputProtocolException(final CompoundType.FieldMetadata field, final String message) {
        super(message);
        this.field = checkNotNull(field);
    }

    public InvalidFieldInputProtocolException(final CompoundType.FieldMetadata field, final Throwable cause) {
        super(cause);
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
