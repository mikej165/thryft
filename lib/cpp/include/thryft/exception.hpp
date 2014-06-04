#ifndef _THRYFT_EXCEPTION_HPP_
#define _THRYFT_EXCEPTION_HPP_

#include <exception>

#include "thryft/base.hpp"

namespace thryft {
class Exception : public ::thryft::Base, public ::std::exception {
  public:
    Exception() {
    }

    virtual ~Exception() throw() {
    }
};
}

#endif  // _THRYFT_EXCEPTION_HPP_
