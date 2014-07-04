#-------------------------------------------------------------------------------
# Copyright (c) 2013, Minor Gordon
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL  DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
# OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
# OF SUCH DAMAGE.
#-------------------------------------------------------------------------------

from thryft.generators.java import java_generator
from thryft.generators.java.java_document import JavaDocument
from thryft.generators.java.java_function import JavaFunction
from thryft.generators.java.java_service import JavaService
from yutil import lpad


class _ServletJavaGenerator(java_generator.JavaGenerator):
    class _Document(JavaDocument):
        def __init__(self, servlet_type, **kwds):
            JavaDocument.__init__(self, **kwds)
            self.__servlet_type = servlet_type

        def java_package(self):
            try:
                return self.namespace_by_scope((self.__servlet_type + '_servlet_java', 'servlet_java', 'java')).name
            except KeyError:
                return None

#         def _save(self, out_file_path):
#             out_dir_path, out_file_name = os.path.split(out_file_path)
#             out_file_base_name, out_file_ext = os.path.splitext(out_file_name)
#             out_file_path = os.path.join(out_dir_path, camelize(out_file_base_name) + self.__servlet_type.capitalize() + 'Servlet' + out_file_ext)
#             return JavaDocument._save(self, out_file_path)

    class _Function(JavaFunction):
        def _java_read_http_servlet_request_body(self, **kwds):
            return self.parent._java_read_http_servlet_request_body(**kwds)

        def _java_write_http_servlet_response_body(self, **kwds):
            return self.parent._java_write_http_servlet_response_body(**kwds)

    class _Service(JavaService):
        def _java_write_http_servlet_response_body(self, content_type='application/json', headers=None, variable_name_prefix=''):
            if headers is not None:
                headers = \
                    lpad("\n", "\n".join(
                        """%shttpServletResponse.setHeader("%s", "%s");""" % (variable_name_prefix, header_name, headers[header_name])
                        for header_name in sorted(headers.keys())))
            else:
                headers = ''
            return """\
// TODO: remove from production
%(variable_name_prefix)shttpServletResponse.setContentType("%(content_type)s");%(headers)s

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

final String %(variable_name_prefix)shttpServletRequestBody;
{
    final java.io.InputStreamReader %(variable_name_prefix)shttpServletRequestBodyReader = new java.io.InputStreamReader(%(variable_name_prefix)shttpServletRequestInputStream);
    final java.io.StringWriter %(variable_name_prefix)shttpServletRequestBodyWriter = new java.io.StringWriter();
    final char[] %(variable_name_prefix)shttpServletRequestBodyBuffer = new char[4096];
    int %(variable_name_prefix)shttpServletRequestBodyBufferReadRet = 0;
    while ((%(variable_name_prefix)shttpServletRequestBodyBufferReadRet = %(variable_name_prefix)shttpServletRequestBodyReader.read(%(variable_name_prefix)shttpServletRequestBodyBuffer)) != -1) {
        %(variable_name_prefix)shttpServletRequestBodyWriter.write(%(variable_name_prefix)shttpServletRequestBodyBuffer, 0, %(variable_name_prefix)shttpServletRequestBodyBufferReadRet);
    }
    %(variable_name_prefix)shttpServletRequestBody = %(variable_name_prefix)shttpServletRequestBodyWriter.toString();
}
""" % locals()
