var userFeed = new Instafeed({
  get: 'user',
  userId: '15097742',
  clientId: '1e2670966288411aa652756a42b97a67',
  accessToken: '15097742.1e26709.8b8ab46ecb6a481cb3027a4db970e074',
  resolution: 'low_resolution',
  limit: '4',
  template: '<li><a href="{{link}}"><img src="{{image}}" /></a></li>'
});
userFeed.run();
