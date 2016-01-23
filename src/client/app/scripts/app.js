/**
 * Created by Ofir_Dagan on 23/01/2016.
 */
var app = angular.module('djangoiTunes', []);

app.config(function($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
