######################################################################
# Cloud Routes Web Application
# -------------------------------------------------------------------
# Health Check - Forms Class
######################################################################

from ..base import BaseCheckForm


class CheckForm(BaseCheckForm):
    ''' Class that creates an web form for the dashboard '''
    title = "PaperTrail: Webhook"
    description = """    After creation this monitor will generate a unique URL that can be used with PaperTrail Webhooks. PaperTrail webhooks can be generated as a result of any defined alert. A user could use this functionality to detect database connectivity errors, application errors or increases in traffic.
    """
    webhook_include = "monitors/webhooks/papertrail.html"

if __name__ == '__main__':
    pass
