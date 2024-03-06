from odoo import models, fields, api

class CustomMailMail(models.Model):
    _inherit = 'mail.mail'

    @api.model
    def create(self, vals):
        recipient_ids = vals.get('recipient_ids')
        if len(recipient_ids) > 1:
            recipient_ids = [recipient_id[1] for recipient_id in recipient_ids]
            recipients = self.env['res.partner'].browse(recipient_ids)
            recipient_emails = recipients.mapped('email')
            recipient_emails_csv = ','.join(recipient_emails)
            vals['email_to'] = recipient_emails_csv
            vals['recipient_ids'] = [(5,)]  # Clear existing many2many relations

        # Call the super method to continue with the creation process
        return super(CustomMailMail, self).create(vals)
