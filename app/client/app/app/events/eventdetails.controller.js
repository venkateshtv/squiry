(function () {
    function eventDetailsController($scope, $state,$stateParams, events, $window) {
        var vm = this;
        vm.event = {};
        vm.message = "";
        vm.calculatePrice = calculatePrice;
        vm.calculateTotalPrice = calculateTotalPrice;
        vm.totalPrice = 0;
        vm.discounts = {};
        vm.finalPriceBeforeTax = 0;

        function calculatePrice(price){
            price.totalPrice = (price.selectedQuantity ? price.selectedQuantity : 0) * price.price;
            return price.totalPrice;
        }

        function calculateTotalPrice(){
            if(Object.keys(vm.event).length === 0 && vm.event.constructor === Object){
                return;
            }
            vm.totalPrice = 0;
            for(var price in vm.event.prices){
                vm.totalPrice += vm.event.prices[price].totalPrice ? vm.event.prices[price].totalPrice : 0;
            }
            vm.finalPriceBeforeTax = vm.totalPrice ? vm.totalPrice : 0;
            if(Object.keys(vm.discounts).length >= 1){
                vm.finalPriceBeforeTax = events.calculateDiscountPrice(vm.totalPrice,vm.discounts.percentageDiscount,vm.discounts.coupondiscounts);               
            }
            if(vm.totalPrice == 0 || !vm.finalPriceBeforeTax || vm.finalPriceBeforeTax == 0){
                return 0;
            }
            vm.tax = (vm.finalPriceBeforeTax * 3/100);
            vm.finalPriceAfterTax =  vm.finalPriceBeforeTax + vm.tax;
            return vm.totalPrice;
        }
                
        function parseDiscounts(){
            for(var i in vm.event.discounts){
                var discount = vm.event.discounts[i];
                if(discount.discounttype === "percentage"){
                    vm.discounts.percentageDiscount = discount;
                } else {
                    if(!vm.discounts.coupondiscounts){
                        vm.discounts.coupondiscounts=[];
                    }
                    vm.discounts.coupondiscounts.push(discount);
                }
            }
        }
        function getEventDetail(eventname,eventid){
            console.log("Attempting to load event");
            vm.message = "";
            events.getEventDetails(eventname,eventid).then(function(result){
                if(result.data.length !== 0){
                    vm.event = result.data;                    
                    parseDiscounts();
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