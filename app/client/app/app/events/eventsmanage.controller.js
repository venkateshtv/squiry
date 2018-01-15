(function () {
    function eventsManageController($scope, $state, events) {
        var vm = this;
        vm.allevents = [];        
        vm.eventCategories = [];
        vm.newEvent = {};
        vm.AddNewEvent = AddNewEvent;
        vm.message = "";
        function getAllEvents() {
            events.getAllEvents().then(function (result) {
                vm.allevents = result.data;
            }).catch(function (error) {
                console.log("ERROR getting squiry picks");
            });
        }        
        function getEventCategories(){
            console.log("Attempting to load events");
            events.getEventCategories().then(function(result){
                if(result.data){
                    vm.eventCategories = result.data;
                    vm.newEvent.categoryid = vm.eventCategories[0];
                }
                
            }).catch(function(error){
                console.log("Error getting event categories");
            });
        }
        function init() {
            //getAllEvents();                     
            getEventCategories();    
        }
        init();
        function AddNewEvent(){
            vm.message = "";
            vm.newEvent.categoryid = vm.newEvent.id;
            events.addEvent(vm.newEvent).then(function(result){
                vm.message = "Successfully created event with id"+result.data;
            }).catch(function(error){
                vm.message = "Something went wrong while creating event";
            });
        }
    }
    eventsManageController.$inject = ['$scope', '$state', 'events'];
    angular.module('squiryapp.events').controller('eventsManageController', eventsManageController);
})();