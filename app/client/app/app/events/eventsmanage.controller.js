(function () {
    function eventsManageController($scope, $state, events) {
        var vm = this;
        vm.allevents = [];        
        vm.eventCategories = [];
        vm.newEvent = {prices:[]};
        vm.uploadEventImage = uploadEventImage;
        vm.addNewEvent = addNewEvent;                
        vm.addPrice = addPrice;
        vm.removePrice = removePrice;
        
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
        function addNewEvent(){
            vm.message = "";
            vm.newEvent.categoryid = vm.newEvent.categoryid.id;
            events.addEvent(vm.newEvent).then(function(result){
                vm.message = "Successfully created event with id"+result.data;
            }).catch(function(error){
                vm.message = "Something went wrong while creating event";
            });
        }
        function uploadEventImage(file){                       
            events.uploadEventImage(file).then(function(result){
                vm.newEvent.url = result.data;
            }).catch(function(error){
                console.log("Error while uploading image");
            });
        }
        function addPrice(){
            vm.newEvent.prices.push({name:"",price:0,total:0});
        }
        function removePrice(removePrice){
            for(var i=0;i<vm.newEvent.prices.length;i++){
                var price = vm.newEvent.prices[i];
                if(price == removePrice){
                    vm.newEvent.prices.splice(i,1);
                    return false;
                }
            }
        }
    }
    eventsManageController.$inject = ['$scope', '$state', 'events'];
    angular.module('squiryapp.events').controller('eventsManageController', eventsManageController);
})();