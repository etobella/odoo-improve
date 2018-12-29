# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import logging
from datetime import datetime
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__)


class TestGroup(TransactionCase):

    def setUp(self):
        super(TestGroup, self).setUp()

    def check_group(self, i, u, hier=False):
        _logger.info('Start for %s groups and %s users' % (i, u))
        start_date = datetime.now()
        group = self.env['res.groups'].create({
            'name': 'Group',
        })
        user = self.env['res.users']
        for j in range(u):
            user |= self.env['res.users'].create({
                'name': 'USer %s' % j,
                'login': 'testing_user%s' % j,
                'email': 'testinguser@odoo.odoo',
                'groups_id': [(4, group.id)]
            })
        group_1 = group
        for j in range(i):
            group_2 = self.env['res.groups'].create({
                'name': 'Group %s' % j
            })
            gr = group if hier else group_1
            # We are trying to simulate how it works on real life
            gr[0].write({'implied_ids': [(4, group_2.id)],})
            self.assertIn(group_2, group[0].trans_implied_ids)
            for us in user:
                self.assertIn(group_2, us.groups_id)
            group_1 = group_2
        _logger.info('Lasted for %s' % (
            datetime.now() - start_date
        ).total_seconds())

    def test_10(self):
        self.check_group(10, 1)

    def test_20(self):
        self.check_group(20, 1)

    def test_30(self):
        self.check_group(30, 1)

    def test_10_10(self):
        self.check_group(10, 10)

    def test_20_10(self):
        self.check_group(20, 10)

    def test_30_10(self):
        self.check_group(30, 10)

    def test_10_h(self):
        self.check_group(10, 1, True)

    def test_20_h(self):
        self.check_group(20, 1, True)

    def test_30_h(self):
        self.check_group(30, 1, True)

    def test_10_10_h(self):
        self.check_group(10, 10, True)

    def test_20_10_h(self):
        self.check_group(20, 10, True)

    def test_30_10_h(self):
        self.check_group(30, 10, True)
