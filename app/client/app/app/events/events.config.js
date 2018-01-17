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
        });        
    }
    eventsConfig.$inject = ['$stateProvider', '$urlRouterProvider', '$urlMatcherFactoryProvider'];
    angular.module('squiryapp.events').config(eventsConfig);

})();