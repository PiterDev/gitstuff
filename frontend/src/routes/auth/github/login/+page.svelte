<script lang="ts">
	import { PUBLIC_GH_CLIENT_ID } from "$env/static/public";

    let { data } = $props();
    
    const githubAuthUrl = 'https://github.com/login/oauth/authorize';
    const clientId = PUBLIC_GH_CLIENT_ID;
    const scope = 'user repo';
    const redirectUri = 'http://gitstuff.piterdev.me/auth/github/callback';

    function githubRedirect() {
        const url = `${githubAuthUrl}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}`;
        window.location.href = url;
    }
</script>

<main>
    {#if data.sessionExpired}
        <p>Your session has expired. Please login again.</p>
    {:else}
        <p>Please Log in with GitHub.</p>
    {/if}

    <button onclick={githubRedirect}>Login with GitHub</button>
</main>

<style lang="scss">
    main {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    button {
        padding: 1rem;
        border-radius: 10rem;
        color: #000;
        text-decoration: none;
        background: #fff;
        border: 1px solid rgb(45, 45, 45);
    }

</style>