requirejs.config({

    deps:[
        "app"
    ],

    paths:{
        "jquery":"../libs/jquery-1.8.2.min",
        "underscore":"../libs/underscore-min",
        "backbone":"../libs/backbone-min",
        "jquery.mobile":"../libs/jquery.mobile-1.1.1.min",

        //Plugins
        "text":"../libs/rjs-text"

    },

    shim:{
        "backbone":{
            deps:["jquery", "underscore"],
            exports:"Backbone"
        }
    }

});

/*requirejs([
 "jquery",
 "underscore",
 "backbone",
 "jquery.mobile"
 ], function(){
 console.log("done")
 });*/