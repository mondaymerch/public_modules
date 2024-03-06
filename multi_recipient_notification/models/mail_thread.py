from odoo import models, fields


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    # def _notify_thread(self, message, msg_vals=False, notify_by_email=True, **kwargs):
    #     """ Overwrite the standard notification method so prevent emails being sent
    #     to thread followers that are NOT an internal user
    #     """
    #     msg_vals = msg_vals if msg_vals else {}
    #     rdata = self._notify_compute_recipients(message, msg_vals)
    #     if not rdata:
    #         return rdata
    #
    #     self._notify_record_by_inbox(message, rdata, msg_vals=msg_vals, **kwargs)
    #     if notify_by_email:
    #         self._notify_record_by_email(message, rdata, msg_vals=msg_vals, **kwargs)
    #
    #     return rdata

    def _notify_compute_recipients(self, message, msg_vals):
        rdata = super(MailThread, self)._notify_compute_recipients(message, msg_vals)

        rdata = [recipient for recipient in rdata if recipient['type'] != 'customer']

        return rdata
