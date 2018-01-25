(function () {
    function eventCheckoutController($scope, $state,$stateParams, events, $window) {
        var vm = this;
        vm.event = {};
        vm.message = "";
        vm.user = {};
        vm.proceedToPayment = proceedToPayment;
        vm.goBack = function(){
            $window.history.back();
        };

        function init(){
            vm.cart= events.getCart();
            if(!vm.cart || vm.cart.length === 0){
                $window.history.back();
            }
        }
        init();
        function create_form_elements(form,formDict){
            
            for(var key in formDict){
                var hiddenField = document.createElement("input");
                hiddenField.setAttribute("type", "hidden");
                hiddenField.setAttribute("name", key);
                hiddenField.setAttribute("value", formDict[key]);    
                form.appendChild(hiddenField);
            }
            return form;
        }
        function payment_order(params, paymentRequest){
            //Create PaymentFormdata
            //Post form
            //var payU = "https://secure.payu.in/_payment";
            var payU = "https://test.payu.in/_payment";
            var form = document.createElement("form");
            form.setAttribute("method", "POST");
            form.setAttribute("action", payU);

            var formDict={};
            formDict['key']=paymentRequest.merchant_key;
            formDict['txnid']=paymentRequest.txnid;
            formDict['hash']=paymentRequest.hash;
            formDict['amount'] =params.amount;
            formDict['productinfo']=params.productinfo;
            formDict['firstname']=params.firstname;
            formDict['email']=params.email;
            formDict['phone']=params.phone;
            formDict['udf1']=params.udf1;
            formDict['udf2']=params.udf2;
            formDict['udf3']=params.udf3;
            formDict['udf4']=params.udf4;
            formDict['udf5']=params.udf5;
            formDict['furl']='https://squiryapp.herokuapp.com/paymentfailure';
            formDict['surl']='https://squiryapp.herokuapp.com/paymentsuccess';
            //formDict['service_provider']='payu_paisa'
            form = create_form_elements(form,formDict);
            document.body.appendChild(form);
            form.submit();

            // var request = new XMLHttpRequest();
            // request.open("POST", payU);
            // request.send(paymentFormData);
        }
        function proceedToPayment(){
            var paymentRequest = null;
            //Get Payment Request
            var params = {};
            params.firstname= vm.user.firstname;
            params.email= vm.user.email;
            params.amount= vm.cart[0].finalPriceAfterTax;
            params.productinfo= vm.cart[0].id;
            params.phone=vm.user.phone;
            params.udf1=vm.cart[0].name;
            params.udf2=vm.cart[0].address;
            params.udf3=vm.cart[0].eventstart;
            params.udf4="4";
            params.udf5="5";
            events.getPaymentRequest(params).then(function(result){
                paymentRequest = result.data;
                payment_order(params,paymentRequest);
            }).catch(function(error){
                console.log("Something went wrong while makig payment request");
                vm.message = "Something went wrong while making payment request";
            });
        }   
    }
    eventCheckoutController.$inject = ['$scope', '$state','$stateParams', 'events','$window'];
    angular.module('squiryapp.events').controller('eventCheckoutController', eventCheckoutController);
})();