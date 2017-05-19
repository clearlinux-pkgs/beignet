#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : beignet
Version  : 1
Release  : 31
URL      : https://cgit.freedesktop.org/beignet/snapshot/68c31b20e54a435975a9008ab93e760bc5cd193c.tar.gz
Source0  : https://cgit.freedesktop.org/beignet/snapshot/68c31b20e54a435975a9008ab93e760bc5cd193c.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: beignet-lib
Requires: beignet-data
BuildRequires : cmake
BuildRequires : cmrt-dev
BuildRequires : libdrm-dev
BuildRequires : llvm-dev
BuildRequires : llvm-lib
BuildRequires : ncurses-dev
BuildRequires : pciutils
BuildRequires : pkgconfig(OpenCL)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(x11)
BuildRequires : python3-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Beignet
=======
Beignet is an open source implementation of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs on
Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU. The code base also contains the compiler
part of the stack which is included in `backend/`. For more specific information

%package data
Summary: data components for the beignet package.
Group: Data

%description data
data components for the beignet package.


%package dev
Summary: dev components for the beignet package.
Group: Development
Requires: beignet-lib
Requires: beignet-data
Provides: beignet-devel

%description dev
dev components for the beignet package.


%package lib
Summary: lib components for the beignet package.
Group: Libraries
Requires: beignet-data

%description lib
lib components for the beignet package.


%prep
%setup -q -n 68c31b20e54a435975a9008ab93e760bc5cd193c

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495215023
mkdir clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir} -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DENABLE_OPENCL_20=ON -DCMAKE_BUILD_TYPE=RelWithDebInfo -DLLVM_INSTALL_DIR=/usr/bin
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1495215023
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/beignet/beignet.bc
/usr/lib64/beignet/beignet.pch
/usr/lib64/beignet/beignet_20.bc
/usr/lib64/beignet/beignet_20.pch

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/com.intel.beignet.metainfo.xml

%files dev
%defattr(-,root,root,-)
/usr/include/CL/cl.h
/usr/include/CL/cl_d3d10.h
/usr/include/CL/cl_d3d11.h
/usr/include/CL/cl_dx9_media_sharing.h
/usr/include/CL/cl_egl.h
/usr/include/CL/cl_ext.h
/usr/include/CL/cl_gl.h
/usr/include/CL/cl_gl_ext.h
/usr/include/CL/cl_intel.h
/usr/include/CL/cl_platform.h
/usr/include/CL/opencl.h
/usr/lib64/beignet/include/ocl.h
/usr/lib64/beignet/include/ocl_as.h
/usr/lib64/beignet/include/ocl_async.h
/usr/lib64/beignet/include/ocl_atom.h
/usr/lib64/beignet/include/ocl_atom_20.h
/usr/lib64/beignet/include/ocl_common.h
/usr/lib64/beignet/include/ocl_convert.h
/usr/lib64/beignet/include/ocl_defines.h
/usr/lib64/beignet/include/ocl_enqueue.h
/usr/lib64/beignet/include/ocl_float.h
/usr/lib64/beignet/include/ocl_geometric.h
/usr/lib64/beignet/include/ocl_image.h
/usr/lib64/beignet/include/ocl_integer.h
/usr/lib64/beignet/include/ocl_math.h
/usr/lib64/beignet/include/ocl_math_20.h
/usr/lib64/beignet/include/ocl_math_common.h
/usr/lib64/beignet/include/ocl_memcpy.h
/usr/lib64/beignet/include/ocl_memset.h
/usr/lib64/beignet/include/ocl_misc.h
/usr/lib64/beignet/include/ocl_pipe.h
/usr/lib64/beignet/include/ocl_printf.h
/usr/lib64/beignet/include/ocl_relational.h
/usr/lib64/beignet/include/ocl_simd.h
/usr/lib64/beignet/include/ocl_sync.h
/usr/lib64/beignet/include/ocl_types.h
/usr/lib64/beignet/include/ocl_vload.h
/usr/lib64/beignet/include/ocl_vload_20.h
/usr/lib64/beignet/include/ocl_work_group.h
/usr/lib64/beignet/include/ocl_workitem.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/beignet/libcl.so
/usr/lib64/beignet/libgbe.so
/usr/lib64/beignet/libgbeinterp.so
