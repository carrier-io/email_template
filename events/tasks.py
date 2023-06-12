from pylon.core.tools import web, log


class Event:
    integration_name = "email_template"

    @web.event(f"{integration_name}_created_or_updated")
    def _created_or_updated(self, context, event, payload):
        log.info('email template event %s', payload['settings'])
        updated_data = context.rpc_manager.call.integrations_update_attrs(
            integration_id=payload['id'],
            project_id=payload.get("project_id"),
            update_dict={'status': 'success'},
            return_result=True
        )

        context.sio.emit('task_creation', {
            'ok': True,
            **updated_data
        })
