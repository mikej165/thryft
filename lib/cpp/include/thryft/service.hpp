#ifndef _THRYFT_SERVICE_HPP_
#define _THRYFT_SERVICE_HPP_

#include "thryft/struct.hpp"

namespace thryft {
class Service {
public:
  class Message : public ::thryft::Struct {
  };

  class RequestHandler {
  };

public:
  virtual ~Service() {
  }
};
}

#endif  // _THRYFT_SERVICE_HPP_
