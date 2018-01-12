(function(){        
    var squiryPicksComponent = {
        templateUrl:'dist/app/home/squirypicks.template.html',      
        bindings:{
            events:'<'
        },
        controllerAs: 'squirypicks'        
    };
    angular.module('squiryapp.home').component('squiryPicks',squiryPicksComponent);    
})();