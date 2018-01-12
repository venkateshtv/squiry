(function(){        
    var topEventsComponent = {
        templateUrl:'dist/app/home/topevents.template.html',      
        bindings:{
            events:'<',
            eventCategories:'<',
            loadEventsByCategory:'&'
        },
        controllerAs:'topEvents'
    };
    angular.module('squiryapp.home').component('topEvents',topEventsComponent);    
})();