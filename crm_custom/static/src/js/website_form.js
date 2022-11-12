odoo.define('crm_custom.animation', function (require) {
'use strict';

    var core = require('web.core');
    var ajax = require('web.ajax');
    var sAnimation = require('website.content.snippets.animation');
    var qweb = core.qweb;
    var crmUtils = require('crm_custom.utils');

    sAnimation.registry.form_builder_send = sAnimation.registry.form_builder_send.extend({
        start: function (editable_mode) {
            this.crm_custom_loaded = ajax.loadXML('/crm_custom/static/src/xml/website_form.xml', qweb);
            return this._super.apply(this, arguments);
        },

        update_status: function (status) {
            if (status === "email_error"){
                var $result = this.$('#o_website_form_result');
                this.crm_custom_loaded.done(function () {
                    $result.replaceWith(qweb.render("crm_custom.status_" + status));
                });
                return;
            }
            this._super.apply(this, arguments);
        },

        send: function (e) {
            let model_name = this.$target.data('model_name');

            if (model_name === "crm.lead") {
                let email = $('input[name="email_from"]');
                email.removeClass('is-invalid');

                if (!crmUtils.validate_email(email.val())) {
                    this.update_status('email_error');
                    email.addClass('is-invalid');
                    return false;
                }
            }

            this._super.apply(this, arguments);
        },
    });
});