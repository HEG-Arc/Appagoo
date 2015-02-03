'use strict';

angular.module('storeApp')
    .controller('StoreController', function ($scope, $http, $filter) {

        var makeFilterItems = $filter('makeFilterItems');

        $http.get('../../api/applications/?format=json').then(function(results) {
            $scope.applications = results.data;

            $scope.filter = makeFilterItems($scope.applications, "category", true);
            console.log($scope.applications);

        });

        //filter
        $scope.filterByCategory = function(item) {
            return $scope.filter.check[item.category];
        };

    });