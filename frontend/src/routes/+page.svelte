<script lang="ts">
	import Icon from '$lib/components/Icon.svelte';
	import Canvas from '$lib/components/Canvas.svelte';
	import SquareLoading from '$lib/components/Loader/SquareLoading.svelte';
	import Table from '$lib/components/Table.svelte';

	let fileVar: any;
	let isLoading = false;
	let msg: any;

	export let name: any;

	async function submitForm() {
		isLoading = true;
		const data = new FormData();
		data.append('file', fileVar[0]);
		//console.log(JSON.stringify(data));
		//console.log(fileVar);
		//console.log(JSON.stringify(fileVar));

		const res = await fetch('http://localhost:8080/prediction', {
			method: 'POST',
			body: data
		});
		isLoading = false;
		msg = await res.json();
	}

	async function getHello() {
		const res = await fetch(`http://localhost:8080`);
		const text = await res.text();

		if (res.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}
</script>

<div>
	<div class="md:grid md:grid-cols-3 md:gap-6 ">
		<div class="md:col-span-1 flex items-center">
			<div class="px-4 sm:px-0">
				<h2 class="text-4xl font-bold sm:text-3xl md:text-3xl lg:text-5xl xl:text-4xl">
					¡Bienvenido!
				</h2>
				<p class="mt-1  dark:text-gray-300 text-gray-600">
					Visualiza medios porosos en 3D a partir de cortes bidimensionales
				</p>
			</div>
		</div>
		<div class="mt-5 md:mt-0 md:col-span-2">
			<form class="space-y-8 divide-y">
				<div class="flex justify-center items-center w-full">
					<label
						for="dropzone-file"
						class="flex flex-col justify-center items-center w-full h-64 bg-gray-50 rounded-lg border-2 border-gray-300 border-dashed cursor-pointer dark:hover:bg-bray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
					>
						<div class="flex flex-col justify-center items-center pt-5 pb-6 ">
							<svg
								aria-hidden="true"
								class="mb-3 w-10 h-10 text-gray-400"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
								xmlns="http://www.w3.org/2000/svg"
								><path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
								/></svg
							>

							<p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
								<span class="font-semibold"
									>Haz click para subir una secuencia de medios porosos</span
								>
							</p>
							<p class="text-xs text-gray-500 dark:text-gray-400">.ZIP or .npy</p>
						</div>
						<input
							id="dropzone-file"
							bind:files={fileVar}
							type="file"
							class="hidden"
							accept=".zip,.npy"
						/>
					</label>
				</div>
			</form>
		</div>
	</div>
</div>

<form class="my-12" on:submit|preventDefault={submitForm}>
	<input
		value="Predecir Cortes"
		type="submit"
		class="inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-teal-500 hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-teal-500"
	/>
</form>

{#if isLoading}
	<div class="text-center">
		<SquareLoading />

		<p>... cargando</p>
	</div>
{/if}

{#if msg}
	<h1
		class="dark:text-gray-300 text-gray-600 my-5 text-4xl font-bold sm:text-3xl md:text-3xl lg:text-5xl xl:text-4xl"
	>
		Resultados de medio poroso
	</h1>
	<div class="grid grid-cols-4 gap-6">
		<div>
			<h3>Porosidad:</h3>
			<p>{msg.porosity}</p>
			<h3>Tau:</h3>
			<p>{msg.tau}</p>
		</div>
		<Table porosity={msg.porosity} tau={msg.tau} />
		<Canvas />
	</div>
{/if}
