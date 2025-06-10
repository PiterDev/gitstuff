<script lang="ts">
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();

  let name = "";
  let description = "";

  function handleSubmit(e: Event) {
    e.preventDefault();
    if (!name.trim()) return;
    dispatch("create", { name, description });
    name = "";
    description = "";
  }
</script>

<form class="add-repo-form" on:submit|preventDefault={handleSubmit}>
  <input
    class="repo-input"
    type="text"
    placeholder="Issue title"
    bind:value={name}
    required
    maxlength="100"
  />
  <input
    class="repo-input"
    type="text"
    placeholder="Description (optional)"
    bind:value={description}
    maxlength="200"
  />
  <button class="create-btn" type="submit">Create</button>
</form>

<style>
  .add-repo-form {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: #464646;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    margin-top: 1.5rem;
    width: 100%;
    min-height: 3.2rem;
    box-sizing: border-box;
  }

  .repo-input {
    background: #292929;
    color: #fff;
    border: 1px solid #444;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    flex: 1 1 0;
    outline: none;
    transition: border 0.2s;
  }
  .repo-input:focus {
    border: 1.5px solid #8ab4f8;
  }

  .create-btn {
    background: #8ab4f8;
    color: #232323;
    border: none;
    border-radius: 6px;
    padding: 0.5rem 1.2rem;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
    height: 2.2rem;
    min-width: 5.5rem;
  }
  .create-btn:hover {
    background: #5b8bd6;
    color: #fff;
  }
</style>