import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Search from './Search';
import registerServiceWorker from './registerServiceWorker';
import $ from 'jquery'
import jQuery from 'jquery'
import 'bootstrap/dist/js/bootstrap.min.js'

ReactDOM.render(<Search />, document.getElementById('search-courses'));
registerServiceWorker();
