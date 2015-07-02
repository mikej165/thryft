package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Date;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import javax.annotation.Nullable;

public final class BuiltinsOutputProtocol extends StackedOutputProtocol<BuiltinsOutputProtocol.NestedOutputProtocol> {
    abstract class NestedOutputProtocol extends AbstractOutputProtocol {
        protected NestedOutputProtocol() {
        }

        @Override
        public final void writeBinary(final byte[] value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeBool(final boolean value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeByte(final byte value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeDateTime(final Date value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeDecimal(final BigDecimal value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeDouble(final double value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeI16(final short value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeI32(final int value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeI64(final long value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeListBegin(final Type elementType, final int size) throws OutputProtocolException {
            final List<Object> list = new ArrayList<>(size);
            _writeValue(list);
            _getOutputProtocolStack().push(new ListOutputProtocol(list));
        }

        @Override
        public final void writeListEnd() throws OutputProtocolException {
        }

        @Override
        public final void writeMapBegin(final Type keyType, final Type valueType, final int size)
                throws OutputProtocolException {
            final Map<Object, Object> map = new LinkedHashMap<>(size);
            _writeValue(map);
            _getOutputProtocolStack().push(new MapOutputProtocol(map));
        }

        @Override
        public final void writeMapEnd() throws OutputProtocolException {
        }

        @Override
        public final void writeNull() throws OutputProtocolException {
            _writeValue(null);
        }

        @Override
        public final void writeSetBegin(final Type elementType, final int size) throws OutputProtocolException {
            final Set<Object> set = new LinkedHashSet<>(size);
            _writeValue(set);
            _getOutputProtocolStack().push(new SetOutputProtocol(set));
        }

        @Override
        public final void writeString(final String value) throws OutputProtocolException {
            _writeValue(value);
        }

        @Override
        public final void writeStructBegin(final String name) throws OutputProtocolException {
            final Map<Object, Object> struct = new LinkedHashMap<>();
            _writeValue(struct);
            _getOutputProtocolStack().push(new StructOutputProtocol(struct));
        }

        @Override
        public final void writeStructEnd() throws OutputProtocolException {
        }

        @Override
        public final void writeVariant(final Object value) throws OutputProtocolException {
            _writeValue(value);
        }

        protected abstract void _writeValue(final Object value);
    }

    private final class ListOutputProtocol extends NestedOutputProtocol {
        public ListOutputProtocol(final List<Object> list) {
            this.list = list;
        }

        @Override
        protected void _writeValue(final Object value) {
            list.add(value);
        }

        private final List<Object> list;
    }

    private final class MapOutputProtocol extends NestedOutputProtocol {
        public MapOutputProtocol(final Map<Object, Object> map) {
            this.map = map;
        }

        @Override
        protected void _writeValue(final Object value) {
            if (nextKey != null) {
                map.put(nextKey, value);
                nextKey = null;
            } else {
                nextKey = value;
            }
        }

        private final Map<Object, Object> map;
        private Object nextKey = null;
    }

    private final class RootOutputProtocol extends NestedOutputProtocol {
        public @Nullable Object getValue() {
            return value;
        }

        @Override
        protected void _writeValue(final Object value) {
            this.value = value;
        }

        private Object value = null;
    }

    private final class SetOutputProtocol extends NestedOutputProtocol {
        public SetOutputProtocol(final Set<Object> set) {
            this.set = set;
        }

        @Override
        protected void _writeValue(final Object value) {
            set.add(value);
        }

        private final Set<Object> set;
    }

    private final class StructOutputProtocol extends NestedOutputProtocol {
        public StructOutputProtocol(final Map<Object, Object> struct) {
            this.struct = struct;
        }

        @Override
        public void writeFieldBegin(final String name, final Type type, final short id) throws OutputProtocolException {
            nextFieldName = name;
        }

        @Override
        public void writeFieldEnd() throws OutputProtocolException {
        }

        @Override
        public void writeFieldStop() throws OutputProtocolException {
        }

        @Override
        protected void _writeValue(final Object value) {
            checkNotNull(nextFieldName);
            struct.put(nextFieldName, value);
            nextFieldName = null;
        }

        private String nextFieldName = null;

        private final Map<Object, Object> struct;
    }

    public BuiltinsOutputProtocol() {
        _getOutputProtocolStack().push(new RootOutputProtocol());
    }

    public @Nullable Object getValue() {
        return ((RootOutputProtocol) _getOutputProtocolStack().peek()).getValue();
    }
}
