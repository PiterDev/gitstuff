import { error, redirect, type Cookies } from '@sveltejs/kit';

export type FetchWithAuth = {
	fetch: typeof globalThis.fetch;
	cookies: Cookies;
	token: string | undefined;
	body: Record<string, unknown> | null;
	endpoint: string;
	method: 'GET' | 'POST' | 'PATCH' | 'DELETE';
	onUnauthorizedRedirect?: string;
	onNotFoundMessage?: string | null;
};

export async function fetchWithAuth({
	fetch,
	cookies,
	endpoint,
	method,
	token,
	body = null,
	onUnauthorizedRedirect = '/auth/github/login',
	onNotFoundMessage = null
}: FetchWithAuth) {
	if (!token) {
		throw redirect(302, onUnauthorizedRedirect);
	}
	const res = await fetch(endpoint, {
		method,
		body: body ? JSON.stringify(body) : null,
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Token ${token}`
		}
	});

	const data = await res.json();

	if (res.status === 401 || data.status === '401') {
		// Token expired
		cookies.delete('token', { path: '/' });
		throw redirect(302, onUnauthorizedRedirect + '?session_expired=true');
	}

	if (res.status === 404 || data.status === '401') {
		if (onNotFoundMessage) {
			throw error(404, onNotFoundMessage);
		}
		throw error(404, 'Not found');
	}

	return data;
}
