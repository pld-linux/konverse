Summary:	A Jabber (an XML-based open source IM system) client for KDE
Summary(pl):	Klient dla Jabbera (XML-owego systemu powiadamiania) pod KDE
Name:		konverse
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	%{name}-%{version}.tgz
# Source0-md5:	a0ce55498d60f87805705af059d43cc8
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/konverse/%{name}-%{version}.tar.gz
URL:		http://konverse.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konverse is a Jabber (http://www.jabber.org/) client for KDE. Jabber
is an Open-Source, XML-based instant messaging protocol. Features
include a buddy wizard, buddy search and buddy groups.

%description -l pl
Konverse to klient Jabbera (http://www.jabber.org/) dla KDE. Jabber
jest otwartym protoko³em komunikowania bazuj±cym na XML.

%prep
%setup -q

%build
%{__make} -f Makefile.cvs
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konverse
%{_applnkdir}/Internet/konverse.desktop
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/add_user.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/connect.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/chat_dlg.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/konverse_message.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/new_message.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/useradd_dlg.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_away.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_dnd.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_chat.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_offline.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_online.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_unknown.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/actions/user_xaway.png
%{_datadir}/apps/konverse/icons/hicolor/16x16/apps/konverse.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_away.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_dnd.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_chat.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_offline.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_online.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/konverse_xaway.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/actions/vcard.png
%{_datadir}/apps/konverse/icons/hicolor/22x22/apps/konverse.png
%{_datadir}/apps/konverse/pics/konverse-large.png
%{_datadir}/icons/locolor/16x16/apps/konverse.png
%{_datadir}/icons/locolor/22x22/apps/konverse.png
