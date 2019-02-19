➜  testOpenCV git:(master) ✗ pip2 install numpy
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/39/17/f296f19b342975f6a6e653ef74a59fce9a8eeb2b052961f70c5f036fb8c1/numpy-1.16.1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (13.9MB)
    100% |████████████████████████████████| 13.9MB 1.7MB/s
Installing collected packages: numpy
Successfully installed numpy-1.16.1
➜  testOpenCV git:(master) ✗ pip2 install scipy
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Collecting scipy
  Downloading https://files.pythonhosted.org/packages/85/70/9f8f1e9ed9fd33b96bb27fb080171fb571f7d33fecbd857e9f504e6dcc9a/scipy-1.2.1-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (27.4MB)
    100% |████████████████████████████████| 27.4MB 908kB/s
Requirement already satisfied: numpy>=1.8.2 in /usr/local/lib/python2.7/site-packages (from scipy) (1.16.1)
Installing collected packages: scipy
Successfully installed scipy-1.2.1
➜  testOpenCV git:(master) ✗ brew install opencv
==> Installing dependencies for opencv: eigen, aom, fontconfig, frei0r, gmp, libtasn1, nettle, libffi, p11-kit, gnutls, lame, fribidi, glib, pixman, cairo, graphite2, icu4c, harfbuzz, libass, libbluray, libsoxr, libogg, libvorbis, libvpx, opencore-amr, opus, rtmpdump, flac, libsndfile, libsamplerate, rubberband, sdl2, snappy, speex, giflib, leptonica, tesseract, theora, x264, xvid, ffmpeg, isl, mpfr, libmpc, gcc, openblas, python, numpy and tbb
==> Installing opencv dependency: eigen
==> Downloading https://homebrew.bintray.com/bottles/eigen-3.3.7.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring eigen-3.3.7.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/eigen/3.3.7: 487 files, 6.5MB
==> Installing opencv dependency: aom
==> Downloading https://homebrew.bintray.com/bottles/aom-1.0.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring aom-1.0.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/aom/1.0.0: 19 files, 12.4MB
==> Installing opencv dependency: fontconfig
==> Downloading https://homebrew.bintray.com/bottles/fontconfig-2.13.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring fontconfig-2.13.1.sierra.bottle.tar.gz
==> Regenerating font cache, this may take a while
==> /usr/local/Cellar/fontconfig/2.13.1/bin/fc-cache -frv
🍺  /usr/local/Cellar/fontconfig/2.13.1: 531 files, 3.3MB
==> Installing opencv dependency: frei0r
==> Downloading https://homebrew.bintray.com/bottles/frei0r-1.6.1.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring frei0r-1.6.1.sierra.bottle.1.tar.gz
🍺  /usr/local/Cellar/frei0r/1.6.1: 137 files, 2.0MB
==> Installing opencv dependency: gmp
==> Downloading https://homebrew.bintray.com/bottles/gmp-6.1.2_2.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring gmp-6.1.2_2.sierra.bottle.1.tar.gz
🍺  /usr/local/Cellar/gmp/6.1.2_2: 18 files, 3.1MB
==> Installing opencv dependency: libtasn1
==> Downloading https://homebrew.bintray.com/bottles/libtasn1-4.13.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libtasn1-4.13.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libtasn1/4.13: 59 files, 435.2KB
==> Installing opencv dependency: nettle
==> Downloading https://homebrew.bintray.com/bottles/nettle-3.4.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring nettle-3.4.1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/nettle/3.4.1: 85 files, 2MB
==> Installing opencv dependency: libffi
==> Downloading https://homebrew.bintray.com/bottles/libffi-3.2.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libffi-3.2.1.sierra.bottle.tar.gz
==> Caveats
libffi is keg-only, which means it was not symlinked into /usr/local,
because some formulae require a newer version of libffi.

For compilers to find libffi you may need to set:
  export LDFLAGS="-L/usr/local/opt/libffi/lib"

For pkg-config to find libffi you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/libffi/3.2.1: 16 files, 297.0KB
==> Installing opencv dependency: p11-kit
==> Downloading https://homebrew.bintray.com/bottles/p11-kit-0.23.15.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring p11-kit-0.23.15.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/p11-kit/0.23.15: 63 files, 2.9MB
==> Installing opencv dependency: gnutls
==> Downloading https://homebrew.bintray.com/bottles/gnutls-3.6.6.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring gnutls-3.6.6.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/gnutls/3.6.6: 1,200 files, 8.9MB
==> Installing opencv dependency: lame
==> Downloading https://homebrew.bintray.com/bottles/lame-3.100.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring lame-3.100.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/lame/3.100: 27 files, 2.1MB
==> Installing opencv dependency: fribidi
==> Downloading https://homebrew.bintray.com/bottles/fribidi-1.0.5.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring fribidi-1.0.5.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/fribidi/1.0.5: 66 files, 581.4KB
==> Installing opencv dependency: glib
==> Downloading https://homebrew.bintray.com/bottles/glib-2.58.3.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring glib-2.58.3.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/glib/2.58.3: 435 files, 18.5MB
==> Installing opencv dependency: pixman
==> Downloading https://homebrew.bintray.com/bottles/pixman-0.38.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring pixman-0.38.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/pixman/0.38.0: 13 files, 1.3MB
==> Installing opencv dependency: cairo
==> Downloading https://homebrew.bintray.com/bottles/cairo-1.16.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring cairo-1.16.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/cairo/1.16.0: 117 files, 5.5MB
==> Installing opencv dependency: graphite2
==> Downloading https://homebrew.bintray.com/bottles/graphite2-1.3.13.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring graphite2-1.3.13.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/graphite2/1.3.13: 18 files, 236.3KB
==> Installing opencv dependency: icu4c
==> Downloading https://homebrew.bintray.com/bottles/icu4c-63.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring icu4c-63.1.sierra.bottle.tar.gz
==> Caveats
icu4c is keg-only, which means it was not symlinked into /usr/local,
because macOS provides libicucore.dylib (but nothing else).

If you need to have icu4c first in your PATH run:
  echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

For compilers to find icu4c you may need to set:
  export LDFLAGS="-L/usr/local/opt/icu4c/lib"
  export CPPFLAGS="-I/usr/local/opt/icu4c/include"

For pkg-config to find icu4c you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/icu4c/63.1: 254 files, 68.3MB
==> Installing opencv dependency: harfbuzz
==> Downloading https://homebrew.bintray.com/bottles/harfbuzz-2.3.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring harfbuzz-2.3.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/harfbuzz/2.3.0: 179 files, 9.5MB
==> Installing opencv dependency: libass
==> Downloading https://homebrew.bintray.com/bottles/libass-0.14.0_1.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring libass-0.14.0_1.sierra.bottle.1.tar.gz
🍺  /usr/local/Cellar/libass/0.14.0_1: 10 files, 510.1KB
==> Installing opencv dependency: libbluray
==> Downloading https://homebrew.bintray.com/bottles/libbluray-1.0.2.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libbluray-1.0.2.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libbluray/1.0.2: 20 files, 1.5MB
==> Installing opencv dependency: libsoxr
==> Downloading https://homebrew.bintray.com/bottles/libsoxr-0.1.3.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libsoxr-0.1.3.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libsoxr/0.1.3: 28 files, 242.5KB
==> Installing opencv dependency: libogg
==> Downloading https://homebrew.bintray.com/bottles/libogg-1.3.3.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libogg-1.3.3.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libogg/1.3.3: 97 files, 460.5KB
==> Installing opencv dependency: libvorbis
==> Downloading https://homebrew.bintray.com/bottles/libvorbis-1.3.6.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libvorbis-1.3.6.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libvorbis/1.3.6: 157 files, 2.3MB
==> Installing opencv dependency: libvpx
==> Downloading https://homebrew.bintray.com/bottles/libvpx-1.8.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libvpx-1.8.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libvpx/1.8.0: 17 files, 2.2MB
==> Installing opencv dependency: opencore-amr
==> Downloading https://homebrew.bintray.com/bottles/opencore-amr-0.1.5.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring opencore-amr-0.1.5.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/opencore-amr/0.1.5: 17 files, 638.4KB
==> Installing opencv dependency: opus
==> Downloading https://homebrew.bintray.com/bottles/opus-1.3.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring opus-1.3.sierra.bottle.1.tar.gz
🍺  /usr/local/Cellar/opus/1.3: 17 files, 982.6KB
==> Installing opencv dependency: rtmpdump
==> Downloading https://homebrew.bintray.com/bottles/rtmpdump-2.4+20151223.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring rtmpdump-2.4 20151223.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/rtmpdump/2.4+20151223: 19 files, 422.2KB
==> Installing opencv dependency: flac
==> Downloading https://homebrew.bintray.com/bottles/flac-1.3.2_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring flac-1.3.2_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/flac/1.3.2_1: 53 files, 1.8MB
==> Installing opencv dependency: libsndfile
==> Downloading https://homebrew.bintray.com/bottles/libsndfile-1.0.28.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libsndfile-1.0.28.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libsndfile/1.0.28: 48 files, 1.8MB
==> Installing opencv dependency: libsamplerate
==> Downloading https://homebrew.bintray.com/bottles/libsamplerate-0.1.9_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libsamplerate-0.1.9_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libsamplerate/0.1.9_1: 28 files, 3.0MB
==> Installing opencv dependency: rubberband
==> Downloading https://homebrew.bintray.com/bottles/rubberband-1.8.2_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring rubberband-1.8.2_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/rubberband/1.8.2_1: 12 files, 643.4KB
==> Installing opencv dependency: sdl2
==> Downloading https://homebrew.bintray.com/bottles/sdl2-2.0.9.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring sdl2-2.0.9.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/sdl2/2.0.9: 87 files, 4.5MB
==> Installing opencv dependency: snappy
==> Downloading https://homebrew.bintray.com/bottles/snappy-1.1.7_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring snappy-1.1.7_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/snappy/1.1.7_1: 18 files, 118.1KB
==> Installing opencv dependency: speex
==> Downloading https://homebrew.bintray.com/bottles/speex-1.2.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring speex-1.2.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/speex/1.2.0: 21 files, 689.6KB
==> Installing opencv dependency: giflib
==> Downloading https://homebrew.bintray.com/bottles/giflib-5.1.4_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring giflib-5.1.4_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/giflib/5.1.4_1: 21 files, 312.7KB
==> Installing opencv dependency: leptonica
==> Downloading https://homebrew.bintray.com/bottles/leptonica-1.77.0_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring leptonica-1.77.0_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/leptonica/1.77.0_1: 48 files, 5.8MB
==> Installing opencv dependency: tesseract
==> Downloading https://homebrew.bintray.com/bottles/tesseract-4.0.0_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring tesseract-4.0.0_1.sierra.bottle.tar.gz
==> Caveats
This formula containes only the "eng", "osd", and "snum" language data files.
If you need all the other supported languages, `brew install tesseract-lang`.
==> Summary
🍺  /usr/local/Cellar/tesseract/4.0.0_1: 63 files, 30.1MB
==> Installing opencv dependency: theora
==> Downloading https://homebrew.bintray.com/bottles/theora-1.1.1.sierra.bottle.2.tar.gz
######################################################################## 100.0%
==> Pouring theora-1.1.1.sierra.bottle.2.tar.gz
🍺  /usr/local/Cellar/theora/1.1.1: 96 files, 2.1MB
==> Installing opencv dependency: x264
==> Downloading https://homebrew.bintray.com/bottles/x264-r2917.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring x264-r2917.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/x264/r2917: 11 files, 5.9MB
==> Installing opencv dependency: xvid
==> Downloading https://homebrew.bintray.com/bottles/xvid-1.3.5.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring xvid-1.3.5.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/xvid/1.3.5: 10 files, 1.2MB
==> Installing opencv dependency: ffmpeg
==> Downloading https://homebrew.bintray.com/bottles/ffmpeg-4.1.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring ffmpeg-4.1.1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/ffmpeg/4.1.1: 282 files, 58.6MB
==> Installing opencv dependency: isl
==> Downloading https://homebrew.bintray.com/bottles/isl-0.20.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring isl-0.20.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/isl/0.20: 71 files, 3.9MB
==> Installing opencv dependency: mpfr
==> Downloading https://homebrew.bintray.com/bottles/mpfr-4.0.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring mpfr-4.0.1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/mpfr/4.0.1: 28 files, 4.6MB
==> Installing opencv dependency: libmpc
==> Downloading https://homebrew.bintray.com/bottles/libmpc-1.1.0.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring libmpc-1.1.0.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/libmpc/1.1.0: 12 files, 353.9KB
==> Installing opencv dependency: gcc
==> Downloading https://homebrew.bintray.com/bottles/gcc-8.2.0.sierra.bottle.2.tar.gz
######################################################################## 100.0%
==> Pouring gcc-8.2.0.sierra.bottle.2.tar.gz
🍺  /usr/local/Cellar/gcc/8.2.0: 1,494 files, 343.6MB
==> Installing opencv dependency: openblas
==> Downloading https://homebrew.bintray.com/bottles/openblas-0.3.5.sierra.bottle.1.tar.gz
######################################################################## 100.0%
==> Pouring openblas-0.3.5.sierra.bottle.1.tar.gz
==> Caveats
openblas is keg-only, which means it was not symlinked into /usr/local,
because macOS provides BLAS and LAPACK in the Accelerate framework.

For compilers to find openblas you may need to set:
  export LDFLAGS="-L/usr/local/opt/openblas/lib"
  export CPPFLAGS="-I/usr/local/opt/openblas/include"

For pkg-config to find openblas you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/openblas/lib/pkgconfig"

==> Summary
🍺  /usr/local/Cellar/openblas/0.3.5: 21 files, 120.8MB
==> Installing opencv dependency: python
==> Downloading https://homebrew.bintray.com/bottles/python-3.7.2_2.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring python-3.7.2_2.sierra.bottle.tar.gz
==> /usr/local/Cellar/python/3.7.2_2/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> /usr/local/Cellar/python/3.7.2_2/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> /usr/local/Cellar/python/3.7.2_2/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/
==> Caveats
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /usr/local/Cellar/python/3.7.2_2: 3,861 files, 59.7MB
==> Installing opencv dependency: numpy
==> Downloading https://homebrew.bintray.com/bottles/numpy-1.16.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring numpy-1.16.1.sierra.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/f2py
Target /usr/local/bin/f2py
already exists. You may want to remove it:
  rm '/usr/local/bin/f2py'

To force the link and overwrite all conflicting files:
  brew link --overwrite numpy

To list all files that would be deleted:
  brew link --overwrite --dry-run numpy

Possible conflicting files are:
/usr/local/bin/f2py
/usr/local/bin/f2py2
/usr/local/bin/f2py2.7
/usr/local/lib/python2.7/site-packages/numpy/LICENSE.txt
/usr/local/lib/python2.7/site-packages/numpy/__config__.py
/usr/local/lib/python2.7/site-packages/numpy/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/_distributor_init.py
/usr/local/lib/python2.7/site-packages/numpy/_globals.py
/usr/local/lib/python2.7/site-packages/numpy/_pytesttester.py
/usr/local/lib/python2.7/site-packages/numpy/compat/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/compat/_inspect.py
/usr/local/lib/python2.7/site-packages/numpy/compat/py3k.py
/usr/local/lib/python2.7/site-packages/numpy/compat/setup.py
/usr/local/lib/python2.7/site-packages/numpy/compat/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/compat/tests/test_compat.py
/usr/local/lib/python2.7/site-packages/numpy/conftest.py
/usr/local/lib/python2.7/site-packages/numpy/core/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/core/_add_newdocs.py
/usr/local/lib/python2.7/site-packages/numpy/core/_aliased_types.py
/usr/local/lib/python2.7/site-packages/numpy/core/_dtype.py
/usr/local/lib/python2.7/site-packages/numpy/core/_dtype_ctypes.py
/usr/local/lib/python2.7/site-packages/numpy/core/_dummy.so
/usr/local/lib/python2.7/site-packages/numpy/core/_internal.py
/usr/local/lib/python2.7/site-packages/numpy/core/_methods.py
/usr/local/lib/python2.7/site-packages/numpy/core/_multiarray_module_test.so
/usr/local/lib/python2.7/site-packages/numpy/core/_multiarray_tests.so
/usr/local/lib/python2.7/site-packages/numpy/core/_multiarray_umath.so
/usr/local/lib/python2.7/site-packages/numpy/core/_operand_flag_tests.so
/usr/local/lib/python2.7/site-packages/numpy/core/_rational_tests.so
/usr/local/lib/python2.7/site-packages/numpy/core/_string_helpers.py
/usr/local/lib/python2.7/site-packages/numpy/core/_struct_ufunc_tests.so
/usr/local/lib/python2.7/site-packages/numpy/core/_type_aliases.py
/usr/local/lib/python2.7/site-packages/numpy/core/_umath_tests.so
/usr/local/lib/python2.7/site-packages/numpy/core/arrayprint.py
/usr/local/lib/python2.7/site-packages/numpy/core/cversions.py
/usr/local/lib/python2.7/site-packages/numpy/core/defchararray.py
/usr/local/lib/python2.7/site-packages/numpy/core/einsumfunc.py
/usr/local/lib/python2.7/site-packages/numpy/core/fromnumeric.py
/usr/local/lib/python2.7/site-packages/numpy/core/function_base.py
/usr/local/lib/python2.7/site-packages/numpy/core/generate_numpy_api.py
/usr/local/lib/python2.7/site-packages/numpy/core/getlimits.py
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/__multiarray_api.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/__ufunc_api.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/_neighborhood_iterator_imp.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/_numpyconfig.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/arrayobject.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/arrayscalars.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/halffloat.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/multiarray_api.txt
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/ndarrayobject.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/ndarraytypes.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/noprefix.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_3kcompat.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_common.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_cpu.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_endian.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_interrupt.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_math.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_no_deprecated_api.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/npy_os.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/numpyconfig.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/old_defines.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/oldnumeric.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/ufunc_api.txt
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/ufuncobject.h
/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy/utils.h
/usr/local/lib/python2.7/site-packages/numpy/core/info.py
/usr/local/lib/python2.7/site-packages/numpy/core/lib/libnpymath.a
/usr/local/lib/python2.7/site-packages/numpy/core/lib/npy-pkg-config/mlib.ini
/usr/local/lib/python2.7/site-packages/numpy/core/lib/npy-pkg-config/npymath.ini
/usr/local/lib/python2.7/site-packages/numpy/core/machar.py
/usr/local/lib/python2.7/site-packages/numpy/core/memmap.py
/usr/local/lib/python2.7/site-packages/numpy/core/multiarray.py
/usr/local/lib/python2.7/site-packages/numpy/core/numeric.py
/usr/local/lib/python2.7/site-packages/numpy/core/numerictypes.py
/usr/local/lib/python2.7/site-packages/numpy/core/overrides.py
/usr/local/lib/python2.7/site-packages/numpy/core/records.py
/usr/local/lib/python2.7/site-packages/numpy/core/setup.py
/usr/local/lib/python2.7/site-packages/numpy/core/setup_common.py
/usr/local/lib/python2.7/site-packages/numpy/core/shape_base.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/_locales.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/data/astype_copy.pkl
/usr/local/lib/python2.7/site-packages/numpy/core/tests/data/recarray_from_file.fits
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_abc.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_api.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_arrayprint.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_datetime.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_defchararray.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_deprecations.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_dtype.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_einsum.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_errstate.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_extint128.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_function_base.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_getlimits.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_half.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_indexerrors.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_indexing.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_item_selection.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_longdouble.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_machar.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_mem_overlap.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_memmap.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_multiarray.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_nditer.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_numeric.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_numerictypes.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_overrides.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_print.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_records.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_scalar_ctors.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_scalarbuffer.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_scalarinherit.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_scalarmath.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_scalarprint.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_shape_base.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_ufunc.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_umath.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_umath_complex.py
/usr/local/lib/python2.7/site-packages/numpy/core/tests/test_unicode.py
/usr/local/lib/python2.7/site-packages/numpy/core/umath.py
/usr/local/lib/python2.7/site-packages/numpy/core/umath_tests.py
/usr/local/lib/python2.7/site-packages/numpy/ctypeslib.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/__config__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/__version__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/ccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/autodist.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/bdist_rpm.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build_clib.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build_ext.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build_py.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build_scripts.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/build_src.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/config.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/config_compiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/develop.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/egg_info.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/install.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/install_clib.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/install_data.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/install_headers.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/command/sdist.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/compat.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/conv_template.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/core.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/cpuinfo.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/exec_command.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/extension.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/absoft.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/compaq.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/environment.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/g95.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/gnu.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/hpux.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/ibm.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/intel.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/lahey.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/mips.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/nag.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/none.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/pathf95.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/pg.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/sun.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/fcompiler/vast.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/from_template.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/info.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/intelccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/lib2def.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/line_endings.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/log.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/mingw/gfortran_vs2003_hack.c
/usr/local/lib/python2.7/site-packages/numpy/distutils/mingw32ccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/misc_util.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/msvc9compiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/msvccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/npy_pkg_config.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/numpy_distribution.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/pathccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/setup.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/system_info.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_exec_command.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_fcompiler.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_fcompiler_gnu.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_fcompiler_intel.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_fcompiler_nagfor.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_from_template.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_misc_util.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_npy_pkg_config.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/tests/test_system_info.py
/usr/local/lib/python2.7/site-packages/numpy/distutils/unixccompiler.py
/usr/local/lib/python2.7/site-packages/numpy/doc/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/doc/basics.py
/usr/local/lib/python2.7/site-packages/numpy/doc/broadcasting.py
/usr/local/lib/python2.7/site-packages/numpy/doc/byteswapping.py
/usr/local/lib/python2.7/site-packages/numpy/doc/constants.py
/usr/local/lib/python2.7/site-packages/numpy/doc/creation.py
/usr/local/lib/python2.7/site-packages/numpy/doc/glossary.py
/usr/local/lib/python2.7/site-packages/numpy/doc/indexing.py
/usr/local/lib/python2.7/site-packages/numpy/doc/internals.py
/usr/local/lib/python2.7/site-packages/numpy/doc/misc.py
/usr/local/lib/python2.7/site-packages/numpy/doc/structured_arrays.py
/usr/local/lib/python2.7/site-packages/numpy/doc/subclassing.py
/usr/local/lib/python2.7/site-packages/numpy/doc/ufuncs.py
/usr/local/lib/python2.7/site-packages/numpy/dual.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/__main__.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/__version__.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/auxfuncs.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/capi_maps.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/cb_rules.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/cfuncs.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/common_rules.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/crackfortran.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/diagnose.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/f2py2e.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/f2py_testing.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/f90mod_rules.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/func2subr.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/info.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/rules.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/setup.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.c
/usr/local/lib/python2.7/site-packages/numpy/f2py/src/fortranobject.h
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/array_from_pyobj/wrapmodule.c
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/assumed_shape/.f2py_f2cmap
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/assumed_shape/foo_free.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/assumed_shape/foo_mod.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/assumed_shape/foo_use.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/assumed_shape/precision.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/common/block.f
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/kind/foo.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo.f
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo_fixed.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/mixed/foo_free.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/parameter/constant_both.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/parameter/constant_compound.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/parameter/constant_integer.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/parameter/constant_non_compound.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/parameter/constant_real.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/regression/inout.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/size/foo.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/src/string/char.f90
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_array_from_pyobj.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_assumed_shape.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_block_docstring.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_callback.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_common.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_compile_function.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_kind.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_mixed.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_parameter.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_quoted_character.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_return_character.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_return_complex.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_return_integer.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_return_logical.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_return_real.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_semicolon_split.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_size.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/test_string.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/tests/util.py
/usr/local/lib/python2.7/site-packages/numpy/f2py/use_rules.py
/usr/local/lib/python2.7/site-packages/numpy/fft/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/fft/fftpack.py
/usr/local/lib/python2.7/site-packages/numpy/fft/fftpack_lite.so
/usr/local/lib/python2.7/site-packages/numpy/fft/helper.py
/usr/local/lib/python2.7/site-packages/numpy/fft/info.py
/usr/local/lib/python2.7/site-packages/numpy/fft/setup.py
/usr/local/lib/python2.7/site-packages/numpy/fft/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/fft/tests/test_fftpack.py
/usr/local/lib/python2.7/site-packages/numpy/fft/tests/test_helper.py
/usr/local/lib/python2.7/site-packages/numpy/lib/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/lib/_datasource.py
/usr/local/lib/python2.7/site-packages/numpy/lib/_iotools.py
/usr/local/lib/python2.7/site-packages/numpy/lib/_version.py
/usr/local/lib/python2.7/site-packages/numpy/lib/arraypad.py
/usr/local/lib/python2.7/site-packages/numpy/lib/arraysetops.py
/usr/local/lib/python2.7/site-packages/numpy/lib/arrayterator.py
/usr/local/lib/python2.7/site-packages/numpy/lib/financial.py
/usr/local/lib/python2.7/site-packages/numpy/lib/format.py
/usr/local/lib/python2.7/site-packages/numpy/lib/function_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/histograms.py
/usr/local/lib/python2.7/site-packages/numpy/lib/index_tricks.py
/usr/local/lib/python2.7/site-packages/numpy/lib/info.py
/usr/local/lib/python2.7/site-packages/numpy/lib/mixins.py
/usr/local/lib/python2.7/site-packages/numpy/lib/nanfunctions.py
/usr/local/lib/python2.7/site-packages/numpy/lib/npyio.py
/usr/local/lib/python2.7/site-packages/numpy/lib/polynomial.py
/usr/local/lib/python2.7/site-packages/numpy/lib/recfunctions.py
/usr/local/lib/python2.7/site-packages/numpy/lib/scimath.py
/usr/local/lib/python2.7/site-packages/numpy/lib/setup.py
/usr/local/lib/python2.7/site-packages/numpy/lib/shape_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/stride_tricks.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/py2-objarr.npy
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/py2-objarr.npz
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/py3-objarr.npy
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/py3-objarr.npz
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/python3.npy
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/data/win64python2.npy
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test__datasource.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test__iotools.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test__version.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_arraypad.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_arraysetops.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_arrayterator.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_financial.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_format.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_function_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_histograms.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_index_tricks.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_io.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_mixins.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_nanfunctions.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_packbits.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_polynomial.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_recfunctions.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_shape_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_stride_tricks.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_twodim_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_type_check.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_ufunclike.py
/usr/local/lib/python2.7/site-packages/numpy/lib/tests/test_utils.py
/usr/local/lib/python2.7/site-packages/numpy/lib/twodim_base.py
/usr/local/lib/python2.7/site-packages/numpy/lib/type_check.py
/usr/local/lib/python2.7/site-packages/numpy/lib/ufunclike.py
/usr/local/lib/python2.7/site-packages/numpy/lib/user_array.py
/usr/local/lib/python2.7/site-packages/numpy/lib/utils.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/_umath_linalg.so
/usr/local/lib/python2.7/site-packages/numpy/linalg/info.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/lapack_lite.so
/usr/local/lib/python2.7/site-packages/numpy/linalg/linalg.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/setup.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/tests/test_build.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/tests/test_deprecations.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/tests/test_linalg.py
/usr/local/lib/python2.7/site-packages/numpy/linalg/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/ma/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/ma/bench.py
/usr/local/lib/python2.7/site-packages/numpy/ma/core.py
/usr/local/lib/python2.7/site-packages/numpy/ma/extras.py
/usr/local/lib/python2.7/site-packages/numpy/ma/mrecords.py
/usr/local/lib/python2.7/site-packages/numpy/ma/setup.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_core.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_deprecations.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_extras.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_mrecords.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_old_ma.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/ma/tests/test_subclassing.py
/usr/local/lib/python2.7/site-packages/numpy/ma/testutils.py
/usr/local/lib/python2.7/site-packages/numpy/ma/timer_comparison.py
/usr/local/lib/python2.7/site-packages/numpy/ma/version.py
/usr/local/lib/python2.7/site-packages/numpy/matlib.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/defmatrix.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/setup.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_defmatrix.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_interaction.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_masked_matrix.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_matrix_linalg.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_multiarray.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_numeric.py
/usr/local/lib/python2.7/site-packages/numpy/matrixlib/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/_polybase.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/chebyshev.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/hermite.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/hermite_e.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/laguerre.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/legendre.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/polynomial.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/polyutils.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/setup.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_chebyshev.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_classes.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_hermite.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_hermite_e.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_laguerre.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_legendre.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_polynomial.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_polyutils.py
/usr/local/lib/python2.7/site-packages/numpy/polynomial/tests/test_printing.py
/usr/local/lib/python2.7/site-packages/numpy/random/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/random/info.py
/usr/local/lib/python2.7/site-packages/numpy/random/mtrand.so
/usr/local/lib/python2.7/site-packages/numpy/random/randomkit.h
/usr/local/lib/python2.7/site-packages/numpy/random/setup.py
/usr/local/lib/python2.7/site-packages/numpy/random/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/random/tests/test_random.py
/usr/local/lib/python2.7/site-packages/numpy/random/tests/test_regression.py
/usr/local/lib/python2.7/site-packages/numpy/setup.py
/usr/local/lib/python2.7/site-packages/numpy/testing/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/decorators.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/noseclasses.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/nosetester.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/parameterized.py
/usr/local/lib/python2.7/site-packages/numpy/testing/_private/utils.py
/usr/local/lib/python2.7/site-packages/numpy/testing/decorators.py
/usr/local/lib/python2.7/site-packages/numpy/testing/noseclasses.py
/usr/local/lib/python2.7/site-packages/numpy/testing/nosetester.py
/usr/local/lib/python2.7/site-packages/numpy/testing/print_coercion_tables.py
/usr/local/lib/python2.7/site-packages/numpy/testing/setup.py
/usr/local/lib/python2.7/site-packages/numpy/testing/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/testing/tests/test_decorators.py
/usr/local/lib/python2.7/site-packages/numpy/testing/tests/test_doctesting.py
/usr/local/lib/python2.7/site-packages/numpy/testing/tests/test_utils.py
/usr/local/lib/python2.7/site-packages/numpy/testing/utils.py
/usr/local/lib/python2.7/site-packages/numpy/tests/__init__.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_ctypeslib.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_matlib.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_numpy_version.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_public_api.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_reloading.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_scripts.py
/usr/local/lib/python2.7/site-packages/numpy/tests/test_warnings.py
/usr/local/lib/python2.7/site-packages/numpy/version.py
==> Caveats
If you use system python (that comes - depending on the OS X version -
with older versions of numpy, scipy and matplotlib), you may need to
ensure that the brewed packages come earlier in Python's sys.path with:
  mkdir -p /Users/wenchen/Library/Python/2.7/lib/python/site-packages
  echo 'import sys; sys.path.insert(1, "/usr/local/lib/python3.7/site-packages")' >> /Users/wenchen/Library/Python/2.7/lib/python/site-packages/homebrew.pth
==> Summary
🍺  /usr/local/Cellar/numpy/1.16.1: 998 files, 26MB
==> Installing opencv dependency: tbb
==> Downloading https://homebrew.bintray.com/bottles/tbb-2019_U3_1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring tbb-2019_U3_1.sierra.bottle.tar.gz
🍺  /usr/local/Cellar/tbb/2019_U3_1: 134 files, 2.7MB
==> Installing opencv
==> Downloading https://homebrew.bintray.com/bottles/opencv-4.0.1.sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring opencv-4.0.1.sierra.bottle.tar.gz
Warning: opencv dependency gcc was built with a different C++ standard
library (libstdc++ from clang). This may cause problems at runtime.
🍺  /usr/local/Cellar/opencv/4.0.1: 679 files, 227.3MB
==> Caveats
==> libffi
libffi is keg-only, which means it was not symlinked into /usr/local,
because some formulae require a newer version of libffi.

For compilers to find libffi you may need to set:
  export LDFLAGS="-L/usr/local/opt/libffi/lib"

For pkg-config to find libffi you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/libffi/lib/pkgconfig"

==> icu4c
icu4c is keg-only, which means it was not symlinked into /usr/local,
because macOS provides libicucore.dylib (but nothing else).

If you need to have icu4c first in your PATH run:
  echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
  echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc

For compilers to find icu4c you may need to set:
  export LDFLAGS="-L/usr/local/opt/icu4c/lib"
  export CPPFLAGS="-I/usr/local/opt/icu4c/include"

For pkg-config to find icu4c you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"

==> tesseract
This formula containes only the "eng", "osd", and "snum" language data files.
If you need all the other supported languages, `brew install tesseract-lang`.
==> openblas
openblas is keg-only, which means it was not symlinked into /usr/local,
because macOS provides BLAS and LAPACK in the Accelerate framework.

For compilers to find openblas you may need to set:
  export LDFLAGS="-L/usr/local/opt/openblas/lib"
  export CPPFLAGS="-I/usr/local/opt/openblas/include"

For pkg-config to find openblas you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/openblas/lib/pkgconfig"

==> python
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages

See: https://docs.brew.sh/Homebrew-and-Python
==> numpy
If you use system python (that comes - depending on the OS X version -
with older versions of numpy, scipy and matplotlib), you may need to
ensure that the brewed packages come earlier in Python's sys.path with:
  mkdir -p /Users/wenchen/Library/Python/2.7/lib/python/site-packages
  echo 'import sys; sys.path.insert(1, "/usr/local/lib/python3.7/site-packages")' >> /Users/wenchen/Library/Python/2.7/lib/python/site-packages/homebrew.pth
