from odoo import models, fields, api


class PortalMixin(models.AbstractModel):
    _inherit = "portal.mixin"

    def _notify_get_groups(self, msg_vals=None):
        access_token = self._portal_ensure_token()
        groups = super(PortalMixin, self)._notify_get_groups(msg_vals=msg_vals)

        if access_token:
            mm_platform_domain = self.env['ir.config_parameter'].sudo().get_param('platform.mm.domain')
            access_link = mm_platform_domain + '/orders/' + str(self.id) + '?access_token=' + str(access_token)

            new_group = [
                ('portal_customer', lambda pdata: pdata['type'] == 'customer', {
                    'has_button_access': False,
                    'button_access': {
                        'url': access_link,
                        'title': "View in our new Platform"
                    },
                    'notification_is_customer': True,
                })
            ]

            # remove the existing portal_customer group introduced by the portal module
            groups = [group for group in groups if group[0] != 'portal_customer']

        else:
            new_group = []
        return new_group + groups
