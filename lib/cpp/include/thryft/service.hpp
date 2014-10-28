#ifndef _THRYFT_SERVICE_HPP_
#define _THRYFT_SERVICE_HPP_

#include "thryft/struct.hpp"

namespace thryft {
class Exception;

template <class ServiceT>
class Service {
public:
  class Messages {
  public:
    class Response : public Struct {
    };

    class RequestHandler {
    };

    class Request : public Struct {
    public:
      virtual void respond(const Exception&) const {
      }

      virtual void respond(Response&) const {
      }
    };
  };

public:
  virtual ~Service() {
  }
};
}

#endif  // _THRYFT_SERVICE_HPP_
