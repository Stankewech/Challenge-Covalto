document.addEventListener('DOMContentLoaded', () => {
    const loadBtn = document.getElementById('load-family-btn');
    const gridContainer = document.getElementById('character-grid');
    
    const timeStatValue = document.querySelector('#time-stat strong');
    const timeStatLabel = document.querySelector('#time-stat small');

    // Diccionario de códigos HTTP
    const httpMessages = {
        200: "OK",
        201: "Created",
        204: "No Content",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable"
    };

    const customBios = {
        1: "Genio científico, alcohólico y abuelo sociópata. Arrastra a su nieto a aventuras extremadamente peligrosas a través del multiverso.",
        2: "Nieto ansioso y de buen corazón. Su ingenuidad es constantemente puesta a prueba por los traumas interdimensionales causados por Rick.",
        3: "Hermana mayor de Morty. Típicamente obsesionada con su estatus social, pero sorprendentemente capaz en situaciones apocalípticas.",
        4: "Hija de Rick y cirujana de caballos. Lucha constantemente con problemas de abandono, una superioridad intelectual reprimida y su matrimonio.",
        5: "Padre de familia inseguro, patético pero bien intencionado. Generalmente despreciado por Rick y frecuentemente desempleado."
    };

    async function fetchFamily() {
        const characterIds = [1, 2, 3, 4, 5]; 
        
        try {
            gridContainer.innerHTML = '<div class="loader">Ejecutando pruebas de API...</div>';
            loadBtn.disabled = true;

            const globalStartTime = performance.now();

            const requests = characterIds.map(async (id) => {
                const startTime = performance.now();
                let status = 500;
                let data = null;

                try {
                    const response = await fetch(`https://rickandmortyapi.com/api/character/${id}`);
                    status = response.status; 
                    data = await response.json();
                } catch (err) {
                    console.error(`Error en ID ${id}:`, err);
                }

                const endTime = performance.now();
                
                return {
                    data: data,
                    httpStatus: status,
                    latency: (endTime - startTime).toFixed(0) 
                };
            });

            const results = await Promise.all(requests);

            const globalEndTime = performance.now();
            const totalBatchTime = (globalEndTime - globalStartTime).toFixed(0);
            
            if(timeStatValue && timeStatLabel) {
                timeStatValue.textContent = `${totalBatchTime}ms`;
                timeStatLabel.textContent = `Total Batch Time`;
            }

            renderSneakerCards(results);

        } catch (error) {
            console.error("Error general:", error);
            gridContainer.innerHTML = `<div class="empty-state">Ocurrió un error en las pruebas.</div>`;
        } finally {
            loadBtn.disabled = false;
        }
    }

    function renderSneakerCards(results) {
        gridContainer.innerHTML = '';

        results.forEach(result => {
            const char = result.data;
            if (!char) return; 

            const bio = customBios[char.id] || "Información clasificada.";
            
            const statusClass = result.httpStatus === 200 ? 'http-ok' : 'http-err';
            const vitalStatus = char.status === 'Alive' ? 'Vivo' : char.status === 'Dead' ? 'Muerto' : '???';
            const vitalClass = char.status === 'Alive' ? 'vivo' : char.status === 'Dead' ? 'muerto' : 'desconocido';

            // Extracción del mensaje de código de estado
            const statusText = httpMessages[result.httpStatus] || "Unknown Status";

            const card = document.createElement('article');
            card.className = 'sneaker-card';
            
            card.innerHTML = `
                <div class="sc-header">
                    <h3 class="sc-title">${char.name}</h3>
                    <p class="sc-subtitle">Especie: ${char.species} • ID: 00${char.id}</p>
                </div>
                
                <div class="sc-image-box">
                    <img src="${char.image}" alt="Retrato estático" loading="lazy">
                    <div class="sc-bio-overlay">
                        <p>${bio}</p>
                    </div>
                </div>
                
                <div class="sc-footer">
                    <div class="sc-metrics">
                        <p class="sc-status-code ${statusClass}">${result.httpStatus} <span style="text-transform: uppercase; margin-left: 4px;">${statusText}</span></p>
                        <p class="sc-time">ejecución en ${result.latency} ms</p>
                    </div>
                    <button class="sc-btn ${vitalClass}">${vitalStatus}</button>
                </div>
            `;
            
            gridContainer.appendChild(card);
        });
    }

    loadBtn.addEventListener('click', fetchFamily);
});