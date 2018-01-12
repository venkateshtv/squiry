(function(){        
    function events($http){
        var vm=this; 
        vm.getSquiryPicks = getSquiryPicks;
        vm.getTopEvents = getTopEvents;
        vm.getEventCategories = getEventCategories;
        
        function getSquiryPicks(){
            return $http.get('api/squirypicksevents');
        }
        function getTopEvents(category){
            return $http.get('api/topevents');
        }
        function getEventCategories(){
            return $http.get('api/eventcategories');
        }
        return vm;
    }
    events.$inject = ['$http'];
    angular.module('squiryapp.events').service('events',events);    
})();