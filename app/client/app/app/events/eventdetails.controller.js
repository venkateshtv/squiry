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
        vm.quantities=[{display:" ",value:0},{display:1,value:1},{display:2,value:2},{display:3,value:3},{display:4,value:4},{display:5,value:5},{display:6,value:6},{display:7,value:7},{display:8,value:8},{display:9,value:9},{display:10,value:10}];
        vm.checkout = checkout;
        vm.verifyCoupon = verifyCoupon;
        vm.discountMessage = "";
        
        function updateDiscounts(discountname,discounttype){
            for(var i in vm.discounts.coupondiscounts){
                discount = vm.discounts.coupondiscounts[i];
                if(discount.name == discountname && discounttype == discounttype){
                    discount.validcoupon = true;
                }
            }
        }
        function verifyCoupon(coupon){
            vm.discountMessage = "";
            events.verifyCoupon(vm.event.id,coupon).then(function(result){
                if(result.data && result.data.verified === "true"){
                    vm.discountMessage = "Coupon verified";
                    updateDiscounts(result.data.discountname,result.data.discounttype);
                } else {
                    vm.discountMessage = "Not a valid coupon";
                }
            }).catch(function(error){
                vm.discountMessage = "Something went wrong while verifying coupon";
            });
        }
        function checkout(){
            $state.go('eventcheckout', {eventname:$stateParams.eventname,eventid:$stateParams.eventid,eventsession:JSON.stringify(event)});
        }
        function calculatePrice(price){
            var selectedQuatity = 0;
            if(price.selectedQuantity.hasOwnProperty('value')){
                selectedQuatity = price.selectedQuantity.value;
            } else {
                selectedQuatity = price.selectedQuantity;
            }
            price.totalPrice = selectedQuatity * price.price;
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
            vm.bookingfee = +((vm.finalPriceBeforeTax * 3/100).toFixed(2));
            vm.tax = +((vm.bookingfee * 18/100).toFixed(2));
            vm.finalPriceAfterTax =  vm.finalPriceBeforeTax + vm.bookingfee + vm.tax;
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