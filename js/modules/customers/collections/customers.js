define([
    //Libs
    'backbone',
    //Deps
    '../models/customer'
], function (Backbone, Customer) {

    return Backbone.Collection.extend({
        model:Customer,
        url:"/getCustomers"
    });

});

