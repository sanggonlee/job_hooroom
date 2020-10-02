<script>
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher();

    export let posting;

    let currentWords = posting.words.filter(Boolean);
    let newWord = '';

    function addWord(evt) {
        currentWords = [...currentWords, newWord];
        newWord = '';
    }

    function removeWord(word) {
        currentWords = currentWords.filter(currentWord => currentWord !== word);
    }

    function updateNewWord(evt) {
        newWord = evt.target.value;
    }

    function submit() {
        dispatch('submit', {
           posting,
           vettedWords: currentWords,
        });
    }
</script>

<main>
    <h3>{posting.title}</h3>
    <p>{posting.description}</p>
    <div>
        {#each currentWords as word}
            <span class="word-pill">
                {word}
                <button class="remove-word" on:click={() => removeWord(word)}>-</button>
            </span>
        {/each}
    </div>
    <div class="add-word">
        <input type="text" on:change={updateNewWord} value={newWord} />
        <button on:click={addWord}>+</button>
    </div>
    <button class="submit" on:click={submit}>
        Confirm
    </button>
</main>

<style>
    .word-pill {
        display: inline-block;
        padding: 5px 10px;
        margin: 3px;
        border-radius: 2px;
        background-color: lightblue;
    }

    .add-word > input {
        height: 30px;
        margin-right: -5px;
    }

    .add-word > button {
        padding: 5px 10px;
        color: white;
        background-color: cornflowerblue;
        border-radius: 2px;
    }

    .remove-word {
        color: black;
        background-color: white;
        border-radius: 3px;
        margin: 0;
        padding: 5px 10px;
    }
</style>
