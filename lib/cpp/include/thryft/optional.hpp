#ifndef _THRYFT_OPTIONAL_HPP_
#define _THRYFT_OPTIONAL_HPP_

#include <new>

namespace thryft {
template <typename T>
class Optional {
  public:
    Optional()
      : present_(false) {
    }

    Optional(const T& value)
      : present_(true) {
      init(value);
    }

    Optional(const Optional<T>& other)
      : present_(other.present_) {
      if (present_) {
        init(other.get());
      }
    }

    ~Optional() {
      destroy();
    }

    const T& get() const {
      return *static_cast<const T*>(value());
    }

    T& get() {
      return *static_cast<T*>(value());
    }

    T& operator*() {
      return get();
    }

    const T& operator*() const {
      return get();
    }

    operator bool() const {
      return present_;
    }

    Optional<T>& operator=(const T& value) {
      destroy();
      this->present_ = true;
      init(value);
      return *this;
    }

    Optional<T>& operator=(const Optional<T>& value) {
      destroy();
      if (present_ == value.present_) {
        init(value.get());
      }
      return *this;
    }

    bool present() const {
      return present_;
    }

  private:
    void destroy() {
      if (present_) {
        get().~T();
        present_ = false;
      }
    }

    void init(const T& value) {
      new(this->value()) T(value);
    }

    void* value() {
      return value_;
    }

    const void* value() const {
      return value_;
    }

  private:
    char value_[sizeof(T)];
    bool present_; // After value_ in case value_ falls short of alignment
};
}

#endif  // _THRYFT_OPTIONAL_HPP_
