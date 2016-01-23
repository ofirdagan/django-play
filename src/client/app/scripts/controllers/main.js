/**
 * Created by Ofir_Dagan on 23/01/2016.
 */
(function () {
  angular.module('djangoiTunes').controller('MainCtrl', function (iTunesApi) {
    this.artists = [];

    iTunesApi.getArtists().then(function (artists) {
      angular.copy(artists, this.artists);
    }.bind(this));

    this.submit = function () {
      iTunesApi.addArtist(this.artist);
    };
  });
})();