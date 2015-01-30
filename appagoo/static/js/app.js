angular.module('storeApp', ['ngResource'])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}
    $interpolateProvider.startSymbol('[[').endSymbol(']]');

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.
    $resourceProvider.defaults.stripTrailingSlashes = false;
    })
    .controller('StoreController', function ($scope, $http) {
        $http.get('../api/applications/?format=json').success(function(data) {
           $scope.applications = data;
        });

        $scope.nextPage = function() {

        };
        /* TEST PAGINATION
        $scope.main = {
            page: 1
        };

        $scope.loadPage = function() {
           $http.get('../api/applications/?page=' + $scope.main.page + '&format=json').success(function(data) {
               $scope.applications = data.results;
               $scope.hasNext = data.next;
           });
        };

        $scope.nextPage = function () {
            if($scope.hasNext != null) {
                $scope.main.page++;
                $scope.loadPage();
            }
        };
        */
    });

/*
    .factory('StoreService', ['$resource', function($resource) {
        var factory = {
            applications: $resource()
        }
        return $resource('/api/applications/:id');
    }]);
*/