(function () {
    function slickSliderLink(scope, element, attrs) {
        //$(element[0]).addClass('slider-wapper');
        $(element[0]).css('visibility','hidden');
        scope.$watch('slickSlider.valuetowait',function(newValue,oldValue){
            if(newValue != oldValue){
                $(element[0]).slick({
                    arrows: false,
                    autoplay: true,
                    autoplaySpeed: 2000,
                    dots: false,
                    pauseOnFocus: false,
                    pauseOnHover: false,
                    infinite: true,
                    slidesToShow: 1,
                });
                $(element[0]).css('visibility','visible');
                //$(element[0]).removeClass('slider-wapper');
                //$(element[0]).addClass('slider-wapper-slick-initialized');
            }
        });
    }
    slickSliderLink.$inject = ['scope', 'element', 'attrs'];
    var slickSliderDirective = function () {
        return {
            restrict: 'A',
            link: slickSliderLink,
            bindToController: true,
            scope: {
                valuetowait: '<'
            },
            controllerAs: "slickSlider",
            controller: function ($scope) {
                var vm = this;
                
            }
        };
    };
    angular.module('squiryapp.tools').directive('imageSlider', slickSliderDirective);
})();