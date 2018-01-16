(function () {
    function events($http) {
        var vm = this;
        vm.getBanners = getBanners;
        vm.getTopEvents = getTopEvents;
        vm.getEventCategories = getEventCategories;
        vm.getEventDetails = getEventDetails;
        vm.getAllEvents = getAllEvents;
        vm.addEvent = addEvent;
        vm.updateEvent = updateEvent;
        vm.uploadEventImage = uploadEventImage;
        vm.calculateDiscountPrice = calculateDiscountPrice;

        function calculateDiscountPrice(totalPrice,percentageDiscount, discounts) {
            if (totalPrice === 0 || (discounts && discounts.length == 0)) {
                return;
            }
            var price = totalPrice;
            if (percentageDiscount && percentageDiscount.discounttype === "percentage") {
                price = totalPrice - ((totalPrice * percentageDiscount.discountvalue) / 100);
            }
            for (var i in discounts) {
                var discount = discounts[i];
                // if (!discount.registered) {
                //     return false;
                // }
                if (discount.validcoupon && discount.discounttype === "couponflat") {
                    price = price - discount.discountvalue;
                } else if (discount.validcoupon && discount.discounttype === "couponpercentage") {
                    price = price - ((price * discount.discountvalue) / 100);
                }
            }
            return price;
        }

        function getBanners() {
            return $http.get('api/banners');
        }

        function getTopEvents(category) {
            return $http.get('api/topevents');
        }

        function getEventCategories() {
            return $http.get('api/eventcategories');
        }

        function getEventDetails(eventname, eventid) {
            return $http.get('api/event/' + eventname + '/' + eventid)
        }

        function getAllEvents() {
            return $http.get('api/allevents');
        }

        function addEvent(event) {
            return $http.post('api/addevent', event);
        }

        function updateEvent(event) {
            return $http.post('api/updateevent', event);
        }

        function uploadEventImage(file) {
            var formdata = new FormData();
            formdata.append('file', file);
            return $http({
                url: 'api/uploadeventimage',
                method: "POST",
                data: formdata,
                headers: {
                    'Content-Type': undefined
                }
            });
        }
        return vm;
    }
    events.$inject = ['$http'];
    angular.module('squiryapp.events').service('events', events);
})();