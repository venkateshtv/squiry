(function(){        
    var homeComponent = {
        templateUrl:'dist/app/home/home.template.html',
        controllerAs:'homeComponent',
        controller:'homecontroller'
    };
    angular.module('squiryapp.home').component('home',homeComponent);    
})();