from thryft.generators.java.java_generator import JavaGenerator
from yutil import indent, decamelize


class PropertiesJavaGenerator(JavaGenerator):
    def __init__(self, project_name):
        JavaGenerator.__init__(self)
        self._project_name = project_name

    class Field(JavaGenerator.Field):
        def java_property_initializer(self):
            java_name = self.java_name()
            thrift_name = self.name
            from_string = self.type.java_from_string("%(java_name)sString" % locals())
            type_qname = self.type.java_qname(boxed=True)
            if self.required:
                if self.value is not None:
                    java_value = self.java_value()
                    empty_initializer = null_initializer = "%(java_name)s = %(java_value)s;" % locals()
                else:
                    null_initializer = """throw new RuntimeException("no such property %(thrift_name)s");""" % locals()
                    empty_initializer = """throw new RuntimeException("property %(thrift_name)s is empty");""" % locals()
                return """\
final %(type_qname)s %(java_name)s;
{
    Object %(java_name)sObject = __properties.remove("%(thrift_name)s");
    if (!(%(java_name)sObject instanceof String)) {
        %(null_initializer)s
    } else {
        final String %(java_name)sString = ((String)%(java_name)sObject).trim();
        if (%(java_name)sString.isEmpty()) {
            %(empty_initializer)s
        } else {
            %(java_name)s = %(from_string)s;
        }
    }
}""" % locals()
            else:
                if self.value is not None:
                    java_value = self.java_value()
                    null_or_empty_initializer = """%(java_name)s = com.google.common.base.Optional.<%(type_qname)s>of(%(java_value)s)""" % locals()
                else:
                    null_or_empty_initializer = """%(java_name)s = com.google.common.base.Optional.<%(type_qname)s>absent()""" % locals()
                return """\
final com.google.common.base.Optional<%(type_qname)s> %(java_name)s;
{
    Object %(java_name)sObject = __properties.remove("%(thrift_name)s");
    if (!(%(java_name)sObject instanceof String)) {
        %(null_or_empty_initializer)s;
    } else {
        final String %(java_name)sString = ((String)%(java_name)sObject).trim();
        if (%(java_name)sString.isEmpty()) {
            %(null_or_empty_initializer)s;
        } else {
            %(java_name)s = com.google.common.base.Optional.of(%(from_string)s);
        }
    }
}""" % locals()

        def java_to_map_put(self, map_variable):
            getter_name = self.java_getter_name()
            name = self.name
            if self.required:
                return "%(map_variable)s.put(\"%(name)s\", %(getter_name)s());" % locals();
            else:
                return """\
if (%(getter_name)s().isPresent()) {
    %(map_variable)s.put(\"%(name)s\", %(getter_name)s().get());
}""" % locals()

    class StructType(JavaGenerator.StructType):
        def _java_member_declarations(self):
            name = self.java_name()
            ret = JavaGenerator.StructType._java_member_declarations(self)
            ret.append("private final static org.slf4j.Logger logger = org.slf4j.LoggerFactory.getLogger(%(name)s.class);" % locals())
            return ret

        def _java_method_load(self):
            name = self.java_name()
            field_initializers = indent(' ' * 4, "\n\n".join(field.java_property_initializer() for field in self.fields))
            field_thrift_names = ', '.join('"%s"' % field.name for field in self.fields)
            field_values = ', '.join(field.java_name() for field in self.fields)
            project_name = self._parent_generator()._project_name
            project_name_upper = self._parent_generator()._project_name.upper()
            properties_file_name = decamelize(self.name)
            if properties_file_name.endswith('_properties'):
                properties_file_name = properties_file_name[:-len('_properties')]
            properties_file_name = properties_file_name + '.properties'
            return {'load': """
public static %(name)s load() {
    return load(com.google.common.base.Optional.<java.io.File> absent());
}

public static %(name)s load(final com.google.common.base.Optional<java.io.File> commandLinePropertiesFilePath) {
    java.util.Properties __properties = new java.util.Properties();

    String[] __propertyNames = {%(field_thrift_names)s};
    for (final String propertyName : __propertyNames) {
        final String propertyValue = System.getenv("%(project_name_upper)s_" + propertyName.toUpperCase());
        if (propertyValue != null) {
            __properties.put(propertyName, propertyValue);
        }
    }

    __properties = __mergeProperties(__properties, __readProperties("%(properties_file_name)s"));
    __properties = __mergeProperties(__properties, __readProperties(new java.io.File(
            new java.io.File(new java.io.File(System.getProperty("user.home")),
                    ".%(project_name)s"), "%(properties_file_name)s")));
    __properties = __mergeProperties(__properties, __readProperties(new java.io.File(
            "/etc/%(project_name)s/%(properties_file_name)s")));
    if (commandLinePropertiesFilePath.isPresent()) {
        __properties = __mergeProperties(__properties,
                __readProperties(commandLinePropertiesFilePath.get()));
    }

%(field_initializers)s

    for (final java.util.Map.Entry<Object, Object> entry : __properties.entrySet()) {
        throw new RuntimeException("properties file(s) have unknown property " + entry.getKey().toString());
    }

    return new %(name)s(%(field_values)s);
}""" % locals()}

        def _java_method__merge_properties(self):
            return {'__mergeProperties': '''\
private static java.util.Properties __mergeProperties(
        final java.util.Properties leftProperties, final java.util.Properties rightProperties) {
    final java.util.Properties mergedProperties = new java.util.Properties();
    mergedProperties.putAll(leftProperties);
    for (final java.util.Map.Entry<Object, Object> rightEntry : rightProperties
            .entrySet()) {
        if (!(rightEntry.getKey() instanceof String)) {
            continue;
        }
        mergedProperties.put(rightEntry.getKey(), rightEntry.getValue());
    }
    return mergedProperties;
}'''}

        def _java_method__read_properties(self):
            name = self.java_name()
            return {'__readProperties': """\
private static java.util.Properties __readProperties(final java.io.File propertiesFilePath) {
    final java.util.Properties properties = new java.util.Properties();
    try (final java.io.FileReader propertiesFileReader = new java.io.FileReader(
            propertiesFilePath)) {
        properties.load(propertiesFileReader);
        logger.debug("read properties file {}", propertiesFilePath);
    } catch (final java.io.FileNotFoundException e) {
        logger.debug("properties file {} not found", propertiesFilePath);
    } catch (final java.io.IOException e) {
        logger.warn("unable to read properties file {}: ", propertiesFilePath, e);
    }
    return properties;
}

private static java.util.Properties __readProperties(final String propertiesResourceName) {
    final java.util.Properties properties = new java.util.Properties();

    final java.io.InputStream propertiesInputStream = %(name)s.class
            .getResourceAsStream(propertiesResourceName);
    if (propertiesInputStream == null) {
        logger.debug("properties file {} not found in the CLASSPATH", propertiesResourceName);
        return properties;
    }

    try {
        try {
            properties.load(propertiesInputStream);
            logger.debug("read properties file {} from CLASSPATH", propertiesResourceName);
        } finally {
            propertiesInputStream.close();
        }
    } catch (final java.io.IOException e) {
        logger.warn("unable to read properties file {} from the CLASSPATH: ", propertiesResourceName, e);
    }
    return properties;
}""" % locals()}

        def _java_method_to_map(self):
            fields_to_map = "\n".join(indent(' ' * 4, (field.java_to_map_put('builder')
                                             for field in self.fields)))
            return {'toMap': """\
public com.google.common.collect.ImmutableMap<String, Object> toMap() {
    final com.google.common.collect.ImmutableMap.Builder<String, Object> builder = com.google.common.collect.ImmutableMap.builder();
%(fields_to_map)s
    return builder.build();
}""" % locals()}

        def _java_methods(self):
            methods = JavaGenerator.StructType._java_methods(self)
            methods.update(self._java_method_load())
            methods.update(self._java_method__merge_properties())
            methods.update(self._java_method__read_properties())
            methods.update(self._java_method_to_map())
            return methods