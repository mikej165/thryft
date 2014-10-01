#ifndef _THRYFT_CONFIG_HPP_
#define _THRYFT_CONFIG_HPP_

#ifdef __GNUC__
 #if __GNUC__*100 + __GNUC_MINOR__ < 40700
  #define override
  #define final
 #endif //GCC version
#else
 #ifdef _MSC_VER
  #if _MSC_VER < 1600
   #define override
   #define final
  #endif
 #endif
#endif

#endif // _THRYFT_CONFIG_HPP_
