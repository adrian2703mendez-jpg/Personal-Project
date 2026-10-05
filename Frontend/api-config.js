const isLocalFrontend = window.location.hostname === 'localhost' && window.location.port !== '5000';
window.API_BASE_URL = isLocalFrontend ? 'http://localhost:5000' : window.location.origin;
