<script>
	import { onMount } from "svelte";
	import { getPostings, trainWords } from './api.js';
	import Posting from './Posting.svelte';

	async function vetWords(evt) {
		console.log('evt=',evt);
		const { type, detail } = evt;
		if (type !== 'submit') {
			return;
		}

		const { posting, vettedWords } = detail;
		await trainWords(posting._id, vettedWords);
	}

	let postings = [];
	let total = 0;
	let error;
	let isLoading = true;
	onMount(async () => {
		try {
			const resp = await getPostings({ limit: 5 });
			if (!resp) {
				throw 'Empty response';
			}
			total = resp.total;
			postings = resp.hits;
		} catch(e) {
			error = `Error occurred: ${e}`;
		} finally {
			isLoading = false;
		}
	});
</script>

<main>
	{#if isLoading}
		<h1 class="loading">Loading...</h1>
	{:else}
		{#if error}
			<div class="error">
				{error}
			</div>
		{/if}
		<h2>Total: {total}</h2>
		<div>
			{#each postings as posting}
				<Posting {posting} on:submit={vetWords} />
			{/each}
		</div>
	{/if}
</main>

<style>
	main {
		height: 100%;
		width: 100%;
	}

	.loading {
		display: flex;
		justify-content: center;
    	align-items: center;
		width: 100%;
		height: 100%;
		margin: auto;
		font-size: 4em;
	}

	.error {
		color: red;
	}
</style>
