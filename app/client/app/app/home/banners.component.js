(function(){        
    var bannersComponent = {
        templateUrl:'dist/app/home/banners.template.html',      
        bindings:{
            banners:'<'
        },
        controllerAs: 'bannerComponent',
        controller:'bannersController'        
    };
    angular.module('squiryapp.home').component('banners',bannersComponent);    
})();