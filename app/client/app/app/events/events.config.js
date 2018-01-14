(function(){        
    function eventsConfig($stateProvider,$urlRouterProvider){
        $stateProvider.state('eventsmanage',{
            url:'/eventsmanage',
            views: {
                'pages':{
                    template:'<events-manage></events-manage>'
                }
            }
        });        
    }
    eventsConfig.$inject = ['$stateProvider','$urlRouterProvider'];
    angular.module('squiryapp.events').config(eventsConfig);
    
})();