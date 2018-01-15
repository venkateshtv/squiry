(function () {
    function sqImageUploaderLink(scope, element, attrs) {
        element.bind('change', function () {
            scope.imageUploader.changeImageFile(element[0].files[0]);
            console.log("Image File", element[0].files[0]);
        });
    }
    sqImageUploaderLink.$inject = ['scope', 'element', 'attrs'];
    var imageUploadDirective = function () {
        return {
            restrict: 'A',
            link: sqImageUploaderLink,
            bindToController: true,
            scope: {
                uploadfile: '&'
            },
            controllerAs: "imageUploader",
            controller: function () {
                var vm = this;
                vm.changeImageFile = function (file) {
                    vm.uploadfile()(file);
                    // var reader = new FileReader();
                    // reader.onloadend = function (e) {
                    //     var data = e.target.result;
                    //     vm.uploadfile()(data);
                    // }
                    // reader.readAsArrayBuffer(file);
                    
                };
            }
        };
    };
    angular.module('squiryapp.tools').directive('sqImageUploader', imageUploadDirective);
})();