const gulp = require('gulp')
const autoprefixer = require('gulp-autoprefixer');
const concat = require('gulp-concat');
const cleanCSS = require('gulp-clean-css')
const browserSync = require('browser-sync').create();
const exec = require('child_process').exec;

browserSync.init({
	notify: false,
	port: 8000,
	proxy: 'localhost:8000'
    });


function style(){
	return gulp.src('./src/**/*.css')
			.pipe(concat('style.css'))
			.pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        	}))
        	.pipe(cleanCSS({compatibility: 'ie8'}))
			.pipe(gulp.dest('./css'))
			.pipe(browserSync.stream());
};

function watch(){
	return gulp.watch('./src/**/*.css', style);
};

gulp.task('css', style);
gulp.task('watch', watch);