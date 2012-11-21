define([
    //Libs
    'backbone',
    //Deps
    '../models/product'
], function (Backbone, Product) {

    return Backbone.Collection.extend({
        model:Product,
        url:"/getProducts"
    });

});

