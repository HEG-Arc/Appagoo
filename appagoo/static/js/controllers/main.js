'use strict';

angular.module('storeApp')
    .controller('storeController', function ($scope, $http, $filter, $animate) {

        var makeFilterItems = $filter('makeFilterItems');
        var minimalRate = $filter('minimalRate');

        $http.get('../../api/applications/?format=json').then(function(results) {
            $scope.applications = results.data;

            $scope.filter = makeFilterItems($scope.applications, "category", true);
        });

        //filter
        $scope.filterByCategory = function(item) {
            return $scope.filter.check[item.category];
        };

        $scope.filterByMinimalRate = function(item) {
            return $scope.filter.minimalRate = item.value;
        };


        function removeFromArray(array, item) {
            var idx = array.indexOf(item);
            if (idx > -1) {
                array.splice(idx, 1);
            }
            return array;
        }

        $scope.addCategoryFilter = function(item) {
            removeFromArray($scope.filter.unchosen, item);
            $scope.filter.chosen.push(item);
            $scope.filter.check[item] = true;
        };

        $scope.removeCategoryFilter = function(item) {
            removeFromArray($scope.filter.chosen, item);
            $scope.filter.unchosen.push(item);
            $scope.filter.check[item] = false;
        };




    });