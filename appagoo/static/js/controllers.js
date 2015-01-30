var storeControllers = angular.module('storeApp.controllers', []);

storeControllers.controller('StoreCtrl', function StoreCtrl($scope, Application) {
  $scope.applications = {};

  ApplicationService.query(function(response) {
    $scope.applications = response;
  });

});

--------------------------------------------------------------------------------------------------------------------------test_angular----------------------------------------------------------------------------─ mm