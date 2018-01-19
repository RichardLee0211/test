#
# Find the native PNG includes and library
#

# This module defines
# PNG_INCLUDE_DIR, whre to find png.h, etc
# PNG_LIBRARIES, the libraries to link against to use PNG
# PNG_DEFINITIONS - You should call
# add_definitions (${PNG_DEFINITIONS}) defore compiling code
# that include png library files.
# PNG_FOUND, if false, do not try to use PNG.

# also defined, but not for general use are
# PNG_LIBRARY, where to find the PNG library.

# None of the above will be defined unless zlib can be found

# PNG depends on Zlib
include( FindZLIB.cmake )

if(ZLIB_FOUND)
    find_path(PNG_PNG_INCLUDE_DIR png.h
        /usr/local/include
        /usr/include
        )

    find_library(PNG_LIBRARY png
        /usr/lib
        /usr/local/lib
        )

    if(PNG_LIBRARY)
        if(PNG_PNG_INCLUDE_DIR)
            # png.h includes zlib.h. Sign.
            set(PNG_INCLUDE_DIR
                ${PNG_PNG_INCLUDE_DIR} ${ZLIB_INCLUDE_DIR} )
            set(PNG_LIBRARIES ${PNG_LIBRARY} ${ZLIB_INCLUDE_DIR} )
            set(PNG_FOUND "Yes")

            if(CYGWIN)
                if(BUILD_SHARED_LIBS)
                    # No need to define PNG_USE_DLL here, because
                    # it's default for Cygwin.
                else(BUILD_SHARED_LIBS)
                    set (PNG_DEFINITIONS -DPNG_STATIC)
                endif(BUILD_SHARE_LIBS)
            endif(CYGWIN)

        endif()
    endif()

endif()
