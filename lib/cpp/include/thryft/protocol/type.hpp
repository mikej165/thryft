#ifndef _THRYFT_PROTOCOL_TYPE_HPP_
#define _THRYFT_PROTOCOL_TYPE_HPP_

namespace thryft {
namespace protocol {
enum class Type {
  STOP       = 0,
#ifdef VOID
#undef VOID
#endif
  VOID       = 1,
  BOOL       = 2,
  BYTE       = 3,
  I08        = 3,
  I16        = 6,
  I32        = 8,
  U64        = 9,
  I64        = 10,
  DOUBLE     = 4,
  STRING     = 11,
  UTF7       = 11,
  STRUCT     = 12,
  MAP        = 13,
  SET        = 14,
  LIST       = 15,
  UTF8       = 16,
  UTF16      = 17,
  FLOAT      = 18
};
}
}

#endif  // _THRYFT_PROTOCOL_TYPE_HPP_
