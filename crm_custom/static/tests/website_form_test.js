odoo.define('crm_custom.utils_tests', function (require) {
"use strict";
var crmUtils = require('crm_custom.utils');

QUnit.module('crm_custom', {}, function () {

    QUnit.module('utils');

    QUnit.test("Email validation", function (assert) {
        assert.expect(3);
        assert.strictEqual(crmUtils.validate_email("pepe"), false);
        assert.strictEqual(crmUtils.validate_email("jesus@sanchez.lopez"), true);
        assert.strictEqual(crmUtils.validate_email("pepe@pepe"), false);
    });
});
});
