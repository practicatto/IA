<script lang="ts">
	import SquareLoading from './Loader/SquareLoading.svelte';

	async function get_medium() {
		const medium = await fetch('http://localhost:8080/models/output');
		if (medium.status === 200) {
			return medium;
		} else {
			throw new Error(medium.statusText);
		}
	}

	let medium = get_medium();
</script>

{#await medium}
	<SquareLoading />
{:then response}
	<model-viewer
		alt=""
		src="http://localhost:8080/models/output"
		ar
		ar-modes="webxr scene-viewer quick-look"
		environment-image="neutral"
		auto-rotate
		camera-controls
	/>
{:catch error}
	<div class="text-center">
		<p class="text-red-500">{error.message}</p>
	</div>
{/await}
