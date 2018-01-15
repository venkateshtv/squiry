(function () {
    console.log("INTERCEPTOR0");
    angular.module('squiryapp').factory('httpInterceptor', function ($q, $rootScope, $log) {

            var numLoadings = 0;
           console.log("INTERCEPTOR");
            return {
                request: function (config) {

                    numLoadings++;
                    console.log("Num loadings",numLoadings);
                    // Show loader
                    $rootScope.$broadcast("loader_show");
                    return config || $q.when(config)

                },
                response: function (response) {
                    
                    if ((--numLoadings) === 0) {
                        // Hide loader
                        $rootScope.$broadcast("loader_hide");
                    }
                    console.log("Num loadings reduce",numLoadings);
                    return response || $q.when(response);

                },
                responseError: function (response) {

                    if (!(--numLoadings)) {
                        // Hide loader
                        $rootScope.$broadcast("loader_hide");
                    }

                    return $q.reject(response);
                }
            };
        })
        .config(function ($httpProvider) {
            $httpProvider.interceptors.push('httpInterceptor');
        })
        .directive("loader", function ($rootScope) {
            return function ($scope, element, attrs) {
                $scope.$on("loader_show", function () {
                    return element.show();
                });
                return $scope.$on("loader_hide", function () {
                    return element.hide();
                });
            };
        });
    // var config = function ($httpProvider) {
    //     $httpProvider.responseInterceptors.push('myHttpInterceptor');

    //     var spinnerFunction = function spinnerFunction(data, headersGetter) {
    //         $("#spinner").show();
    //         return data;
    //     };
    // };
    // config.$inject = ['$httpProvider'];

    // angular.module('squiryapp').config(config);

    // var httpInterceptorFactor = function ($q, $window) {
    //     return function (promise) {
    //         return promise.then(function (response) {
    //             $("#spinner").hide();
    //             return response;
    //         }, function (response) {
    //             $("#spinner").hide();
    //             return $q.reject(response);
    //         });
    //     };
    // };
    // httpInterceptorFactor.$inject = ['$q','$window'];
    // angular.module('squiryapp').factory('myHttpInterceptor', httpInterceptorFactor);
})();