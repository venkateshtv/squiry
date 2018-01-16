(function () {
    function bannersController($scope, $state, events) {
        var vm = this;
        vm.goToEvent = function(banner){
            $state.go('eventdetails',{eventname:banner.name,eventid:banner.id});
        };
    }
    bannersController.$inject = ['$scope', '$state', 'events'];
    angular.module('squiryapp.home').controller('bannersController', bannersController);
})();