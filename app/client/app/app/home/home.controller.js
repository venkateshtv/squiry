(function () {
    function homeController($scope, $state, events) {
        var vm = this;
        vm.banners = [];
        vm.topEvents = [];
        vm.getTopEvents = getTopEvents;
        vm.eventCategories = [];

        function getBanners() {
            events.getBanners().then(function (result) {
                vm.banners = result.data;
            }).catch(function (error) {
                console.log("ERROR getting Banners");
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
                vm.searchSelectedCategory = vm.eventCategories[0];
                getTopEvents();
            }).catch(function(error){
                console.log("Error getting categories");
            });
        }
        function init() {
            getBanners();            
            getEventCategories();
        }
        init();

    }
    homeController.$inject = ['$scope', '$state', 'events'];
    angular.module('squiryapp.home').controller('homecontroller', homeController);
})();