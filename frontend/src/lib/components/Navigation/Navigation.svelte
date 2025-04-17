<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/dashboard">Dashboard</a></li>
        <li><a href="/auth/github/login">Login</a></li> 
    </ul>
</nav>

<style lang="scss">
    nav {
        margin: 0;
        padding: 0;
        width: 100vw;

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        padding: 1rem;
        margin-bottom: 1rem;

        border-bottom: #fff solid 1px;
    }

    ul {
        margin: 0;
        padding: 0;

        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
    }

    li {
        list-style: none;
    }

</style>