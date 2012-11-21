define([
    //Libs
    'backbone',
    //Deps
    './product',
    '../collections/products',
    'text!../../../../../templates/product.html'
],
    function (Backbone, ProductView, Products, ItemTemplate) {
        return Backbone.View.extend({

            /*	    events : {
             'click #bt':'btClick'
             },
             */
            template:_.template(ItemTemplate),

            render:function (products) {
                /*var products = this.options.products;
                 var content = '<div id='productsDiv'><ul id='productsList'>'
                 for(var i in products){
                 content+='<li>' + products[i].get('Name') + '</li>';
                 }
                 content += '</ul></div>';
                 this.$el.html(content);
                 return this;*/

                //products = options.products.models;
                var content = '';
                for (var i in products) {
                    content += this.template(products[i].toJSON());
                }
                $("#productsList").html(content).listview('refresh');

                return this;
            }
        })

    });