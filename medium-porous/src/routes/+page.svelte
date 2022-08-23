<script lang="ts">
	import Icon from '$lib/components/Icon.svelte';
	import zip from '$lib/assets/icons/zip.svg?raw';

	let fileVar: any;
	let isLoading = false;
	let msg: any;

	async function submitForm() {
		isLoading = true;
		const data = new FormData();
		data.append('file', fileVar[0]);
		//console.log(JSON.stringify(data));
		//console.log(fileVar);
		//console.log(JSON.stringify(fileVar));

		const res = await fetch('http://127.0.0.1:8000/upload', {
			method: 'POST',
			body: data
		});
		isLoading = false;
		msg = await res.json();
	}

	async function getHello() {
		const res = await fetch(`http://127.0.0.1:8000/`);
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
				<p class="mt-1  dark:text-gray-300 text-gray-600">Algo sobre el proyecto</p>
			</div>
		</div>
		<div class="mt-5 md:mt-0 md:col-span-2">
			<form class="space-y-8 divide-y">
				<div
					class="px-4 py-5 dark:bg-slate-700 bg-white space-y-6 sm:p-6 shadow sm:rounded-md sm:overflow-hidden  sm:grid sm:grid-cols-3 sm:gap-3 sm:items-start  sm: sm:pt-5"
				>
					<label
						for="the-file"
						class="block text-sm font-medium dark:text-gray-200 text-gray-700 sm:mt-px sm:pt-2"
					>
						Secuencia de medios porosos:
					</label>
					<div class="mt-1 sm:mt-0 sm:col-span-2">
						<div
							class="max-w-lg flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md"
						>
							<div class="space-y-1 text-center text-gray-400">
								<Icon
									class="mx-auto h-12 w-12"
									fill="currentColor"
									stroke={'text-gray-200'}
									data={zip}
								/>

								<div class="flex text-sm text-gray-600 ">
									<label
										for="file-upload"
										class="relative cursor-pointer dark:bg-slate-700 dark:text-teal-300 bg-white rounded-md font-medium text-teal-600 hover:text-teal-500 focus-within:outline-none focus-within:ring-2  focus-within:ring-teal-500"
									>
										<span>Subir archivo</span>
										<input
											id="file-upload"
											name="file-upload"
											type="file"
											class="sr-only"
											accept=".zip,.npy"
											bind:files={fileVar}
										/>
									</label>
								</div>
							</div>
							<p class="text-xs dark:text-gray-300 text-gray-500">Zip o npy</p>
						</div>
					</div>
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
		<p>... cargando</p>
	</div>
{/if}

{#if msg}
	<div class="text-center">
		<p>{JSON.stringify(msg)}</p>
	</div>
{/if}

<!-- svelte-ignore a11y-missing-attribute -->
<iframe
	id="vs_iframe"
	src="https://www.viewstl.com/?embedded"
	style="border:0;margin:0;width:100%;height:100%;"
/>
