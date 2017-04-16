Name:           ros-jade-geographic-msgs
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS geographic_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/geographic_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-runtime
Requires:       ros-jade-std-msgs
Requires:       ros-jade-uuid-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-uuid-msgs

%description
ROS messages for Geographic Information Systems.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Apr 16 2017 Jack O'Quin <jack.oquin@gmail.com> - 0.5.2-0
- Autogenerated by Bloom

* Sat Apr 25 2015 Jack O'Quin <jack.oquin@gmail.com> - 0.4.0-0
- Autogenerated by Bloom

