var app = angular.module('MoviesApp', ['restangular', 'ui.router']);

app.constant('API_HOST', 'http://127.0.0.1:8000/api/');

app.config(function($stateProvider, RestangularProvider) {

    RestangularProvider.setBaseUrl('http://127.0.0.1:8000/api/v1/');
    RestangularProvider.setRequestSuffix('/');

    $stateProvider
        .state({
            name: "movies",
            url: "/movies",
            controller: 'MovieController as $ctrl',
            templateUrl: "../../views/movie/movie_list.html"
        })
        .state({
            name: "genres",
            url: "/genres",
            controller: "GenreController as $ctrl",
            templateUrl: "../../views/genre/genre_list.html"
        })
        .state({
            name: "directors",
            url: "/directors",
            controller: "DirectorController as $ctrl",
            templateUrl: "../../views/director/director_list.html"
        })
        .state({
            name: "actors",
            url: "/actors",
            controller: "ActorController as $ctrl",
            templateUrl: "../../views/actor/actor_list.html"
        })
        .state({
            name: "music",
            url: "/music",
            controller: "MusicController as $ctrl",
            templateUrl: "../../views/music/music_list.html"
        });
});

app.service('MoviesService', function(Restangular, API_HOST) {
    /**
    Example
    // /movies/
    // /movies/1/
    // /movies/1/genres
    // /movies/1/genres/2/
    // return Restangular
    // .one('movies', 1)
    // .one('genres', 2)
    // .get();
    */
    this.GetMovies = function() {
        return Restangular.one('movies').get();
    };

    return this;

});

app.controller('MovieController', function($scope, $timeout, MoviesService) {
    $scope.MoviesList = [];

    $timeout(function() {
        MoviesService.GetMovies().then(function(response) {
            $scope.$applyAsync(function() {
                $scope.MoviesList = response.data;
            });
        });
    });

});

app.service('GenresService', function(Restangular, API_HOST) {

    this.GetGenres = function() {
        return Restangular.one('genres').get();
    };

    return this;

});

app.controller('GenreController', function($scope, $timeout, GenresService) {
    $scope.GenresList = [];

    $timeout(function() {
        GenresService.GetGenres().then(function(response) {
            $scope.$applyAsync(function() {
                $scope.GenresList = response.data;
            });
        });
    });

});

app.service('DirectorsService', function(Restangular, API_HOST) {

    this.GetDirectors = function() {
        return Restangular.one('directors').get();
    };

    return this;
});

app.controller('DirectorController', function($scope, $timeout, DirectorsService) {
    $scope.DirectorsList = [];

    $timeout(function() {
        DirectorsService.GetDirectors().then(function(response) {
            $scope.$applyAsync(function() {
                $scope.DirectorsList = response.data;
            });
        });
    });

});


app.service('ActorsService', function(Restangular, API_HOST) {

    this.GetActors = function() {
        return Restangular.one('actors').get();
    };

    return this;

});

app.controller('ActorController', function($scope, $timeout, ActorsService) {
    $scope.ActorsList = [];

    $timeout(function() {
        ActorsService.GetActors().then(function(response) {
            $scope.$applyAsync(function() {
                $scope.ActorsList = response.data;
            });
        });
    });

});

app.service('MusicService', function(Restangular, API_HOST) {

    this.GetMusic = function() {
        return Restangular.one('music').get();
    };

    return this;

});

app.controller('MusicController', function($scope, $timeout, MusicService) {
    $scope.MusicList = [];

    $timeout(function() {
        MusicService.GetMusic().then(function(response) {
            $scope.$applyAsync(function() {
                $scope.MusicList = response.data;
            });
        });
    });

});


//todos.controller("TodoController", function($scope) {
//   $scope.filteredTodos = []
//  ,$scope.currentPage = 1
//  ,$scope.numPerPage = 10
//  ,$scope.maxSize = 5;
//
//  $scope.makeTodos = function() {
//    $scope.todos = [];
//    for (i=1;i<=1000;i++) {
//      $scope.todos.push({ text:"todo "+i, done:false});
//    }
//  };
//  $scope.makeTodos();
//
//  $scope.$watch("currentPage + numPerPage", function() {
//    var begin = (($scope.currentPage - 1) * $scope.numPerPage)
//    , end = begin + $scope.numPerPage;
//
//    $scope.filteredTodos = $scope.todos.slice(begin, end);
//  });
//});
