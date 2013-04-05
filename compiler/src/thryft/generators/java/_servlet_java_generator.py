from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import camelize
import os.path


class _ServletJavaGenerator(java_generator.JavaGenerator):
    class _Document(JavaDocument):
        def __init__(self, servlet_type, **kwds):
            JavaDocument.__init__(self, **kwds)
            self.__servlet_type = servlet_type

        def _save(self, out_file_path):
            out_dir_path, out_file_name = os.path.split(out_file_path)
            out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
            out_file_path = os.path.join(out_dir_path, camelize(out_file_base_name) + self.__servlet_type.capitalize() + 'Servlet' + out_file_ext)
            return JavaDocument._save(self, out_file_path)

    class _Function(JavaFunction):
        def _java_read_http_servlet_request_body(self, **kwds):
            return self.parent._java_read_http_servlet_request_body(**kwds)

        def _java_write_http_servlet_response_body(self, **kwds):
            return self.parent._java_write_http_servlet_response_body(**kwds)

    class _Service(JavaService):
        def _java_write_http_servlet_response_body(self, content_type='application/json', variable_name_prefix=''):
            return """\
if (%(variable_name_prefix)shttpServletResponseBody.length() >= 128) {
    final String %(variable_name_prefix)shttpServletRequestAcceptEncoding = %(variable_name_prefix)shttpServletRequest.getHeader("Accept-Encoding");
    if (%(variable_name_prefix)shttpServletRequestAcceptEncoding != null && !%(variable_name_prefix)shttpServletRequestAcceptEncoding.isEmpty()) {
        final String[] contentCodings = %(variable_name_prefix)shttpServletRequestAcceptEncoding.split(",");
        final java.util.TreeMap<java.math.BigDecimal, String> contentCodingsMap = new java.util.TreeMap<java.math.BigDecimal, String>();
        java.math.BigDecimal nextQvalue = new java.math.BigDecimal(Long.MAX_VALUE);
        for (final String contentCoding : contentCodings) {
            final String[] contentCodingSplit = contentCoding.split(";", 2);
            final String name = contentCodingSplit[0].trim();
            final java.math.BigDecimal qvalue;
            if (contentCodingSplit.length == 2) {
                final String[] qvalueSplit = contentCodingSplit[1].split("=", 2);
                if (qvalueSplit.length == 2) {
                    try {
                        qvalue = new java.math.BigDecimal(qvalueSplit[1].trim());
                        if (qvalue == java.math.BigDecimal.ZERO) {
                            continue;
                        }
                    } catch (final NumberFormatException e) {
                        continue;
                    }
                } else {
                    continue;
                }
            } else {
                qvalue = nextQvalue;
                nextQvalue = nextQvalue.subtract(java.math.BigDecimal.ONE);
            }
            contentCodingsMap.put(qvalue, name);
        }

        if (!contentCodingsMap.isEmpty()) {
            final String contentCoding = contentCodingsMap.lastEntry().getValue();
            if (contentCoding.equals("deflate") || contentCoding.equals("gzip")) {
                final java.io.ByteArrayOutputStream byteArrayOutputStream = new java.io.ByteArrayOutputStream();

                final java.util.zip.DeflaterOutputStream compressingOutputStream;
                if (contentCoding.equals("deflate")) {
                    compressingOutputStream = new java.util.zip.DeflaterOutputStream(byteArrayOutputStream);
                } else {
                    compressingOutputStream = new java.util.zip.GZIPOutputStream(byteArrayOutputStream);
                }

                byte[] compressedHttpServletResponseBody = null;
                try {
                    try {
                        compressingOutputStream.write(%(variable_name_prefix)shttpServletResponseBody.getBytes());
                        compressingOutputStream.finish();
                        compressedHttpServletResponseBody = byteArrayOutputStream.toByteArray();
                    } finally {
                        compressingOutputStream.close();
                    }
                } catch (java.io.IOException e) {
                }

                if (compressedHttpServletResponseBody != null) {
                    %(variable_name_prefix)shttpServletResponse.setHeader("Content-Encoding", contentCoding);
                    %(variable_name_prefix)shttpServletResponse.getOutputStream().write(compressedHttpServletResponseBody);
                    return;
                }
            }
        }
    }
}

%(variable_name_prefix)shttpServletResponse.setContentType("application/json");
%(variable_name_prefix)shttpServletResponse.getWriter().write(%(variable_name_prefix)shttpServletResponseBody);""" % locals()

        def _java_read_http_servlet_request_body(self, variable_name_prefix=''):
            return """\
final String %(variable_name_prefix)shttpServletRequestContentEncoding = %(variable_name_prefix)shttpServletRequest.getHeader("Content-Encoding");
java.io.InputStream %(variable_name_prefix)shttpServletRequestInputStream = %(variable_name_prefix)shttpServletRequest.getInputStream();
if (%(variable_name_prefix)shttpServletRequestContentEncoding != null) {
    if (%(variable_name_prefix)shttpServletRequestContentEncoding.equals("deflate")) {
        %(variable_name_prefix)shttpServletRequestInputStream = new java.util.zip.InflaterInputStream(%(variable_name_prefix)shttpServletRequestInputStream);
    } else if (%(variable_name_prefix)shttpServletRequestContentEncoding.equals("gzip")) {
        %(variable_name_prefix)shttpServletRequestInputStream = new java.util.zip.GZIPInputStream(%(variable_name_prefix)shttpServletRequestInputStream);
    }
}

final String %(variable_name_prefix)shttpServletRequestBody = org.apache.commons.io.IOUtils.toString(%(variable_name_prefix)shttpServletRequestInputStream);
""" % locals()
