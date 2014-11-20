#ifndef _THRYFT_EXCEPTION_HPP_
#define _THRYFT_EXCEPTION_HPP_

#include <exception>
#include <string>

#include "thryft/base.hpp"

namespace thryft {
class Exception : public ::thryft::Base, public ::std::exception {
  public:
    Exception() {
    }

    Exception(const ::std::string& what)
      : what_(what) {
    }

    virtual ~Exception() throw() {
    }

  public:
    const char* what() const throw() override {
      return what_.c_str();
    }

  private:
    ::std::string what_;
};
}

#endif  // _THRYFT_EXCEPTION_HPP_
