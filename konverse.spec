Summary:	a Jabber (an XML-based open source IM system) client for KDE
Summary(pl):	klient dla Jabbera (XML-owego systemu powiadamiania) pod KDE
Name:		konverse
Version:	0.2
Release:	1
Group:		Applications/Communications
Group(cs):	Aplikace/Komunikace
Group(da):	Programmer/Kommunikation
Group(de):	Applikationen/Kommunikation
Group(es):	Aplicaciones/Comunicaciones
Group(fr):	Applications/Transmissions
Group(is):	Forrit/Samskipti
Group(it):	Applicazioni/Comunicazioni
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/ƒÃøÆ
Group(no):	Applikasjoner/Kommunikasjon
Group(pl):	Aplikacje/Komunikacja
Group(pt):	AplicaÁıes/ComunicaÁıes
Group(ru):	“…Ãœ÷≈Œ…—/ÎœÕÕ’Œ…À¡√……
Group(sl):	Programi/Komunikacije
Group(sv):	Till‰mpningar/Kommunikation
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/ÎœÕ’Œ¶À¡√¶ß
License:	GPL
URL:		http://konverse.sourceforge.net/
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Konverse is a Jabber (http://www.jabber.org/) client for KDE. Jabber
is an Open-Source, XML-based instant messaging protocol. Features
include a buddy wizard, buddy search and buddy groups.


%prep
rm -fr $RPM_BUILD_ROOT
%setup -q
make -f Makefile.cvs


%build
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
