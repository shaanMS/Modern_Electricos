# from django.shortcuts import render
# from django.views.generic import TemplateView







#==== Template View Will later updated to CUSTOM GENERIC CBV ======= this is MVP 1 


from django.views.generic import TemplateView
from django.utils import timezone

from .models import AppInstance
from ads.models import Advertisement   # jahan ads ka model hai


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1️⃣ active site
        instance = (
            AppInstance.objects
            .select_related("config")
            .filter(is_active=True)
            .first()
        )

        if not instance or not hasattr(instance, "config"):
            return context

        # 2️⃣ inject JSON config (header, hero, flags etc.)
        context.update(instance.config.data)

        # 3️⃣ ads (site + section based)
        showAds = instance.config.data.get("uiFlags", {}).get("showAds", False)

        if showAds:
            ads = (
                Advertisement.objects
                .filter(
                    siteInstance=instance,
                    sectionName="homepage",
                    isActive=True
                )
                .order_by("position")
            )
            context["ads"] = ads
            context["showAdSection"] = ads.exists()

        return context
