(function(){        
    function homeConfig($stateProvider,$urlRouterProvider){
        $stateProvider.state('home',{
            url:'/home',
            views: {
                'pages':{
                    template:'<home></home>'
                }
            }
        });
        //$urlRouterProvider.otherwise('/home');
    }
    homeConfig.$inject = ['$stateProvider','$urlRouterProvider'];
    angular.module('squiryapp.home').config(homeConfig);
    
})();