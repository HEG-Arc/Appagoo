// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('storeApp', ['ngResource'])
  .factory('ApplicationService', ['$resource', function($resource) {
    return $resource('/api/applications/:id/');
  }])
