(function(){        
    var eventLandingComponent = {
        templateUrl:'dist/app/events/eventlanding.template.html',
        controllerAs:'eventLandingComponent',
        controller:'eventDetailsController'
    };
    angular.module('squiryapp.events').component('eventLanding',eventLandingComponent);    
})();