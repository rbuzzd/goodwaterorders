define([
    //Libs
    'backbone'
    //Deps
], function (Backbone) {
        return Backbone.View.extend({
            initialize:function () {
            },
            render:function () {
                var product = this.options.product;
                this.$el.html(product.get("Name") + " " + product.get("Price"));
                return this;
            }
        });
    }
);

