import json

from django.template import Template
from django.template import Context
from django.core.mail import send_mail
from django.conf import settings

from beds.models import AlertRule

class AlertManager():
    """Manages Alert Rules"""
    def run(self, obj, diff):
        """Go Through all Alert Rules to send out alerts."""
        for a in AlertRule.objects.all():
            a = json.loads(a.alert_rule)

            if a["object"] == obj.__class__.__name__:
                if a["attribute"] in diff:
                    if diff[a["attribute"]] == a["changed_to"]:
                        # Criteria Satisfied. Run Alert Action

                        subject = Template(a["action"]["subject"]).render(c)
                        msg = Template(a["action"]["message"]).render(c)

                        if "type" == "email":
                            # Fill out subject/message Template
                            c = Context({
                                "object": obj,
                                "diff": diff
                            })

                            if a["action"]["type"] == "email":
                                send_mail(
                                    subject,
                                    msg,
                                    settings.DEFAULT_FROM_EMAIL,
                                    [a["action"]["to"]],
                                    fail_silently=False,
                                )

                        # TODO Add More Alert Types (phone, text, im)
