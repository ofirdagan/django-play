/**
 * Created by Ofir_Dagan on 23/01/2016.
 */
(function() {
  angular.module('djangoiTunes').service('iTunesApi', function ($http) {
    this.addArtist = function (artistName) {
      return $http.post('/api/v1/artists/', {name: artistName}).then(function (response) {
        console.log(response.data);
      });
    };

    this.getArtists = function () {
      return $http.get('/api/v1/artists/').then(function (response) {
        return response.data;
      });
    }
  });
})();
