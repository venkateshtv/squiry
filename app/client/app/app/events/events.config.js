(function () {
    function eventsConfig($stateProvider, $urlRouterProvider, $urlMatcherFactoryProvider) {
        var eventType = {
            encode: function (str) {
                return str && str.replace(/ /g, "-");
            },
            decode: function (str) {
                return str && str.replace(/-/g, " ");
            },
            is: angular.isString,
            pattern: /[^/]+/
        };
        $urlMatcherFactoryProvider.type('event', eventType);

        $stateProvider.state('eventsmanage', {
            url: '/eventsmanage',
            views: {
                'pages': {
                    template: '<events-manage></events-manage>'
                }
            }
        }).state('eventdetails', {
            url: '/events/{eventname:event}/{eventid:int}',
            views: {
                'pages': {
                    template: '<event-details></event-details>'
                }
            }
        }).state('eventlanding', {
            url: '/eventlanding/{eventname:event}/{eventid:int}',
            views: {
                'pages': {
                    template: '<event-landing></event-landing>'
                }
            }
        }).state('eventcheckout', {
            url: '/eventlanding/checkout',            
            views: {
                'pages': {
                    templateUrl: 'dist/app/events/eventcheckout.template.html',
                    controller:'eventCheckoutController',
                    controllerAs:'eventCheckout'
                }                
            }
        });        
        $urlRouterProvider.otherwise('/eventlanding/Its%20so%20Sunny%20%7C%20Sunny%20&%20Andrea%20Live-in%20Concert/23');
    }
    eventsConfig.$inject = ['$stateProvider', '$urlRouterProvider', '$urlMatcherFactoryProvider'];
    angular.module('squiryapp.events').config(eventsConfig);

})();