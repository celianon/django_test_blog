// Webpack v4
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: ['./src/js/index.js', './src/css/style.css'],
  output: {
    path: path.resolve(__dirname, 'build/js'),
    filename: 'main.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
         use: [ { loader: 'babel-loader'} ],
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract(
          {
            fallback: 'style-loader',
            use: ['css-loader']
          })
      },
      
    ]
  },
  plugins: [ 
    new ExtractTextPlugin({filename: '../css/style.css'})
  ]
}