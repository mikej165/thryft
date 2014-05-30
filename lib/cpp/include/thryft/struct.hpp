#ifndef _THRYFT_STRUCT_HPP_
#define _THRYFT_STRUCT_HPP_

#include "thryft/base.hpp"

namespace thryft {
class Struct : public ::thryft::Base {
  public:
    virtual ~Struct() {
    }

  public:
    virtual operator ::std::string() const = 0;
};
}

static inline
std::ostream&
operator<<(
  std::ostream& os,
  const ::thryft::Struct& struct_
) {
  os << static_cast< ::std::string >(struct_);
  return os;
}

#endif  // _THRYFT_STRUCT_HPP_
