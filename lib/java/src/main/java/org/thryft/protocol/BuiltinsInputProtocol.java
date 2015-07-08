package org.thryft.protocol;

import static com.google.common.base.Preconditions.checkNotNull;

import java.math.BigDecimal;
import java.util.Date;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;

public final class BuiltinsInputProtocol extends StackedInputProtocol<BuiltinsInputProtocol.NestedInputProtocol> {
    abstract class NestedInputProtocol extends AbstractInputProtocol {
        protected NestedInputProtocol() {
        }

        @Override
        public byte[] readBinary() throws InputProtocolException {
            return (byte[]) _readValue();
        }

        @Override
        public boolean readBool() throws InputProtocolException {
            return (Boolean) _readValue();
        }

        @Override
        public byte readByte() throws InputProtocolException {
            return ((Number) _readValue()).byteValue();
        }

        @Override
        public Date readDateTime() throws InputProtocolException {
            return (Date) _readValue();
        }

        @Override
        public BigDecimal readDecimal() throws InputProtocolException {
            return (BigDecimal) _readValue();
        }

        @Override
        public double readDouble() throws InputProtocolException {
            return ((Number) _readValue()).doubleValue();
        }

        @Override
        public short readI16() throws InputProtocolException {
            return ((Number) _readValue()).shortValue();
        }

        @Override
        public int readI32() throws InputProtocolException {
            return ((Number) _readValue()).intValue();
        }

        @Override
        public long readI64() throws InputProtocolException {
            return ((Number) _readValue()).longValue();
        }

        @Override
        public ListBegin readListBegin() throws InputProtocolException {
            @SuppressWarnings("unchecked")
            final List<Object> list = (List<Object>) _readValue();
            _getInputProtocolStack().push(new ListInputProtocol(list));
            return new ListBegin(Type.VOID_, list.size());
        }

        @Override
        public MapBegin readMapBegin() throws InputProtocolException {
            @SuppressWarnings("unchecked")
            final Map<Object, Object> map = (Map<Object, Object>) _readValue();
            _getInputProtocolStack().push(new MapInputProtocol(map));
            return new MapBegin(Type.VOID_, Type.VOID_, map.size());
        }

        @Override
        public SetBegin readSetBegin() throws InputProtocolException {
            @SuppressWarnings("unchecked")
            final Set<Object> set = (Set<Object>) _readValue();
            _getInputProtocolStack().push(new SetInputProtocol(set));
            return new SetBegin(Type.VOID_, set.size());
        }

        @Override
        public String readString() throws InputProtocolException {
            return (String) _readValue();
        }

        @Override
        public String readStructBegin() throws InputProtocolException {
            @SuppressWarnings("unchecked")
            final Map<Object, Object> struct = (Map<Object, Object>) _readValue();
            _getInputProtocolStack().push(new StructInputProtocol(struct));
            return "";
        }

        @Override
        public Object readVariant() throws InputProtocolException {
            return _readValue();
        }

        protected abstract Object _readValue();
    }

    private final class ListInputProtocol extends NestedInputProtocol {
        public ListInputProtocol(final List<Object> list) {
            this.iterator = list.iterator();
        }

        @Override
        protected Object _readValue() {
            return iterator.next();
        }

        private final Iterator<Object> iterator;
    }

    private final class MapInputProtocol extends NestedInputProtocol {
        public MapInputProtocol(final Map<Object, Object> map) {
            this.iterator = map.entrySet().iterator();
        }

        @Override
        protected Object _readValue() {
            if (currentEntry == null) {
                currentEntry = iterator.next();
                return checkNotNull(currentEntry.getKey());
            } else {
                final Object value = currentEntry.getValue();
                currentEntry = null;
                return value;
            }
        }

        private Map.Entry<Object, Object> currentEntry = null;
        private final Iterator<Map.Entry<Object, Object>> iterator;
    }

    private final class RootInputProtocol extends NestedInputProtocol {
        public RootInputProtocol(final Object value) {
            this.value = value;
        }

        @Override
        protected Object _readValue() {
            return value;
        }

        private final Object value;
    }

    private final class SetInputProtocol extends NestedInputProtocol {
        public SetInputProtocol(final Set<Object> set) {
            this.iterator = set.iterator();
        }

        @Override
        protected Object _readValue() {
            return checkNotNull(iterator.next());
        }

        private final Iterator<Object> iterator;
    }

    private final class StructInputProtocol extends NestedInputProtocol {
        public StructInputProtocol(final Map<Object, Object> struct) {
            this.iterator = struct.entrySet().iterator();
        }

        @Override
        public FieldBegin readFieldBegin() throws InputProtocolException {
            if (iterator.hasNext()) {
                currentEntry = iterator.next();
                return new FieldBegin(currentEntry.getKey().toString());
            } else {
                return FieldBegin.STOP;
            }
        }

        @Override
        public void readFieldEnd() throws InputProtocolException {
            currentEntry = null;
        }

        @Override
        protected Object _readValue() {
            return currentEntry.getValue();
        }

        private Map.Entry<Object, Object> currentEntry = null;
        private final Iterator<Map.Entry<Object, Object>> iterator;
    }

    public BuiltinsInputProtocol(final Object root) {
        _getInputProtocolStack().push(new RootInputProtocol(root));
    }
}
