# -*- coding: utf-8 -*-
import logging

from odoo import api, Command, fields, models, _

_logger = logging.getLogger(__name__)


class Attendee(models.Model):
    _inherit = 'calendar.attendee'

    def _should_notify_attendee(self):
        """ override base Utility method that determines if the attendee should be notified. """
        self.ensure_one()
        # return self.partner_id != self.env.user.partner_id
        return True  # we want to notify current user also
