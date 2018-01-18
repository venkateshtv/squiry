(function () {
    function eventCheckoutController($scope, $state,$stateParams, events, $window) {
        var vm = this;
        vm.event = {};
        vm.message = "";
        vm.goBack = function(){
            $window.history.back();
        };

        function init(){
            if(!$state.params.hasOwnProperty('eventsession') || !$state.params.eventsession){
                //$window.history.back();
            }
        }
        init();
       
        
    }
    eventCheckoutController.$inject = ['$scope', '$state','$stateParams', 'events','$window'];
    angular.module('squiryapp.events').controller('eventCheckoutController', eventCheckoutController);
})();