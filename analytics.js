window.onload = function() {
  let userId = localStorage.getItem('user_id');
  if (!userId) {
    userId = uuidv4();
    localStorage.setItem('user_id', userId);
  }

  if (!navigator.doNotTrack) {
    fetch('http://your-server.com/analytics', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_id: userId,
        page: window.location.href,
        user_agent: navigator.userAgent
      })
    }).catch(error => console.error('Error:', error));
  }
};

// Function to generate a new UUID
function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}
