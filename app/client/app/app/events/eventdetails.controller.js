(function () {
    function eventDetailsController($scope, $state,$stateParams, events, $window) {
        var vm = this;
        vm.event = {};
        vm.message = "";
                
        function getEventDetail(eventname,eventid){
            console.log("Attempting to load event");
            vm.message = "";
            events.getEventDetails(eventname,eventid).then(function(result){
                if(result.data.length !== 0){
                    vm.event = result.data;                    
                } else {
                    vm.message = "No active event found";
                }                
            }).catch(function(error){
                console.log("Error getting event details");
                vm.message = "Something went wrong while loading the event"
            });
        }
        function init() {            
            getEventDetail($stateParams.eventname,$stateParams.eventid);    
            $window.openGoogleMaps(13.0827,80.2707);
        }
        init();
        
    }
    eventDetailsController.$inject = ['$scope', '$state','$stateParams', 'events','$window'];
    angular.module('squiryapp.events').controller('eventDetailsController', eventDetailsController);
})();