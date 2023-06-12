from pylon.core.tools import log, web
from tools import constants as c


class Slot:
    @web.slot('administration_email_invitation_content')
    def administration_email_invitation_content(self, context, slot, payload):
        available_integrations = context.rpc_manager.call.integrations_get_administration_integrations_by_name(
            integration_name=self.descriptor.name,
        )
        log.info('From new integration admin %s', available_integrations)
        with context.app.app_context():
            return self.descriptor.render_template(
                'invitation/content.html',
                integrations=available_integrations,
                integrations_url='/~/administration/~/configuration/integrations'
            )

    @web.slot('users_email_invitation_content')
    def users_email_invitation_content(self, context, slot, payload):
        available_integrations = context.rpc_manager.call.integrations_get_all_integrations_by_name(
            payload['project_id'],
            integration_name=self.descriptor.name,
        )
        log.info('From new integration %s', available_integrations)
        with context.app.app_context():
            return self.descriptor.render_template(
                'invitation/content.html',
                integrations=available_integrations,
                integrations_url='/-/configuration/integrations'
            )
