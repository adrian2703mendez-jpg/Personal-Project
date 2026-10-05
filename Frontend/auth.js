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

  async function getAccess() {
    const response = await fetch(`${apiBase}/api/access`, {
      credentials: 'include'
    });

    if (!response.ok) return null;
    const data = await response.json();
    return data.success ? data.access : null;
  }

  async function requireSession() {
    const user = await getSession();
    if (!user) {
      const returnTo = `${window.location.pathname}${window.location.search}`;
      window.location.href = `Login.html?returnTo=${encodeURIComponent(returnTo)}`;
      return null;
    }

    window.currentUser = user;
    if (document.body.dataset.requiresAccess === 'true') {
      const access = await getAccess();
      if (!access || !access.allowed) {
        window.location.href = 'Upgrade.html';
        return null;
      }
      window.currentAccess = access;
    }
    document.documentElement.classList.add('authenticated');
    return user;
  }

  window.getSession = getSession;
  window.getAccess = getAccess;
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
