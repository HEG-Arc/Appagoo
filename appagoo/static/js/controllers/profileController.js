'use strict';

angular.module('appagooApp')
    .controller('profileController', function ($scope, $http) {

        $http.get('../../api/threats/?format=json').then(function(results) {
            $scope.threats = results.data;

        });

    });