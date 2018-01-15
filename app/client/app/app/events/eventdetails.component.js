(function(){        
    var eventDetailsComponent = {
        templateUrl:'dist/app/events/eventdetails.template.html',
        controllerAs:'eventDetailsComponent',
        controller:'eventDetailsController'
    };
    angular.module('squiryapp.events').component('eventDetails',eventDetailsComponent);    
})();