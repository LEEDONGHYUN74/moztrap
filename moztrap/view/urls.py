"""
MozTrap root URLconf.

"""
from django.conf.urls.defaults import patterns, url, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from tastypie.api import Api

from moztrap.model.execution.api import RunResource, RunCasesResource, \
    RunEnvironmentsResource

from moztrap.model.environments.api import EnvironmentResource
#from moztrap.model.library.api import CaseVersionResource
from moztrap.model.core.api import ProductResource, ProductVersionResource

admin.autodiscover()

import session_csrf
session_csrf.monkeypatch()

v1_api = Api(api_name='v1')
v1_api.register(RunResource())
v1_api.register(RunCasesResource())
v1_api.register(RunEnvironmentsResource())

#v1_api.register(ResultResource())
#v1_api.register(CaseVersionResource())
v1_api.register(EnvironmentResource())
v1_api.register(ProductResource())
v1_api.register(ProductVersionResource())



run_resource = RunResource()

urlpatterns = patterns(
    "",
    url(r"^$", "moztrap.view.views.home", name="home"),

    # runtests ---------------------------------------------------------------
    url(r"^runtests/", include("moztrap.view.runtests.urls")),

    # users ------------------------------------------------------------------
    url(r"^users/", include("moztrap.view.users.urls")),

    # manage -----------------------------------------------------------------
    url(r"^manage/", include("moztrap.view.manage.urls")),

    # results ----------------------------------------------------------------
    url(r"^results/", include("moztrap.view.results.urls")),

    # admin ------------------------------------------------------------------
    url(r"^admin/", include(admin.site.urls)),

    # browserid --------------------------------------------------------------
    url(r"^browserid/", include("moztrap.view.users.browserid_urls")),

    # api --------------------------------------------------------------------
    url(r"^api/", include(v1_api.urls)),

    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)