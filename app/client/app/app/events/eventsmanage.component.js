(function(){        
    var eventsManageComponent = {
        templateUrl:'dist/app/events/eventsmanage.template.html',
        controllerAs:'eventsManageComponent',
        controller:'eventsManageController'
    };
    angular.module('squiryapp.events').component('eventsManage',eventsManageComponent);    
})();