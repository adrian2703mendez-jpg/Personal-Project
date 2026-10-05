(() => {
  const apiBase = 'http://localhost:5000';

  async function getSession() {
    const response = await fetch(`${apiBase}/api/session`, {
      credentials: 'include'
    });

    if (!response.ok) return null;
    const data = await response.json();
    return data.success ? data.user : null;
  }

  async function requireSession() {
    const user = await getSession();
    if (!user) {
      const returnTo = `${window.location.pathname}${window.location.search}`;
      window.location.href = `Login.html?returnTo=${encodeURIComponent(returnTo)}`;
      return null;
    }

    window.currentUser = user;
    document.documentElement.classList.add('authenticated');
    return user;
  }

  window.getSession = getSession;
  window.requireSession = requireSession;

  document.addEventListener('click', async event => {
    const accountLink = event.target.closest('[onclick*="goToAccount"]');
    if (!accountLink) return;

    event.preventDefault();
    event.stopImmediatePropagation();
    const user = await getSession();
    window.location.href = user ? 'Account.html' : 'Login.html';
  }, true);

  if (document.body.dataset.requiresAuth === 'true') {
    document.documentElement.classList.add('auth-pending');
    document.addEventListener('DOMContentLoaded', () => {
      requireSession().finally(() => {
        document.documentElement.classList.remove('auth-pending');
      });
    });
  }
})();
