Name:		konverse
Version:	0.2
Release:	1
Summary:	a Jabber (an XML-based open source IM system) client for KDE
Group:		Applications/Internet
License:	GPL
Packager:	Slavek Banko <slavek.banko@axis.cz>
URL:		http://konverse.sourceforge.net/
Source:		%{name}-%{version}.tgz
Prefix:		/usr
BuildRoot:	/var/tmp/%{name}-%{version}


%description
Konverse is a Jabber (http://www.jabber.org/) client for KDE.
Jabber is an Open-Source, XML-based instant messaging protocol.
Features include a buddy wizard, buddy search and buddy groups.


%prep
rm -fr $RPM_BUILD_ROOT
%setup
make -f Makefile.cvs


%build
./configure
make


%install
make prefix=$RPM_BUILD_ROOT%{prefix} install


%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/bin/konverse
/usr/share/applnk/Internet/konverse.desktop
/usr/share/apps/konverse/icons/hicolor/16x16/actions/add_user.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/connect.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/chat_dlg.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/konverse_message.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/new_message.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/useradd_dlg.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_away.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_dnd.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_chat.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_offline.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_online.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_unknown.png
/usr/share/apps/konverse/icons/hicolor/16x16/actions/user_xaway.png
/usr/share/apps/konverse/icons/hicolor/16x16/apps/konverse.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_away.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_dnd.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_chat.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_offline.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_online.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/konverse_xaway.png
/usr/share/apps/konverse/icons/hicolor/22x22/actions/vcard.png
/usr/share/apps/konverse/icons/hicolor/22x22/apps/konverse.png
/usr/share/apps/konverse/pics/konverse-large.png
/usr/share/icons/locolor/16x16/apps/konverse.png
/usr/share/icons/locolor/22x22/apps/konverse.png


%changelog
* Sun May 27 2001 Slavek Banko <slavek.banko@axis.cz>
- moved to version 0.2

* Wed May 24 2001 Slavek Banko <slavek.banko@axis.cz>
- moved to current CVS version (0.2pre)

* Wed May 23 2001 Slavek Banko <slavek.banko@axis.cz>
- prepared spec file for RPM
