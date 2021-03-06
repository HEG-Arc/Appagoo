'use strict';

angular.module('appagooApp')
    .controller('storeController', function ($scope, $http, $filter) {

        var makeFilterItems = $filter('makeFilterItems');
        $scope.minRate=0;
        $scope.priceFilter = {
            free:true,
            commercial:false
        };


        $http.get('../../api/applications/?format=json').then(function(results) {
            $scope.applications = results.data;

            $scope.filter = makeFilterItems($scope.applications, "category", true);
        });

        //filter
        $scope.filterByCategory = function(item) {
            return $scope.filter.check[item.category];
        };

        $scope.filterByMinimalRate = function(item) {
            return item.evaluation >= $scope.minRate;
        };

        $scope.filterByPrice = function(item) {
            if($scope.priceFilter.free && $scope.priceFilter.commercial) {
                return item.price >= 0;
            }
            if(!$scope.priceFilter.free && !$scope.priceFilter.commercial) {
                return item.price >= 0;
            }
            if($scope.priceFilter.free && !$scope.priceFilter.commercial) {
                return item.price == 0;
            }
            if(!$scope.priceFilter.free && $scope.priceFilter.commercial) {
                    return item.price > 0;
            }
        }


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

        $scope.changeCommercialPriceFilter = function() {
            $scope.priceFilter.commercial = !$scope.priceFilter.commercial;
        };

        $scope.changeFreePriceFilter = function() {
            $scope.priceFilter.free = !$scope.priceFilter.free;
        };
    });