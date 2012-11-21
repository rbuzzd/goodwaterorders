define([
    //Libs
    'backbone',
    //Deps
    './customer',
    '../collections/customers',
    'text!../../../../../templates/customer.html'
],
    function (Backbone, CustomerView, Customers, ItemTemplate) {
        return Backbone.View.extend({

            /*	    events : {
             'click #bt':'btClick'
             },
             */
            template:_.template(ItemTemplate),

            render:function (customers) {
                var content = '';
                for (var i in customers) {
                    content += this.template(customers[i].toJSON());
                }
                $("#customersList").html(content).listview('refresh');

                return this;
            }
        })

    });