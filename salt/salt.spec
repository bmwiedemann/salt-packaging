#
# spec file for package salt
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} > 1210 || 0%{?rhel} >= 7 || 0%{?fedora}
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%if 0%{?suse_version} > 1110
%bcond_without bash_completion
%bcond_without fish_completion
%bcond_without zsh_completion
%else
%bcond_with    bash_completion
%bcond_with    fish_completion
%bcond_with    zsh_completion
%endif
%bcond_with    test
%bcond_without docs
%bcond_with    builddocs

Name:           salt
Version:        2016.11.4
Release:        0
Summary:        A parallel remote execution system
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
# Git: https://github.com/openSUSE/salt.git
Source0:        https://pypi.python.org/packages/88/3c/77de1e461882708a5a247bbc22f5b3df8a34affe69755ea9540473c9852a/salt-2016.11.4.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml

# PATCH-FIX-OPENSUSE use-forking-daemon.patch tserong@suse.com -- We don't have python-systemd, so notify can't work
# We do not upstream this patch because this is something that we have to fix on our side
Patch1:         tserong-suse.com-we-don-t-have-python-systemd-so-not.patch
# PATCH-FIX-OPENSUSE use-salt-user-for-master.patch -- Run salt master as dedicated salt user
# We do not upstream this patch because this is suse custom configuration
# (see: https://trello.com/c/wh96lCD4/1528-get-rid-of-0003-check-if-byte-strings-are-properly-encoded-in-utf-8-patch-in-the-salt-package)
Patch2:         run-salt-master-as-dedicated-salt-user.patch
# PATCH-FIX-OPENSUSE https://github.com/saltstack/salt/pull/30424
# We do not upstream this patch because it has been fixed upstream
Patch3:         check-if-byte-strings-are-properly-encoded-in-utf-8.patch
# PATCH-FIX-OPENSUSE prevent rebuilds in OBS
# We do not upstream this patch because the issue is on our side
Patch4:         do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
# PATCH-FIX-OPENSUSE Generate events from the Salt minion,
# We do not upstream this because this is for SUSE only (15.08.2016) if Zypper has been used outside the Salt infrastructure
Patch5:         add-zypp-notify-plugin.patch
# PATCH-FIX_OPENSUSE
Patch6:         run-salt-api-as-user-salt-bsc-990029.patch
# PATCH-FIX_OPENSUSE
Patch7:         change-travis-configuration-file-to-use-salt-toaster.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/37856 (pending to include in 2016.11)
Patch8:         setting-up-os-grains-for-sles-expanded-support-suse-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/34165
Patch9:         fix-salt-summary-to-count-not-responding-minions-cor.patch
# PATCH-FIX_OPENSUSE
Patch10:        avoid-failures-on-sles-12-sp2-because-of-new-systemd.patch
# PATCH-FIX_OPENSUSE
Patch11:        add-yum-plugin.patch
# PATCH-FIX_OPENSUSE
Patch12:        add-ssh-option-to-salt-ssh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38806
Patch13:        add-a-salt-minion-service-control-file.patch
# Description N/A
Patch14:        add-options-for-dockerng.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/39762
Patch15:        fix-regression-in-file.get_managed-add-unit-tests.patch
# PATCH-FIX_OPENSUSE
Patch16:        translate-variable-arguments-if-they-contain-hidden-.patch
# PATCH-FIX_OPENSUSE
Patch17:        special-salt-minion.service-file-for-rhel7.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40266
Patch18:        adding-support-for-installing-patches-in-yum-dnf-exe.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40761
Patch19:        search-the-entire-cache_dir-because-storage-paths-ch.patch
# PATCH-FIX_OPENSUSE
Patch20:        fixing-beacons.list-integration-test-failure.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40817
Patch21:        add-unit-test-for-skip-false-values-from-preferred_i.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40852
Patch22:        use-correct-grain-constants-for-timezone.patch
# PATCH-FIX_OPENSUSE (upstream coming soon)
Patch23:        fix-grain-for-os_family-on-suse-series.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41269
Patch24:        bugfix-unable-to-use-127-as-hostname.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41336
Patch25:        fix-setting-language-on-suse-systems.patch
Patch26:        fix-os_family-case-in-unittest.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41235
Patch27:        rest_cherrypy-remove-sleep-call.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40905
Patch28:        fixed-issue-with-parsing-of-master-minion-returns-wh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41533
Patch29:        clean-up-change-attribute-from-interface-dict.patch
# PATCH-FIX_OPENSUSE
Patch30:        fix-format-error-bsc-1043111.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch31:        adding-salt-minion-watchdog-for-sysv-systems-rhel6-a.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch32:        enables-salt-minion-watchdog-on-init.d-script-for-sy.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42339
Patch33:        bugfix-jobs-scheduled-to-run-at-a-future-time-stay-p.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42944
Patch34:        add-clean_id-function-to-salt.utils.verify.py.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42986
Patch35:        notify-systemd-synchronously-bsc-1053376.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/37
Patch36:        revert-we-don-t-have-python-systemd-so-notify-can-t-.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1051948
Patch37:        introducing-the-kubernetes-module.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1052264
Patch38:        list_pkgs-add-parameter-for-returned-attribute-selec.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43441
Patch39:        use-home-to-get-the-user-home-directory-instead-usin.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43366
#                    https://github.com/saltstack/salt/pull/43646/
Patch40:        catching-error-when-pidfile-cannot-be-deleted.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43235
#                    https://github.com/saltstack/salt/pull/43724/
Patch41:        fix-for-delete_deployment-in-kubernetes-module.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43663
Patch42:        multiprocessing-minion-option-documentation-fixes.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43669
Patch43:        introduce-process_count_max-minion-configuration-par.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/0976f8f7131975a1ae29b2724069a301a870a46d
#                    Missed follow-up commit
Patch44:        escape-the-os.sep.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44005
Patch45:        bugfix-always-return-a-string-list-on-unknown-job-ta.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44011
Patch46:        security-fixes-cve-2017-14695-and-cve-2017-14696.patch
# PATCH-FIX_OPENSUSE bsc#1060230
Patch47:        activate-all-beacons-sources-config-pillar-grains.patch
# PATCH-FIX_OPENSUSE bsc#1041993
Patch48:        removes-beacon-configuration-deprecation-warning-48.patch
# PATCH-FIX_OPENSUSE bsc#1068446
Patch49:        bugfix-the-logic-according-to-the-exact-described-pu.patch
# PATCH-FIX_OPENSUSE
Patch50:        avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
# PATCH-FIX_OPENSUSE bsc#1071322
Patch51:        older-logrotate-need-su-directive.patch
# PATCH-FIX_OPENSUSE bsc#1065792
Patch52:        fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45060
Patch53:        feat-add-grain-for-all-fqdns.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44991
Patch54:        split-only-strings-if-they-are-such.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40894
Patch55:        fix-for-broken-jobs-jid-in-2016.11.4.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45365
Patch56:        return-error-when-gid_from_name-and-group-does-not-e.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38675
Patch57:        setvcpus-setmem-fix-return-value-parsing-issue-when-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41795
Patch58:        bugfix-use-utc-date.patch
# PATCH-FIX_OPENSUSE
Patch59:        allow-running-tests-on-python-2.6-systems.patch
# PATCH-FIX_OPENSUSE bsc#1068566
Patch60:        yumpkg-don-t-use-diff_attr-when-determining-install-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43039
Patch61:        catch-importerror-for-kubernetes.client-import.patch
# PATCH-FIX_OPENSUSE bsc#1074227
Patch62:        fix-state-files-with-unicode-bsc-1074227.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46104
Patch63:        suppress-missing-fields-typeerror-exception-by-m2cry.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46104
Patch64:        fix-x509-unit-test-to-run-on-2016.11.4-version.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46413
Patch65:        explore-module.run-response-to-catch-the-result-in-d.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46575
Patch66:        fix-decrease-loglevel-when-unable-to-resolve-addr.patch
# PATCH-FIX_OPENSUSE bsc#1079398
Patch67:        revert-fix-augeas-module-so-shlex-doesn-t-strip-quot.patch
# PATCH-FIX_OPENSUSE bsc#1085635
Patch68:        make-module-result-usable-in-states-module.run-bsc-1.patch
# PATCH-FIX_OPENSUSE bsc#1088423
Patch69:        disable-cron-logging-only-on-sles11-systems-not-on-r.patch
# PATCH-FIX_OPENSUSE bsc#1090271
Patch70:        add-rsyslog-rule-to-avoid-salt-minion-watcher-cron-l.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46635
Patch71:        fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41786
Patch72:        fix-regressions-from-not-calling-load_args_and_kwarg.patch
# PATCH-FIX_OPENSUSE bsc#1087342
Patch73:        backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch74:        strip-trailing-commas-on-linux-user-gecos-fields.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47270
Patch75:        initialize-__context__-retcode-for-functions-handled.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47232
Patch76:        fixed-usage-of-ipaddress.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42798
Patch77:        update-return-data-before-calling-returners.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47211
Patch78:        fix-for-ec2-rate-limit-failures.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47471
Patch79:        do-not-override-jid-on-returners-only-sending-back-t.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47638
Patch80:        add-all_versions-parameter-to-include-all-installed-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47765
Patch81:        prevent-zypper-from-parsing-repo-configuration-from-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch82:        add-other-attribute-to-gecos-fields-to-avoid-inconsi.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch83:        add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42541
Patch84:        bugfix-state-file.line-warning-bsc-1093458-86.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43955
Patch85:        enable-with-salt-version-parameter-for-setup.py-scri.patch
# PATCH-FIX_OPENSUSE
Patch86:        add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_OPENSUSE bsc#1098394 backport of https://github.com/saltstack/salt/pull/47061
Patch87:        porting-fix-diffing-binary-files-in-file.get_diff-bs.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47405
Patch88:        fix-unboundlocalerror-in-file.get_diff.patch


BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
BuildRequires:  python
BuildRequires:  python-devel
# requirements/base.txt
%if 0%{?rhel}
BuildRequires:  python-jinja2
%else
BuildRequires:  python-Jinja2
%endif
BuildRequires:  python-futures >= 2.0
BuildRequires:  python-markupsafe
BuildRequires:  python-msgpack-python > 0.3
BuildRequires:  python-psutil
BuildRequires:  python-requests >= 1.0.0
BuildRequires:  python-tornado >= 4.2.1
BuildRequires:  python-yaml

# requirements/zeromq.txt
BuildRequires:  python-pycrypto >= 2.6.1
BuildRequires:  python-pyzmq >= 2.2.0
%if %{with test}
# requirements/dev_python27.txt
BuildRequires:  python-boto >= 2.32.1
BuildRequires:  python-mock
BuildRequires:  python-moto >= 0.3.6
BuildRequires:  python-pip
BuildRequires:  python-salt-testing >= 2015.2.16
BuildRequires:  python-unittest2
BuildRequires:  python-xml
%endif
%if %{with builddocs}
BuildRequires:  python-sphinx
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
%endif

%if 0%{?suse_version}
Requires(pre):  dbus-1
%else
Requires(pre):  dbus
%endif

Requires:       procps
Requires:       logrotate
Requires:       python
#
%if ! 0%{?suse_version} > 1110
Requires:       python-certifi
%endif
# requirements/base.txt
%if 0%{?rhel}
Requires:  python-jinja2
Requires:  yum
%if 0%{?rhel} == 6
Requires:  yum-plugin-security
Requires:  rsyslog
%endif
%else
Requires:  python-Jinja2
%endif
Requires:       python-futures >= 2.0
Requires:       python-markupsafe
Requires:       python-msgpack-python > 0.3
Requires:       python-psutil
Requires:       python-requests >= 1.0.0
Requires:       python-tornado >= 4.2.1
Requires:       python-yaml
%if 0%{?suse_version}
# required for zypper.py
Requires:       rpm-python
Requires(pre):  libzypp(plugin:system) >= 0
Requires:       zypp-plugin-python
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python-timelib
Suggests:       python-gnupg
# requirements/zeromq.txt
%endif
Requires:       python-pycrypto >= 2.6.1
Requires:       python-pyzmq >= 2.2.0
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python-xml
Suggests:       python-Mako
Recommends:     python-netaddr
%endif

%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre): %insserv_prereq
%endif
%endif

%if %{with fish_completion}
%define fish_dir %{_datadir}/fish/
%define fish_completions_dir %{_datadir}/fish/completions/
%endif

%if %{with bash_completion}
%if 0%{?suse_version} >= 1140
BuildRequires:  bash-completion
%else
BuildRequires:  bash
%endif
%endif

%if %{with zsh_completion}
BuildRequires:  zsh
%endif

%if 0%{?rhel}
BuildRequires:  yum
%endif

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.

%package api
Summary:        The api for Salt a parallel remote execution system
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Requires:       python-CherryPy >= 3.2.2

%description api
salt-api is a modular interface on top of Salt that can provide a variety of entry points into a running Salt system.

%package cloud
Summary:        Generic cloud provisioning tool for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Requires:       python-apache-libcloud
%if 0%{?suse_version}
Recommends:     python-botocore
Recommends:     python-netaddr
%endif

%description cloud
public cloud VM management system
provision virtual machines on various public clouds via a cleanly
controlled profile and mapping system.

%if %{with docs}
%package doc
Summary:        Documentation for salt, a parallel remote execution system
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This contains the documentation of salt, it is an offline version of http://docs.saltstack.com.
%endif

%package master
Summary:        The management component of Saltstack with zmq protocol supported
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version}
Recommends:     python-pygit2 >= 0.20.3
%endif
%ifarch %{ix86} x86_64
%if 0%{?suse_version}
%if 0%{?suse_version} > 1110
Requires:       dmidecode
%else
Requires:       pmtools
%endif
%endif
%endif
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description master
The Salt master is the central server to which all minions connect.
Enabled commands to remote systems to be called in parallel rather
than serially.

%package minion
Summary:        The client component for Saltstack
Group:          System/Management
Requires(pre):  %{name} = %{version}-%{release}

%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description minion
Salt minion is queried and controlled from the master.
Listens to the salt master and execute the commands.

%package proxy
Summary:        Component for salt that enables controlling arbitrary devices
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description proxy
Proxy minions are a developing Salt feature that enables controlling devices that,
for whatever reason, cannot run a standard salt-minion.
Examples include network gear that has an API but runs a proprietary OS,
devices with limited CPU or memory, or devices that could run a minion, but for
security reasons, will not.


%package syndic
Summary:        The syndic component for saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description syndic
Salt syndic is the master-of-masters for salt
The master of masters for salt-- it enables
the management of multiple masters at a time..

%package ssh
Summary:        Management component for Saltstack with ssh protocol
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
Recommends:     sshpass
%endif
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description ssh
Salt ssh is a master running without zmq.
it enables the management of minions over a ssh connection.

%if %{with bash_completion}
%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description bash-completion
Bash command line completion support for %{name}.

%endif

%if %{with fish_completion}
%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description fish-completion
Fish command line completion support for %{name}.
%endif

%if %{with zsh_completion}
%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description zsh-completion
Zsh command line completion support for %{name}.

%endif

%prep
%setup -q -n salt-%{version}
cp %{S:1} .
cp %{S:5} ./.travis.yml
%patch1 -p1

# Do not apply this patch on RHEL 6
%if 0%{?rhel} > 6 || 0%{?suse_version}
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1

# This is SUSE-only patch
%if 0%{?suse_version}
%patch5 -p1
%endif

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%patch31 -p1
%patch32 -p1
%patch50 -p1
%endif 
%if 0%{?rhel} == 6
%patch69 -p1
%patch70 -p1
%endif 
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1

%build
%{__python} setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt

%if %{with docs} && %{without builddocs}
# extract docs from the tarball
mkdir -p doc/_build
pushd doc/_build/
tar xfv %{S:3}
popd
%endif

%if %{with docs} && %{with builddocs}
## documentation
cd doc && make html && rm _build/html/.buildinfo && rm _build/html/_images/proxy_minions.png && cd _build/html && chmod -R -x+X *
%endif

%install
%{__python} setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot}
## create missing directories
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d/
install -Dd -m 0755 %{buildroot}%{_sbindir}
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/minion/extmod
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/jobs
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/proc
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/queues
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/roots
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/syndics
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/tokens
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/cloud
install -Dd -m 0750 %{buildroot}/var/lib/salt
install -Dd -m 0750 %{buildroot}/srv/salt
install -Dd -m 0750 %{buildroot}/srv/pillar
install -Dd -m 0750 %{buildroot}/srv/spm
install -Dd -m 0755 %{buildroot}%{_docdir}/salt
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_autosign
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_denied
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_pre
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_rejected
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/minion

## Install Zypper plugins only on SUSE machines
%if 0%{?suse_version}
install -Dd -m 0750 %{buildroot}%{_prefix}/lib/zypp/plugins/commit
%{__install} scripts/zypper/plugins/commit/zyppnotify %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
install -Dd %{buildroot}%{_prefix}/share/yum-plugins
install -Dd %{buildroot}/etc/yum/pluginconf.d
%{__install} scripts/yum/plugins/yumnotify.py %{buildroot}%{_prefix}/share/yum-plugins
%{__install} scripts/yum/plugins/yumnotify.conf %{buildroot}/etc/yum/pluginconf.d
%endif

## install init and systemd scripts
%if %{with systemd}
install -Dpm 0644 pkg/salt-master.service %{buildroot}%{_unitdir}/salt-master.service
%if 0%{?suse_version}
install -Dpm 0644 pkg/suse/salt-minion.service %{buildroot}%{_unitdir}/salt-minion.service
%else
install -Dpm 0644 pkg/salt-minion.service.rhel7 %{buildroot}%{_unitdir}/salt-minion.service
%endif
install -Dpm 0644 pkg/salt-syndic.service %{buildroot}%{_unitdir}/salt-syndic.service
install -Dpm 0644 pkg/suse/salt-api.service    %{buildroot}%{_unitdir}/salt-api.service
install -Dpm 0644 pkg/salt-proxy@.service %{buildroot}%{_unitdir}/salt-proxy@.service
ln -s service %{buildroot}%{_sbindir}/rcsalt-master
ln -s service %{buildroot}%{_sbindir}/rcsalt-syndic
ln -s service %{buildroot}%{_sbindir}/rcsalt-minion
ln -s service %{buildroot}%{_sbindir}/rcsalt-api
install -Dpm 644 %{S:2}                   %{buildroot}/usr/lib/tmpfiles.d/salt.conf
%else
mkdir -p %{buildroot}%{_initddir}
## install init scripts
install -Dpm 0755 pkg/suse/salt-master %{buildroot}%{_initddir}/salt-master
install -Dpm 0755 pkg/suse/salt-syndic %{buildroot}%{_initddir}/salt-syndic
install -Dpm 0755 pkg/suse/salt-minion %{buildroot}%{_initddir}/salt-minion
install -Dpm 0755 pkg/suse/salt-api %{buildroot}%{_initddir}/salt-api
ln -sf %{_initddir}/salt-master %{buildroot}%{_sbindir}/rcsalt-master
ln -sf %{_initddir}/salt-syndic %{buildroot}%{_sbindir}/rcsalt-syndic
ln -sf %{_initddir}/salt-minion %{buildroot}%{_sbindir}/rcsalt-minion
ln -sf %{_initddir}/salt-api %{buildroot}%{_sbindir}/rcsalt-api
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
install -Dpm 0755 scripts/watchdog/salt-daemon-watcher %{buildroot}%{_bindir}/salt-daemon-watcher
%if 0%{?rhel} == 6
install -Dpm 0640 pkg/suse/rsyslog-cron-salt-watcher.conf %{buildroot}%{_sysconfdir}/rsyslog.d/rsyslog-cron-salt-watcher.conf
%endif 
%endif 

#
## install config files
install -Dpm 0640 conf/minion %{buildroot}%{_sysconfdir}/salt/minion
install -Dpm 0640 /dev/null   %{buildroot}%{_sysconfdir}/salt/minion_id
install -Dpm 0640 conf/master %{buildroot}%{_sysconfdir}/salt/master
install -Dpm 0640 conf/roster %{buildroot}%{_sysconfdir}/salt/roster
install -Dpm 0640 conf/cloud %{buildroot}%{_sysconfdir}/salt/cloud
install -Dpm 0640 conf/cloud.profiles %{buildroot}%{_sysconfdir}/salt/cloud.profiles
install -Dpm 0640 conf/cloud.providers %{buildroot}%{_sysconfdir}/salt/cloud.providers
#
## install logrotate file
install -Dpm 0644  pkg/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
#
## install SuSEfirewall2 rules
install -Dpm 0644  pkg/suse/salt.SuSEfirewall2 %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
#
## install completion scripts
%if %{with bash_completion}
install -Dpm 0644 pkg/salt.bash %{buildroot}%{_sysconfdir}/bash_completion.d/salt
%endif
%if %{with zsh_completion}
install -Dpm 0644 pkg/zsh_completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/salt
%endif

%if %{with fish_completion}
mkdir -p %{buildroot}%{fish_completions_dir}
install -Dpm 0644 pkg/fish-completions/* %{buildroot}%{fish_completions_dir}
%endif

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_docdir}
%fdupes %{buildroot}%{python_sitelib}
%endif

%check
%if %{with test}
python setup.py test --runtests-opts=-u
%endif

%pre
S_HOME="/var/lib/salt"
S_PHOME="/srv/salt"
getent passwd salt | grep $S_PHOME >/dev/null && usermod -d $S_HOME salt
getent group salt >/dev/null || %{_sbindir}/groupadd -r salt
getent passwd salt >/dev/null || %{_sbindir}/useradd -r -g salt -d $S_HOME -s /bin/false -c "salt-master daemon" salt
if [[ -d "$S_PHOME/.ssh" ]]; then
    mv $S_PHOME/.ssh $S_HOME
fi

%post
%if %{with systemd}
systemd-tmpfiles --create /usr/lib/tmpfiles.d/salt.conf || true
%else
dbus-uuidgen --ensure
%endif

%preun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-proxy@.service
%else
%systemd_preun salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-proxy
%endif
%endif

%pre proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-proxy@.service
%endif
%endif

%post proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-proxy@.service
%fillup_only
%else
%systemd_post salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-proxy@.service
%else
%systemd_postun_with_restart salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-proxy
%endif
%endif

%preun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-syndic.service
%else
%systemd_preun salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-syndic
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-syndic stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-syndic
  fi
%endif
%endif

%pre syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-syndic.service
%endif
%endif

%post syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-syndic.service
%fillup_only
%else
%systemd_post salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-syndic.service
%else
%systemd_postun_with_restart salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-syndic
%endif
%endif

%preun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-master.service
%else
%systemd_preun salt-master.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-master
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-master stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-master
  fi
%endif
%endif

%pre master
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-master.service
%endif
%endif

%post master
if [ $1 -eq 2 ] ; then
  # Upgrading from an earlier version.  If this is from 2014, where daemons
  # ran as root, we need to chown some stuff to salt in order for the new
  # version to actually work.  It seems a manual restart of salt-master may
  # still be required, but at least this will actually work given the file
  # ownership is correct.
  for file in master.{pem,pub} ; do
    [ -f /etc/salt/pki/master/$file ] && chown salt /etc/salt/pki/master/$file
  done
  MASTER_CACHE_DIR="/var/cache/salt/master"
  [ -d $MASTER_CACHE_DIR ] && chown -R salt:salt $MASTER_CACHE_DIR
  [ -f $MASTER_CACHE_DIR/.root_key ] && chown root:root $MASTER_CACHE_DIR/.root_key
  true
fi
%if %{with systemd}
if [ `rpm -q systemd --queryformat="%{VERSION}"` -lt 228 ]; then
  # On systemd < 228 the 'TasksTask' attribute is not available.
  # Removing TasksMax from salt-master.service on SLE12SP1 LTSS (bsc#985112)
  sed -i '/TasksMax=infinity/d' %{_unitdir}/salt-master.service
fi
%if 0%{?suse_version}
%service_add_post salt-master.service
%fillup_only
%else
%systemd_post salt-master.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-master
%endif
%endif

%postun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-master.service
%else
%systemd_postun_with_restart salt-master.service
%endif
%else
%if 0%{?suse_version}
%restart_on_update salt-master
%insserv_cleanup
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-master condrestart >/dev/null 2>&1 || :
  fi
%endif
%endif

%preun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-minion.service
%else
%systemd_preun salt-minion.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-minion
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-minion stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-minion
  fi
%endif
%endif

%pre minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-minion.service
%endif
%endif

%post minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-minion.service
%fillup_only
%else
%systemd_post salt-minion.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-minion
  /sbin/service rsyslog condrestart >/dev/null 2>&1 || :
%endif
%endif

%postun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-minion.service
%else
%systemd_postun_with_restart salt-minion.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-minion
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-minion condrestart >/dev/null 2>&1 || :
      /sbin/service rsyslog condrestart >/dev/null 2>&1 || :
  fi
%endif
%endif

%preun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-api.service
%else
%systemd_preun salt-api.service
%endif
%else
%stop_on_removal
%endif

%pre api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-api.service
%endif
%endif

%post api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-api.service
%else
%systemd_post salt-api.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-api.service
%else
%systemd_postun_with_restart salt-api.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update
%endif
%endif

%files api
%defattr(-,root,root)
%{_bindir}/salt-api
%{_sbindir}/rcsalt-api
%if %{with systemd}
%{_unitdir}/salt-api.service
%else
%{_initddir}/salt-api
%endif
%{_mandir}/man1/salt-api.1.*

%files cloud
%defattr(-,root,root)
%{_bindir}/salt-cloud
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.maps.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.profiles.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.providers.d
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.profiles
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.providers
%dir               %attr(0750, root, salt) %{_localstatedir}/cache/salt/cloud
%{python_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%attr(755,root,root)%{python_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%{_mandir}/man1/salt-cloud.1.*

%files ssh
%defattr(-,root,root)
%{_bindir}/salt-ssh
%{_mandir}/man1/salt-ssh.1.gz

%files syndic
%defattr(-,root,root)
%{_bindir}/salt-syndic
%{_mandir}/man1/salt-syndic.1.gz
%{_sbindir}/rcsalt-syndic
%if %{with systemd}
%{_unitdir}/salt-syndic.service
%else
%{_initddir}/salt-syndic
%endif

%files minion
%defattr(-,root,root)
%{_bindir}/salt-minion
%{_mandir}/man1/salt-minion.1.gz
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/salt/minion
%config(noreplace) %attr(0640, root, root) %ghost %{_sysconfdir}/salt/minion_id
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/minion.d/
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/pki/minion/
%dir               %attr(0750, root, root) %{_localstatedir}/cache/salt/minion/
#%dir %ghost        %attr(0750, root, salt) %{_localstatedir}/run/salt/minion
%{_sbindir}/rcsalt-minion

# Install plugin only on SUSE machines
%if 0%{?suse_version}
%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
%{_prefix}/share/yum-plugins/
/etc/yum/pluginconf.d/yumnotify.conf
%endif

%if %{with systemd}
%{_unitdir}/salt-minion.service
%else
%config(noreplace) %{_initddir}/salt-minion
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%{_bindir}/salt-daemon-watcher
%if 0%{?rhel} == 6 
%{_sysconfdir}/rsyslog.d/rsyslog-cron-salt-watcher.conf
%endif
%endif

%files proxy
%defattr(-,root,root)
%{_bindir}/salt-proxy
%{_mandir}/man1/salt-proxy.1.gz
%if %{with systemd}
%{_unitdir}/salt-proxy@.service
%endif

%files master
%defattr(-,root,root)
%{_bindir}/salt
%{_bindir}/salt-master
%{_bindir}/salt-cp
%{_bindir}/salt-key
%{_bindir}/salt-run
%{_mandir}/man1/salt-master.1.gz
%{_mandir}/man1/salt-cp.1.gz
%{_mandir}/man1/salt-key.1.gz
%{_mandir}/man1/salt-run.1.gz
%{_mandir}/man7/salt.7.gz
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
%{_sbindir}/rcsalt-master
%if %{with systemd}
%{_unitdir}/salt-master.service
%else
%config(noreplace) %{_initddir}/salt-master
%endif
#
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/master
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/roster
%dir               %attr(0755, root, salt) %{_sysconfdir}/salt/master.d/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_autosign/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_denied/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_pre/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_rejected/
%dir               %attr(0755, salt, salt) /var/lib/salt
%dir               %attr(0755, root, salt) /srv/salt
%dir               %attr(0755, root, salt) /srv/pillar
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/jobs/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/proc/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/queues/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/roots/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/syndics/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/tokens/
#%dir %ghost        %attr(0750, salt, salt) %{_localstatedir}/run/salt/master/

%files
%defattr(-,root,root,-)
%{_bindir}/spm
%{_bindir}/salt-call
%{_bindir}/salt-unity
%{_mandir}/man1/salt-unity.1.gz
%{_mandir}/man1/salt-call.1.gz
%{_mandir}/man1/spm.1.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
%{python_sitelib}/*
%exclude %{python_sitelib}/salt/cloud/deploy/*.sh
%attr(755,root,root)%{python_sitelib}/salt/cloud/deploy/*.sh
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE
#
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt/pki
%dir        %attr(0750, salt, salt) %{_localstatedir}/log/salt
%dir        %attr(0750, root, salt) %{_localstatedir}/cache/salt
#%dir %ghost %attr(0750, root, salt) %{_localstatedir}/run/salt
%dir        %attr(0750, root, salt) /srv/spm
%if %{with systemd}
/usr/lib/tmpfiles.d/salt.conf
%endif
%{_mandir}/man1/salt.1.*

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%if %{with bash_completion}
%files bash-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/bash_completion.d/
%config %{_sysconfdir}/bash_completion.d/%{name}
%endif

%if %{with zsh_completion}
%files zsh-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/zsh_completion.d/
%config %{_sysconfdir}/zsh_completion.d/%{name}
%endif

%if %{with fish_completion}
%files fish-completion
%defattr(-,root,root)
%{fish_completions_dir}/salt*
%dir %{fish_completions_dir}
%dir %{fish_dir}
%endif

%changelog
