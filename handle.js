const handler = Plaid.create({
  token: 'GENERATED_LINK_TOKEN',
  onSuccess: (public_token, metadata) => {
    fetch('//yourserver.com/get_access_token', {
      method: 'POST',
      body: {
        public_token: public_token,
        accounts: metadata.accounts,
        institution: metadata.institution,
        link_session_id: metadata.link_session_id,
      },
    });
  },
  onLoad: () => {},
  onExit: (error, metadata) => {
    // Save data from the onExit handler
    supportHandler.report({
      error: error,
      institution: metadata.institution,
      link_session_id: metadata.link_session_id,
      plaid_request_id: metadata.request_id,
      status: metadata.status,
    });
  },
  onEvent: (eventName, metadata) => {
    // send event and metadata to self-hosted analytics
    analytics.send(eventName, metadata);
  },
  receivedRedirectUri: null,
});
handler.open();
handler.exit();
handler.destroy();
