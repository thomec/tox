module.exports = function(grunt) {
  "use strict";
  require("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

//concat javascript
  concat: {
    dist: {
      src: [
        'bower_components/jquery/dist/jquery.min.js',
        'bower_components/bootstrap/dist/js/bootstrap.min.js',
        'bower_components/skrollr/dist/skrollr.min.js',
        'bower_components/qrcodejs/qrcode.min.js',
        'bower_components/chartist/dist/chartist.min.js',
        'bower_components/bootstrap-datepicker/js/bootstrap-datepicker.js'
        ],
      dest: 'static/js/main.js',
      }
    },

//minify javascript
  uglify: {
    build: {
      src: 'static/js/main.js',
      dest: 'static/js/main.min.js'
      }
    },

//combine css and minify
  cssmin: {
    combine: {
      files: {
        'static/css/main.min.css': [
          'bower_components/bootstrap/dist/css/bootstrap.css',
          'bower_components/bootstrap-datepicker/dist/css/bootstrap-datepicker3.css',
          'bower_components/font-awesome/css/font-awesome.css',
          'bower_components/chartist/dist/chartist.min.css'
          ]
        }
      },
    minify: {
      src: 'static/css/main.min.css',
      dest: 'static/css/main.min.css'
      }
    },

//compress images
  imagemin: {
    dynamic: {
      files: [{
        expand: true,
        cwd: 'static/img/',
        src: ['**/*.{png,jpg,gif}'],
        dest: 'static/img/'
        }]
      }
    },

//copy files
  copy: {
    main: {
      files: [
        // includes files within path
        {
          expand: true,
          flatten: true,
          src: [
            'bower_components/font-awesome/fonts/*',
            'bower_components/bootstrap/fonts/*'
            ],
          dest: 'static/fonts/',
          filter: 'isFile'
          },
        ],
      },
    },

//watch changes
  watch: {
    options: {
      livereload: true,
      },
    scripts: {
      files: ['static/js/*.js', 'static/css/*.css', 'templates/polls/*.html'],
      tasks: [],
      options: {
        spawn: false,
        },
      }
    }
  });

//register tasks
  grunt.registerTask('default', [
    'concat',
    'uglify',
    'cssmin',
    'imagemin',
    'copy'
  ]);
};
