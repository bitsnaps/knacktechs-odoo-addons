odoo.define('datepicker_advanced_search.datepicker', function (require) {
"use strict";
    var datepicker = require('web.datepicker');
    var SearchView = require('web.SearchView');

    datepicker.DateWidget.include({
        events: _.extend({}, datepicker.DateWidget.prototype.events, {
            "click .o_datepicker_button": "click_button",
        }),
        click_button: function(e){
            this.picker.toggle();
        },
    })

    SearchView.include({
        init: function (parent, dataset, fvg, options) {
            this._super.apply(this, arguments);
            this.visible_filters = true;
        },
    })
});