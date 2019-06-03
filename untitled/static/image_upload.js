angular.module('DemoApp', [])
    .controller('DemoController', function($scope) {
        $scope.loadFile = function(event) {
            $('.upload-cta').css({
                'background': 'url(' + URL.createObjectURL(event.target.files[0]) + ') center'
            }).addClass('upload-preview');
        };

        $scope.uploadFile = function() {
            $('#avatar-upload').click();
        };
    });



var altLoadFile = function(event) {
    $('.upload-cta').css({
        'background': 'url(' + URL.createObjectURL(event.target.files[0]) + ') center'
    }).addClass('upload-preview');
};