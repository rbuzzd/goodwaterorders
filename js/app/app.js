var products;
var currentProduct;
var productsView;

var customers;
var currentCustomer;
var customersView;

requirejs([
    //Libs
    "jquery",
    "jquery.mobile",
    //Deps
    "../modules/products/collections/products",
    "../modules/products/views/products",
    "../modules/customers/collections/customers",
    "../modules/customers/views/customers"

], function ($, mobile, Products, ProductsView, Customers, CustomersView) {

    products = new Products();
    products.fetch();
    productsView = new ProductsView();

    customers = new Customers();
    customers.fetch();
    customersView = new CustomersView();


});

function ShowProducts() {
    if (productsView != undefined) {
        productsView.render(products.models);
    }
    else{
        alert('Попробуйте чуть позже, список еще не загрузился')
    }
}


function ShowCustomers() {
    if (customersView != undefined) {
        customersView.render(customers.models);
    }
    else{
        alert('Попробуйте чуть позже, список еще не загрузился')
    }
}
