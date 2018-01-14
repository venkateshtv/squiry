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
        function getEventDetails(eventid){
            return $http.get('api/getevent/'+eventid)
        }
        function getAllEvents(){
            return $http.get('api/allevents');
        }
        function addEvent(event){
            return $http.post('api/addevent',event);
        }
        function updateEvent(event){
            return $http.post('api/updateevent',event);
        }
        return vm;
    }
    events.$inject = ['$http'];
    angular.module('squiryapp.events').service('events',events);    
})();