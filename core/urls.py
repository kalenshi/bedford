from django.urls import path

from core.analytics.event_logger.detail_view import EventLoggerAnalyticsDetailView
from core.analytics.event_logger.list_view import EventLoggerAnalyticsListView
from core.development.event_logger.detail_view import EventLoggerDevelopmentDetailView
from core.development.event_logger.list_view import EventLoggerDevelopmentListView
from core.development.site.detail_view import SiteDetailView
from core.development.site.list_view import SiteListView
from core.seo.member.detail_view import MemberDetailView
from core.seo.member.list_view import MemberListView
from core.seo.site_url.detail_view import SiteUrlDetailView
from core.seo.site_url.list_view import SiteUrlListView

app_name = "core"

urlpatterns = [
    # Development
    path(
        "event_logger_development/",
        EventLoggerDevelopmentListView.as_view(),
        name="event-logger-development"
    ),
    path(
        "event_logger_development/<event_id>/",
        EventLoggerDevelopmentDetailView.as_view(),
        name="event-logger-development-details"
    ),
    path("site/", SiteListView.as_view(), name="sites"),
    path("site/<site_id>/", SiteDetailView.as_view(), name="site-detail"),

    # Seo
    path("site_url/", SiteUrlListView.as_view(), name="site-urls"),
    path("site_url/<url_id>/", SiteUrlDetailView.as_view(), name="site-urls-detail"),
    path("member/", MemberListView.as_view(), name="members-list"),
    path("member/<mem_id>/", MemberDetailView.as_view(), name="member-detail"),

    # Analytics
    path(
        "event_logger_analytics/",
        EventLoggerAnalyticsListView.as_view(),
        name="event-logger-analytics"
    ),
    path(
        "event_logger_analytics/<event_id>/",
        EventLoggerAnalyticsDetailView.as_view(),
        name="event-logger-analytics-details"
    ),

]
