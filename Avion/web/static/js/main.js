// API Configuration
const API_CONFIG = {
    baseUrl: 'http://localhost:8000',
    endpoints: {
        generate: '/api/generate',
        analyze: '/api/analyze',
        optimize: '/api/optimize'
    }
};

// Token Generation
async function generateToken(concept, style) {
    try {
        const response = await fetch(`${API_CONFIG.baseUrl}${API_CONFIG.endpoints.generate}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                concept,
                style
            })
        });

        if (!response.ok) {
            throw new Error('Generation failed');
        }

        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// UI Interactions
function showLoading() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('result').style.display = 'none';
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
    document.getElementById('result').style.display = 'block';
}

function updateUI(data) {
    document.getElementById('tokenName').textContent = data.name;
    document.getElementById('tokenImage').src = data.image_url;
    document.getElementById('tokenDescription').textContent = data.description;
}

// Event Handlers
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('generationForm');
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const concept = document.getElementById('concept').value;
        const style = document.getElementById('style').value;
        
        showLoading();
        
        try {
            const result = await generateToken(concept, style);
            updateUI(result);
        } catch (error) {
            alert('Generation failed. Please try again.');
        } finally {
            hideLoading();
        }
    });
}); 