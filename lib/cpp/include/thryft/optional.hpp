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

    Optional(const T& value) {
      init(value);
    }

    Optional(const Optional<T>& other) {
      if (other.present_) {
        init(other.get());
      } else {
        present_ = false;
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

    const T* operator->() const {
      return &get();
    }

    T* operator->() {
      return &get();
    }

    operator bool() const {
      return present_;
    }

    Optional<T>& operator=(const T& value) {
      return set(value);
    }

    Optional<T>& operator=(const Optional<T>& value) {
      return set(value);
    }

    bool present() const {
      return present_;
    }

    Optional<T>& set(const T& value) {
      destroy();
      init(value);
      return *this;
    }

    Optional<T>& set(const Optional<T>& value) {
      destroy();
      if (value.present_) {
        init(value.get());
      }
      return *this;
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
      present_ = true;
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
