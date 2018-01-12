(function () {
    function homeController($scope, $state, events) {
        var vm = this;
        vm.squiryPicks = [];
        vm.topEvents = [];
        vm.getTopEvents = getTopEvents;
        vm.eventCategories = [];

        function getSquiryPicks() {
            events.getSquiryPicks().then(function (result) {
                vm.squiryPicks = result.data;
            }).catch(function (error) {
                console.log("ERROR getting squiry picks");
            });
        }
        function getTopEvents(category){
            events.getTopEvents(category).then(function (result){
                vm.topEvents = result.data;
            }).catch(function (error){
                console.log("Error getting Top events");
            });
        }
        function getEventCategories(){
            events.getEventCategories().then(function (result){
                vm.eventCategories = result.data;
                getTopEvents();
            }).catch(function(error){
                console.log("Error getting categories");
            });
        }
        function init() {
            getSquiryPicks();            
            getEventCategories();
        }
        init();

    }
    homeController.$inject = ['$scope', '$state', 'events'];
    angular.module('squiryapp.home').controller('homecontroller', homeController);
})();