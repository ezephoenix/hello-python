var frisby = require('frisby');
var getApiUrl = function(relativePath) {
  var baseUrl = process.env['baseUrl'];
  if (!baseUrl) {
    baseUrl = 'http://localhost:5000';
  }
  return baseUrl + relativePath;
};

frisby.create('Get market data')
  .get(getApiUrl('/hello'))
  .expectStatus(200)
  .expectHeaderContains('content-type', 'text/html')
  .inspectBody()
.toss();