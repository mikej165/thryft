#ifndef _THRYFT_ENUM_VALUE_EXCEPTION_HPP_
#define _THRYFT_ENUM_VALUE_EXCEPTION_HPP_

#include "thryft/exception.hpp"

namespace thryft {
class EnumValueException final : public Exception {
  public:
    virtual ~EnumValueException() throw() {
    }

  public:
    // thryft::Exception
    virtual void read(protocol::InputProtocol& iprot) override {
    }

    virtual void write(protocol::OutputProtocol& oprot) const override {
    }
};
}

#endif  // _THRYFT_ENUM_VALUE_EXCEPTION_HPP_
