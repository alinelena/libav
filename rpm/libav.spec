Name:           libav1
Version:        10.2
Release:        0.0
Summary:        Open source audio and video processing tools
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://libav.org
Source:         %{name}-%{version}.tar.gz
License:        LGPL-2.0+

%description
Libav is a complete, cross-platform solution to record, convert and stream audio and video. It includes libavcodec - the leading audio/video codec library.

%package devel
Summary:        Libav Devel package
Group:          Productivity/Multimedia
Requires:       %{name} = %{version}
Requires:       bzip2-devel

%description devel
Libav is a complete, cross-platform solution to record, convert and stream audio and video.

%package tools
Summary:        Libav tools package
Group:          Productivity/Multimedia
Requires:       %{name} = %{version}

%description tools
Libav is a complete, cross-platform solution to record, convert and stream audio and video.

%prep
%setup -q -n %{name}-%{version}/libav

./configure --prefix=/usr \
    --disable-avserver \
    --disable-avplay \
    --disable-avconv \
    --enable-pic \
    --disable-encoder=flac \
    --disable-decoder=cavs \
    --disable-devices \
    --disable-network \
    --disable-hwaccels \
    --disable-dxva2 \
    --disable-vdpau \
    --disable-filters \
    --disable-doc \
    --enable-gpl \
    --enable-sram \
    --enable-shared \
    --disable-static \
    --disable-yasm

%build
make %{?jobs:-j%jobs}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/avconv/*.avpreset
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/libavcodec/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h
%{_includedir}/libavdevice/*.h
%{_includedir}/libavresample/*.h
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/avprobe
